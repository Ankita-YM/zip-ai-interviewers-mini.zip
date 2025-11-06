# AI Interviewer

A modern, professional AI-powered interview assessment tool built with Flask, OpenAI GPT, and a responsive web interface.

## Features

- **AI-Powered Assessment**: Uses OpenAI GPT-4o-mini for intelligent candidate evaluation
- **Modern UI**: Beautiful, responsive web interface with card-based design
- **Professional Backend**: Production-ready Flask API with comprehensive error handling
- **Real-time Feedback**: Instant AI-generated interview feedback
- **Secure**: Proper input validation and error handling

## Tech Stack

- **Backend**: Python Flask with OpenAI integration
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **AI**: OpenAI GPT-4o-mini
- **Styling**: Modern CSS with gradients and animations
- **Icons**: Font Awesome

## Architecture Overview

```mermaid
graph TB
    A["User Interface<br/>HTML/CSS/JavaScript"] -->|HTTP Requests| B["Flask Backend<br/>Python"]
    B -->|REST API| A
    B -->|OpenAI API| C["OpenAI GPT-4o-mini<br/>AI Engine"]
    C -->|AI Response| B
    B -->|Database| D["Request Logs<br/>& History"]
    
    style A fill:#667eea,stroke:#333,stroke-width:2px,color:#fff
    style B fill:#764ba2,stroke:#333,stroke-width:2px,color:#fff
    style C fill:#4ecdc4,stroke:#333,stroke-width:2px,color:#fff
    style D fill:#44a08d,stroke:#333,stroke-width:2px,color:#fff
```

## Application Flow

```mermaid
sequenceDiagram
    participant User as User Browser
    participant Frontend as Frontend Server
    participant Backend as Backend API
    participant OpenAI as OpenAI Service

    User->>Frontend: Access Application
    Frontend->>User: Load Modern UI
    
    User->>User: Fill Personal Info
    User->>User: Answer Questions
    
    User->>Backend: Submit Interview Data
    Backend->>Backend: Validate Input
    Backend->>OpenAI: Send Prompt
    OpenAI->>Backend: Return AI Assessment
    Backend->>Backend: Parse Response
    Backend->>User: Return Feedback JSON
    Frontend->>User: Display Results
```

## User Journey

```mermaid
flowchart TD
    A["Start Application"] -->|Load Page| B["Personal Information Card"]
    B -->|Fill Details| C{Validation<br/>Check}
    C -->|Invalid| D["Show Error Message"]
    D -->|Correct| B
    C -->|Valid| E["Interview Questions Card"]
    E -->|Answer Questions| F{All Questions<br/>Answered}
    F -->|No| G["Show Validation Error"]
    G -->|Complete| E
    F -->|Yes| H["Submit to Backend"]
    H -->|Processing| I["API Call to OpenAI"]
    I -->|Success| J["Results Card"]
    I -->|Error| K["Error Notification"]
    K -->|Retry| E
    J -->|View Results| L["Display Feedback Report"]
    L -->|New Interview| B
    
    style A fill:#667eea,stroke:#333,stroke-width:2px,color:#fff
    style B fill:#764ba2,stroke:#333,stroke-width:2px,color:#fff
    style E fill:#764ba2,stroke:#333,stroke-width:2px,color:#fff
    style J fill:#4ecdc4,stroke:#333,stroke-width:2px,color:#fff
    style L fill:#44a08d,stroke:#333,stroke-width:2px,color:#fff
    style D fill:#e74c3c,stroke:#333,stroke-width:2px,color:#fff
    style K fill:#e74c3c,stroke:#333,stroke-width:2px,color:#fff
    style C fill:#f39c12,stroke:#333,stroke-width:2px,color:#fff
    style F fill:#f39c12,stroke:#333,stroke-width:2px,color:#fff
```

## System Architecture

```mermaid
graph LR
    subgraph Client["Client Layer"]
        HTML["HTML Structure"]
        CSS["CSS Styling"]
        JS["JavaScript Logic"]
    end
    
    subgraph Server["Server Layer"]
        Flask["Flask Framework"]
        Validation["Input Validation"]
        ErrorHandler["Error Handling"]
    end
    
    subgraph AI["AI Processing"]
        Prompt["Prompt Engineering"]
        OpenAI["OpenAI API"]
        Parser["Response Parser"]
    end
    
    Client -->|HTTP| Server
    Server -->|Requests| AI
    AI -->|Results| Server
    Server -->|JSON Response| Client
    
    style Client fill:#667eea,stroke:#333,stroke-width:2px,color:#fff
    style Server fill:#764ba2,stroke:#333,stroke-width:2px,color:#fff
    style AI fill:#4ecdc4,stroke:#333,stroke-width:2px,color:#fff
    style HTML fill:#5e72e4,stroke:#333,stroke-width:1px,color:#fff
    style CSS fill:#5e72e4,stroke:#333,stroke-width:1px,color:#fff
    style JS fill:#5e72e4,stroke:#333,stroke-width:1px,color:#fff
    style Flask fill:#6c5ce7,stroke:#333,stroke-width:1px,color:#fff
    style Validation fill:#6c5ce7,stroke:#333,stroke-width:1px,color:#fff
    style ErrorHandler fill:#6c5ce7,stroke:#333,stroke-width:1px,color:#fff
    style Prompt fill:#00b894,stroke:#333,stroke-width:1px,color:#fff
    style OpenAI fill:#00b894,stroke:#333,stroke-width:1px,color:#fff
    style Parser fill:#00b894,stroke:#333,stroke-width:1px,color:#fff
```

## Prerequisites

- Python 3.8+
- OpenAI API Key
- Modern web browser

## Installation

1. **Clone the repository** (if applicable) or navigate to the project directory

2. **Install Python dependencies**:
   ```bash
   pip install flask openai flask-cors
   ```

3. **Get OpenAI API Key**:
   - Visit https://platform.openai.com/account/api-keys
   - Create a new secret key
   - Copy the key (starts with `sk-proj-`)

4. **Configure API Key**:
   - Open `backend/ai_interview.py`
   - Replace `'your-api-key-here'` with your actual OpenAI API key:
   ```python
   OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'sk-proj-your-actual-key-here')
   ```

## Running the Application

### Start Backend Server:
```bash
cd backend
python ai_interview.py
```
The backend will run on `http://127.0.0.1:5000`

### Start Frontend Server:
```bash
cd frontend
python -m http.server 8000
```
The frontend will run on `http://localhost:8000`

### Access the Application:
Open your browser and go to `http://localhost:8000`

## Usage

1. **Fill Personal Information**:
   - Enter your name, qualification, skills
   - Select the job role you're applying for

2. **Answer Interview Questions**:
   - Describe your relevant experience
   - Detail your biggest project
   - Explain how you handle challenges

3. **Get AI Feedback**:
   - Click "Finish Interview"
   - Receive comprehensive AI-powered assessment
   - View technical strengths, weaknesses, communication skills, recommendations, and final decision

## Project Structure

```
ai-interviewer-mini/
├── backend/
│   ├── ai_interview.py      # Flask API server
│   └── .env                 # Environment variables
├── frontend/
│   ├── index.html           # Main HTML page
│   ├── style.css            # Modern CSS styling
│   └── script.js            # Frontend JavaScript
└── README.md                # Documentation
```

## Data Flow Diagram

```mermaid
graph TB
    User["Candidate Data Input"] -->|Interview Form| Frontend["Frontend Processing"]
    Frontend -->|JSON Payload| Request["HTTP POST Request"]
    Request -->|/interview| Backend["Backend Processing"]
    Backend -->|Validation| Validate["Input Validation"]
    Validate -->|Valid Data| Prompt["Create AI Prompt"]
    Prompt -->|Send Request| OpenAI["OpenAI API Call"]
    OpenAI -->|AI Response| Response["Receive Feedback"]
    Response -->|Parse| Parser["Response Parser"]
    Parser -->|Structured Data| Output["Generate Report"]
    Output -->|JSON Response| Display["Display Results"]
    Display -->|Feedback Report| Browser["Show to Candidate"]
    
    style User fill:#667eea,stroke:#333,stroke-width:2px,color:#fff
    style Frontend fill:#764ba2,stroke:#333,stroke-width:2px,color:#fff
    style Request fill:#764ba2,stroke:#333,stroke-width:2px,color:#fff
    style Backend fill:#6c5ce7,stroke:#333,stroke-width:2px,color:#fff
    style Validate fill:#6c5ce7,stroke:#333,stroke-width:2px,color:#fff
    style Prompt fill:#6c5ce7,stroke:#333,stroke-width:2px,color:#fff
    style OpenAI fill:#4ecdc4,stroke:#333,stroke-width:2px,color:#fff
    style Response fill:#4ecdc4,stroke:#333,stroke-width:2px,color:#fff
    style Parser fill:#6c5ce7,stroke:#333,stroke-width:2px,color:#fff
    style Output fill:#44a08d,stroke:#333,stroke-width:2px,color:#fff
    style Display fill:#44a08d,stroke:#333,stroke-width:2px,color:#fff
    style Browser fill:#667eea,stroke:#333,stroke-width:2px,color:#fff
```

## API Endpoints

### POST `/interview`
Processes interview data and returns AI feedback.

**Request Body:**
```json
{
  "name": "John Doe",
  "qualification": "Bachelor's in Computer Science",
  "skills": "Python, JavaScript, SQL",
  "jobRole": "Python Developer",
  "answers": {
    "q1": "I have 3 years of experience...",
    "q2": "My biggest project was...",
    "q3": "When facing challenges, I..."
  }
}
```

**Response:**
```json
{
  "technical_strengths": "Strong Python expertise...",
  "weaknesses": "Limited experience in...",
  "communication": "Clear and professional...",
  "recommendation": "Consider for junior role...",
  "decision": "HIRE"
}
```

### GET `/health`
Health check endpoint for monitoring.

## Feedback Generation Pipeline

```mermaid
graph TD
    A["Candidate Answers"] -->|q1: Experience| B["Build Interview Context"]
    A -->|q2: Project| B
    A -->|q3: Challenges| B
    B -->|Profile Data| C["Create AI Prompt"]
    C -->|Technical Prompt| D["GPT-4o-mini Model"]
    D -->|Raw Assessment| E["Parse Response"]
    E -->|5 Feedback Areas| F["Technical Strengths"]
    E -->|5 Feedback Areas| G["Weaknesses"]
    E -->|5 Feedback Areas| H["Communication"]
    E -->|5 Feedback Areas| I["Recommendation"]
    E -->|5 Feedback Areas| J["Final Decision"]
    F -->|Structured| K["Build Report"]
    G -->|Structured| K
    H -->|Structured| K
    I -->|Structured| K
    J -->|Structured| K
    K -->|Format HTML| L["Send to Frontend"]
    L -->|Display| M["Show Candidate"]
    
    style A fill:#667eea,stroke:#333,stroke-width:2px,color:#fff
    style B fill:#764ba2,stroke:#333,stroke-width:2px,color:#fff
    style C fill:#6c5ce7,stroke:#333,stroke-width:2px,color:#fff
    style D fill:#4ecdc4,stroke:#333,stroke-width:2px,color:#fff
    style E fill:#6c5ce7,stroke:#333,stroke-width:2px,color:#fff
    style F fill:#44a08d,stroke:#333,stroke-width:1px,color:#fff
    style G fill:#44a08d,stroke:#333,stroke-width:1px,color:#fff
    style H fill:#44a08d,stroke:#333,stroke-width:1px,color:#fff
    style I fill:#44a08d,stroke:#333,stroke-width:1px,color:#fff
    style J fill:#44a08d,stroke:#333,stroke-width:1px,color:#fff
    style K fill:#00b894,stroke:#333,stroke-width:2px,color:#fff
    style L fill:#667eea,stroke:#333,stroke-width:2px,color:#fff
    style M fill:#764ba2,stroke:#333,stroke-width:2px,color:#fff
```

## Security Features

- Input validation and sanitization
- CORS enabled for frontend communication
- Error handling without exposing sensitive information
- Secure API key management

## Error Handling

The application includes comprehensive error handling:

- **Invalid API Key**: Returns user-friendly error message
- **Network Issues**: Graceful fallback with retry logic
- **Invalid Input**: Detailed validation with specific error messages
- **Server Errors**: Proper logging and 500 error responses

## UI Features

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Modern Aesthetics**: Gradient backgrounds, shadows, and animations
- **Card-Based Layout**: Clean, professional interface
- **Loading States**: Visual feedback during processing
- **Error Notifications**: User-friendly error messages

## Development

### Adding New Features:
1. Backend changes in `ai_interview.py`
2. Frontend changes in respective HTML/CSS/JS files
3. Test both servers together

### Environment Variables:
```bash
export OPENAI_API_KEY="your-key-here"
export FLASK_DEBUG="True"
export PORT="5000"
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Feel free to use and modify as needed.

---
## Special Thanks To
- OpenAI for their powerful language models.
- The Flask community for their excellent web framework.
- **Developed by:** @Tanishq-JM
