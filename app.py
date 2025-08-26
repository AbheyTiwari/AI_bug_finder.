from flask import Flask, render_template, request, redirect, url_for, jsonify
import asyncio
import os
from bugfiner_runner import parse_args, main as bugfiner_main, REPORT_DIR

app = Flask(__name__)

# Ensure report directory exists
os.makedirs(REPORT_DIR, exist_ok=True)

# Simple in-memory logs for live display
live_logs = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        bug_desc = request.form.get("bug_desc")
        test_url = request.form.get("test_url")
        test_name = request.form.get("test_name")
        gemini_key = request.form.get("gemini_key")
        headful = request.form.get("headful") == "on"
        record_video = request.form.get("record_video") != "off"

        args = [
            "--url", test_url,
            "--test-name", test_name,
            "--bug", bug_desc,
        ]
        if headful:
            args.append("--headful")
        if not record_video:
            args.append("--no-video")
        if gemini_key:
            args += ["--gemini-key", gemini_key]

        asyncio.run(run_bugfiner(args))
        return redirect(url_for("index"))

    # Read all reports
    reports = []
    for filename in sorted(os.listdir(REPORT_DIR), reverse=True):
        if filename.endswith(".md"):
            path = os.path.join(REPORT_DIR, filename)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                reports.append({"name": filename, "content": content})
            except:
                reports.append({"name": filename, "content": "Error reading file."})

    return render_template("index.html", reports=reports, logs="\n".join(live_logs))


async def run_bugfiner(args_list):
    import sys
    sys.argv = ["bugfiner_runner.py"] + args_list
    await bugfiner_main()


@app.route("/get-logs")
def get_logs():
    """Return live logs as JSON"""
    return jsonify({"logs": "\n".join(live_logs)})


if __name__ == "__main__":
    app.run(debug=True)
