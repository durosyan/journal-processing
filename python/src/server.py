import os
import glob
from flask import Flask
from journal import read_journal
import json
from dotenv import load_dotenv

load_dotenv()

directory = ""
formatted_entries = []
app = Flask(__name__)

if "JOURNAL_DIR" in os.environ:
    directory = os.environ["JOURNAL_DIR"]
else:
    print("Please set the JOURNAL_DIR environment variable")
    exit(1)

md_files = glob.glob(f"{directory}/**/*.md", recursive=True)
for entry in read_journal(md_files):
    formatted_entry = {
        "date": entry["date"].strftime("%Y-%m-%d"),
        "mood": entry["mood"],
        "title": entry["title"],
    }
    formatted_entries.append(formatted_entry)


@app.route("/healthcheck")
def healthcheck():
    return "OK"


@app.route("/entries/<int:index>")
def get_entry(index):
    if index < 0 or index >= len(formatted_entries):
        return "Entry not found", 404
    entry = formatted_entries[index]
    return json.dumps(entry)


@app.route("/entries")
def get_entries():
    return json.dumps(formatted_entries)


if __name__ == "__main__":
    app.run()
