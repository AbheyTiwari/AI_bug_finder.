<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BugFiner AI - GitHub README</title>
<style>
    /* === Global Styles === */
    body {
        margin: 0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background: linear-gradient(135deg, #1a1a2e, #162447, #1f4068);
        color: #e0e0e0;
        line-height: 1.6;
    }
    a { color: #88c0d0; text-decoration: none; transition: 0.2s; }
    a:hover { color: #00ffe7; }
    h1, h2, h3 { margin-top: 1rem; }
    h1 { font-size: 3rem; color: #00ffe7; text-align: center; margin-bottom: 2rem; }
    h2 { color: #88c0d0; border-bottom: 1px solid #444; padding-bottom: 0.3rem; margin-bottom: 1rem; }
    h3 { color: #cccccc; margin-bottom: 0.5rem; }
    p { margin-bottom: 1rem; }

    /* === Container === */
    .container {
        max-width: 1000px;
        margin: 2rem auto;
        padding: 1rem 2rem;
        background: rgba(30, 30, 45, 0.85);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.5);
    }

    /* === Lists === */
    ul { padding-left: 1.2rem; }
    li { margin-bottom: 0.5rem; }

    /* === Code / Pre === */
    pre, code {
        background: rgba(0,0,0,0.3);
        padding: 0.5rem 1rem;
        border-radius: 10px;
        font-family: 'Courier New', Courier, monospace;
        overflow-x: auto;
        margin-bottom: 1rem;
    }

    /* === Buttons / Links === */
    .btn {
        display: inline-block;
        padding: 0.6rem 1.2rem;
        margin: 0.5rem 0;
        border-radius: 10px;
        border: 1px solid #444;
        background: #2a2a3d;
        color: #e0e0e0;
        text-decoration: none;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .btn:hover { background: #3a3a5a; border-color: #666; }

    /* === Section spacing === */
    section { margin-bottom: 2rem; }

    /* === Media Queries === */
    @media(max-width: 600px){
        .container { padding: 1rem; }
        h1 { font-size: 2.2rem; }
    }
</style>
</head>
<body>
<div class="container">
    <h1>🛠 BugFiner AI</h1>

    <section>
        <h2>🚀 Features</h2>
        <ul>
            <li>Automated Bug Reproduction: Converts vague bug reports into actionable test steps.</li>
            <li>Headless or Headful Execution: Run browser tests with or without UI.</li>
            <li>Live Logs Streaming: View test execution in real-time.</li>
            <li>Video Recording: Optional recording of the browser session for debugging.</li>
            <li>Markdown Reports: Generates structured, human-readable bug reports.</li>
            <li>Dashboard: Manage and view all tests, logs, and reports in a modern, dark-themed interface.</li>
            <li>AI-Powered Analysis: Uses GPT-style AI to interpret vague bug descriptions into reproducible steps.</li>
        </ul>
    </section>

    <section>
        <h2>🎯 Workflow</h2>
        <ul>
            <li>User Submits Bug Report → BugFiner AI Analyzes Description</li>
            <li>Bug Repro Steps Identified?
                <ul>
                    <li>Yes → Automated Browser Test</li>
                    <li>No → Request More Info</li>
                </ul>
            </li>
            <li>Capture Logs & Screenshots → Generate Markdown Report → Dashboard Displays Report → Developer Reviews & Fixes Bug</li>
        </ul>
    </section>

    <section>
        <h2>⚙️ Installation</h2>
        <pre>
git clone https://github.com/AbheyTiwari/BugFiner.git
cd BugFiner

python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

pip install -r requirements.txt

python app.py
        </pre>
    </section>

    <section>
        <h2>🧩 Usage</h2>
        <ul>
            <li>Enter bug description, test URL, and test name.</li>
            <li>Optionally add Gemini API key for AI analysis.</li>
            <li>Choose whether to run with UI and/or record video.</li>
            <li>Click <strong>Run Test</strong> and watch live logs.</li>
            <li>Access detailed Markdown reports in the dashboard.</li>
        </ul>
    </section>

    <section>
        <h2>📂 File Structure</h2>
        <pre>
BugFiner/
│
├─ app.py
├─ bugfiner_runner.py
├─ static/
│   ├─ style.css
│   └─ script.js
├─ templates/
│   ├─ index.html
│   └─ report.html
├─ bug_reports/
└─ requirements.txt
        </pre>
    </section>

    <section>
        <h2>💡 Future Enhancements</h2>
        <ul>
            <li>Multi-tab/browser testing for complex workflows</li>
            <li>CI/CD integration for automated regression testing</li>
            <li>Plugin system to add custom AI models</li>
            <li>Dashboard analytics for bug trends</li>
        </ul>
    </section>

    <section>
        <h2>📈 Tech Stack</h2>
        <ul>
            <li>Backend: Python, Flask, asyncio</li>
            <li>AI: GPT-style models (Gemini, OpenAI API)</li>
            <li>Frontend: HTML5, CSS3, JS, modern dark UI</li>
            <li>Browser Automation: Playwright / Selenium</li>
            <li>Reporting: Markdown + live logs</li>
        </ul>
    </section>

    <section>
        <h2>🔗 Links</h2>
        <a href="https://github.com/AbheyTiwari/BugFiner" class="btn" target="_blank">GitHub Repository</a>
        <a href="https://github.com/AbheyTiwari/BugFiner/issues" class="btn" target="_blank">Issue Tracker</a>
    </section>

    <section>
        <h2>⚖️ License</h2>
        <p>MIT License © 2025 <a href="https://github.com/AbheyTiwari" target="_blank">Abhey Tiwari</a></p>
    </section>
</div>
</body>
</html>
