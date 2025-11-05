// Utility functions
function showCard(cardId) {
    document.querySelectorAll('.card').forEach(card => card.classList.add('hidden'));
    document.getElementById(cardId).classList.remove('hidden');
    document.getElementById(cardId).classList.add('fade-in');
}

function validateForm() {
    const name = document.getElementById("name").value.trim();
    const qualification = document.getElementById("qualification").value.trim();
    const skills = document.getElementById("skills").value.trim();
    const jobRole = document.getElementById("jobRole").value;

    if (!name || !qualification || !skills || !jobRole) {
        showNotification("Please fill in all fields.", "error");
        return false;
    }
    return true;
}

function validateQuestions() {
    const answers = {
        q1: document.getElementById("q1").value.trim(),
        q2: document.getElementById("q2").value.trim(),
        q3: document.getElementById("q3").value.trim()
    };

    if (!answers.q1 || !answers.q2 || !answers.q3) {
        showNotification("Please answer all questions.", "error");
        return false;
    }
    return true;
}

function showNotification(message, type = "info") {
    // Simple notification - you could enhance this with a proper notification system
    alert(message);
}

// Event listeners
document.getElementById("startInterview").addEventListener("click", () => {
    if (validateForm()) {
        showCard('questions-card');
    }
});

document.getElementById("backToPersonal").addEventListener("click", () => {
    showCard('personal-card');
});

document.getElementById("finishInterview").addEventListener("click", async () => {
    if (!validateQuestions()) return;

    const finishBtn = document.getElementById("finishInterview");
    finishBtn.disabled = true;
    finishBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';

    // Get form data
    const name = document.getElementById("name").value;
    const qualification = document.getElementById("qualification").value;
    const skills = document.getElementById("skills").value;
    const jobRole = document.getElementById("jobRole").value;
    const answers = {
        q1: document.getElementById("q1").value,
        q2: document.getElementById("q2").value,
        q3: document.getElementById("q3").value
    };

    try {
        const res = await fetch("http://127.0.0.1:5000/interview", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                name,
                qualification,
                skills,
                jobRole,
                answers
            })
        });

        if (!res.ok) {
            throw new Error(`HTTP error! status: ${res.status}`);
        }

        const data = await res.json();

        // Generate feedback HTML
        const feedbackHTML = `
            <div class="feedback-section">
                <h3><i class="fas fa-user"></i> Candidate Details</h3>
                <table class="feedback-table">
                    <tr><th>Full Name</th><td>${name}</td></tr>
                    <tr><th>Qualification</th><td>${qualification}</td></tr>
                    <tr><th>Skills</th><td>${skills}</td></tr>
                    <tr><th>Job Role Applied</th><td>${jobRole}</td></tr>
                </table>
            </div>

            <div class="feedback-section">
                <h3><i class="fas fa-chart-bar"></i> Interview Feedback</h3>
                <table class="feedback-table">
                    <tr><th>Technical Strengths</th><td>${data.technical_strengths}</td></tr>
                    <tr><th>Weaknesses</th><td>${data.weaknesses}</td></tr>
                    <tr><th>Communication</th><td>${data.communication}</td></tr>
                    <tr><th>Recommendation</th><td>${data.recommendation}</td></tr>
                    <tr><th>Final Decision</th><td><strong>${data.decision}</strong></td></tr>
                </table>
            </div>
        `;

        document.getElementById("feedback").innerHTML = feedbackHTML;
        showCard('feedback-card');

    } catch (error) {
        console.error('Error:', error);
        showNotification("Error processing interview. Please check your API key and try again.", "error");
    } finally {
        finishBtn.disabled = false;
        finishBtn.innerHTML = '<i class="fas fa-check"></i> Finish Interview';
    }
});

document.getElementById("reset").addEventListener("click", () => {
    // Clear all inputs
    document.getElementById("name").value = "";
    document.getElementById("qualification").value = "";
    document.getElementById("skills").value = "";
    document.getElementById("q1").value = "";
    document.getElementById("q2").value = "";
    document.getElementById("q3").value = "";

    // Show first card
    showCard('personal-card');
});

// Initialize the app
document.addEventListener('DOMContentLoaded', () => {
    showCard('personal-card');
});
