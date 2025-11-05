"""
AI Interviewer Backend API
A professional Flask application for AI-powered interview assessments using OpenAI GPT.
"""

import os
import logging
from typing import Dict, Any
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI, OpenAIError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configuration
class Config:
    """Application configuration"""
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'Add-your-key')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4o-mini')
    MAX_RETRIES = 3
    REQUEST_TIMEOUT = 30

# Initialize OpenAI client
try:
    client = OpenAI(api_key=Config.OPENAI_API_KEY)
    logger.info("OpenAI client initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize OpenAI client: {e}")
    client = None

def validate_input_data(data: Dict[str, Any]) -> tuple[bool, str]:
    """
    Validate the input data for the interview endpoint.

    Args:
        data: JSON data from the request

    Returns:
        tuple: (is_valid, error_message)
    """
    required_fields = ['name', 'qualification', 'skills', 'jobRole', 'answers']

    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"

    if not isinstance(data['answers'], dict):
        return False, "Answers must be a dictionary"

    required_answers = ['q1', 'q2', 'q3']
    for answer_key in required_answers:
        if answer_key not in data['answers']:
            return False, f"Missing answer for question: {answer_key}"
        if not data['answers'][answer_key].strip():
            return False, f"Answer for question {answer_key} cannot be empty"

    # Basic validation for other fields
    if not data['name'].strip():
        return False, "Name cannot be empty"
    if not data['jobRole'].strip():
        return False, "Job role cannot be empty"

    return True, ""

def create_interview_prompt(data: Dict[str, Any]) -> str:
    """
    Create a professional prompt for the AI interviewer.

    Args:
        data: Interview data

    Returns:
        str: Formatted prompt
    """
    return f"""
You are an experienced HR professional conducting a technical interview assessment.

CANDIDATE INFORMATION:
- Name: {data['name']}
- Qualification: {data['qualification']}
- Skills: {data['skills']}
- Applied Position: {data['jobRole']}

INTERVIEW RESPONSES:
1. Professional Experience: {data['answers']['q1']}
2. Key Project: {data['answers']['q2']}
3. Challenge Handling: {data['answers']['q3']}

Please provide a comprehensive evaluation in exactly 5 bullet points:

1. **Technical Strengths**: Highlight the candidate's technical competencies and relevant experience
2. **Areas for Development**: Identify skills gaps or weaknesses that need improvement
3. **Communication Skills**: Assess clarity, professionalism, and presentation of ideas
4. **Overall Recommendation**: Provide specific advice for hiring managers
5. **Final Decision**: Choose ONE: "HIRE", "CONSIDER", or "REJECT" with brief justification

Format each point as a clear, professional assessment. Be constructive and specific.
"""

def parse_ai_response(response_text: str) -> Dict[str, str]:
    """
    Parse the AI response into structured feedback.

    Args:
        response_text: Raw AI response

    Returns:
        dict: Structured feedback
    """
    lines = [line.strip() for line in response_text.split('\n') if line.strip()]

    feedback = {
        "technical_strengths": "Unable to analyze technical strengths",
        "weaknesses": "Unable to analyze areas for development",
        "communication": "Unable to analyze communication skills",
        "recommendation": "Unable to provide recommendation",
        "decision": "Unable to make final decision"
    }

    # Try to extract numbered responses
    for line in lines:
        if line.startswith('1.') or '**Technical Strengths**' in line:
            feedback["technical_strengths"] = line.split(':', 1)[-1].strip() if ':' in line else line
        elif line.startswith('2.') or '**Areas for Development**' in line:
            feedback["weaknesses"] = line.split(':', 1)[-1].strip() if ':' in line else line
        elif line.startswith('3.') or '**Communication Skills**' in line:
            feedback["communication"] = line.split(':', 1)[-1].strip() if ':' in line else line
        elif line.startswith('4.') or '**Overall Recommendation**' in line:
            feedback["recommendation"] = line.split(':', 1)[-1].strip() if ':' in line else line
        elif line.startswith('5.') or '**Final Decision**' in line:
            feedback["decision"] = line.split(':', 1)[-1].strip() if ':' in line else line

    return feedback

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "AI Interviewer API",
        "openai_status": "available" if client else "unavailable"
    })

@app.errorhandler(400)
def bad_request(error):
    """Handle bad request errors"""
    return jsonify({
        "error": "Bad Request",
        "message": "Invalid input data provided"
    }), 400

@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors"""
    logger.error(f"Internal server error: {error}")
    return jsonify({
        "error": "Internal Server Error",
        "message": "An unexpected error occurred"
    }), 500

@app.post("/interview")
def interview():
    """
    Process interview data and generate AI-powered feedback.

    Expected JSON payload:
    {
        "name": "string",
        "qualification": "string",
        "skills": "string",
        "jobRole": "string",
        "answers": {
            "q1": "string",
            "q2": "string",
            "q3": "string"
        }
    }
    """
    try:
        # Get and validate input data
        data = request.get_json()
        if not data:
            logger.warning("No JSON data provided in request")
            return jsonify({"error": "No data provided"}), 400

        is_valid, error_message = validate_input_data(data)
        if not is_valid:
            logger.warning(f"Invalid input data: {error_message}")
            return jsonify({"error": error_message}), 400

        # Check if OpenAI client is available
        if not client:
            logger.error("OpenAI client not initialized")
            return jsonify({"error": "AI service unavailable"}), 503

        # Create prompt and call OpenAI API
        prompt = create_interview_prompt(data)
        logger.info(f"Processing interview for candidate: {data['name']}")

        response = client.chat.completions.create(
            model=Config.OPENAI_MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000,
            temperature=0.7
        )

        # Parse and return feedback
        ai_response = response.choices[0].message.content
        feedback = parse_ai_response(ai_response)

        logger.info(f"Successfully processed interview for {data['name']}")

        return jsonify(feedback)

    except OpenAIError as e:
        logger.error(f"OpenAI API error: {e}")
        return jsonify({
            "error": "AI service error",
            "message": "Unable to generate feedback at this time"
        }), 503
    except Exception as e:
        logger.error(f"Unexpected error in interview endpoint: {e}")
        return jsonify({
            "error": "Processing error",
            "message": "An unexpected error occurred while processing your request"
        }), 500

if __name__ == "__main__":
    logger.info("Starting AI Interviewer API server")
    app.run(
        debug=os.getenv('FLASK_DEBUG', 'True').lower() == 'true',
        host='127.0.0.1',
        port=int(os.getenv('PORT', 5000))
    )
