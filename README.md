# AI_bug_finder.

🐞 AI-Powered Bug Reproduction System
📌 Overview

This project is an AI-powered bug reproduction tool that automatically takes vague or incomplete bug reports and reproduces them into concrete steps a developer can follow.

Instead of guessing what a tester meant, the system:

Reads a bug report.

Generates possible reproduction steps.

Runs those steps in a test environment.

Produces a structured bug reproduction report.

This reduces debugging time and ensures bugs are not "unreproducible."

🚀 Features

AI-driven step inference – Converts vague bug reports into reproducible steps.

Automated environment testing – Runs the inferred steps in a browser-like environment.

Structured output – Generates detailed reports with:

Steps to reproduce

Expected vs actual results

Screenshots / console logs

Buggy demo app – login.html intentionally contains multiple errors for testing.

🛠️ Setup
1. Clone the repo
git clone https://github.com/your-username/bug-reproduction-ai.git
cd bug-reproduction-ai

2. Install dependencies
pip install -r requirements.txt


(Python backend requires selenium, playwright, or similar, depending on your chosen runner.)

3. Run the Buggy Demo App

Open login.html in your browser (double-click or serve via local server).
This app contains deliberate bugs for testing the system.

4. Run the Bug Reproduction Agent
python bug_repro_agent.py --input "Login button does not work"


This will:

Parse the report.

Generate reproduction steps.

Attempt to execute them.

Output a detailed log of findings.

📂 Project Structure
bug-reproduction-ai/
│
├── bug_repro_agent.py      # Main AI-powered reproduction system
├── login.html              # Buggy sample app for testing
├── requirements.txt        # Python dependencies
└── README.md               # Documentation

🧪 Example Run

Bug report input:

"Login page doesn’t respond when I click login."

AI Output:

Steps to Reproduce:
1. Open login.html in Chrome.
2. Enter "testuser" in username field.
3. Enter "1234" in password field.
4. Click "Login".

Expected: User should see success message.
Actual: Console shows ReferenceError (ENVIRONMENT not defined).

📌 Notes

This is a prototype for research & hackathon purposes.

Demo app (login.html) is intentionally buggy for testing AI capabilities.

Extend with real-world bug reports and CI/CD integration.
