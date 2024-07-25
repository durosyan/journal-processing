import argparse
import os
import glob
from flask import Flask
from read_journal import read_journal
import json

formatted_entries = []
app = Flask(__name__)

@app.route('/healthcheck')
def healthcheck():
    return "OK"

@app.route('/api/v1/entries/<int:index>')
def get_entry(index):
    if index < 0 or index >= len(entries):
        return "Entry not found", 404
    entry = entries[index]
    return json.dumps(entry)

@app.route('/api/v1/entries')
def get_entries():
    return json.dumps(formatted_entries)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="personal markdown journal")
    parser.add_argument("directory")
    args = parser.parse_args()

    directory = os.path.abspath(args.directory)
    md_files = glob.glob(f"{directory}/**/*.md", recursive=True)

    entries = read_journal(md_files)
    for entry in entries:
        formatted_entry = {
            'date': entry['date'].strftime('%Y-%m-%d'),
            'mood': entry['mood'],
            'title': entry['title']
        }
        formatted_entries.append(formatted_entry)
        
    app.run()