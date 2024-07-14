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

def extract_header_info(file_content):
	# Regular expression to match the header format
	header_pattern = r"---\s*\n(.*?)\s*\n---"
	match = re.search(header_pattern, file_content, re.DOTALL)
	if match:
		header_text = match.group(1)
		# Extract specific fields (title, posted, mood)
		header_lines = header_text.splitlines()
		header_info = {}
		for line in header_lines:
			print(line)
			key, value = line.split(":", 1)
			header_info[key.strip()] = value.strip()
		return header_info
	return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sample argument parser")
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
                    header_info = extract_header_info(file_content)
                    if header_info:
                    	print(header_info)
                        # entries.append(header_info)

    # # Write the extracted data to the JSON index file
    # with open(index, 'w') as index_file:
    #     json.dump(entries, index_file, indent=4)

    print(f"Processed {len(entries)} files. Data saved to {index}")
