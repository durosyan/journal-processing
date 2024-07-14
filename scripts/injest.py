'''
will injest an existing directory into a json file.
finds all files in a directory with the correct text header as follows:

---
title: ""
posted: "HHMM dd/mm/yyyy
mood: xx
---

then parses said text header into a json blob file output
'''

import argparse
import json
import re
import os
import markdown

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="personal markdown journal")
    parser.add_argument("directory")
    parser.add_argument("index")
    args = parser.parse_args()

    directory = os.path.abspath(args.directory)
    index = os.path.abspath(args.index)

    entries = []

    if os.path.exists(index):
        with open(index, 'r') as index_file:
            entries = json.load(index_file)

    for root, dirs, files in os.walk(directory):
        for name in files:
            if name.endswith(".md"):
                file_path = os.path.join(root, name)
                with open(file_path, "r") as file:
                    file_content = file.read()
                    md = markdown.Markdown(extensions=['meta'])
                    md.convert(file_content)
                    print(md.Meta)

    # print(entries)
    # for entry in entries:
    #     print(entry['file'])

    # # Write the extracted data to the JSON index file
    # with open(index, 'w') as index_file:
    #     json.dump(entries, index_file, indent=4)

    print(f"Processed {len(entries)} files. Data saved to {index}")
