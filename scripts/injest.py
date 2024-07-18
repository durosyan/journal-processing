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
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="personal markdown journal")
    parser.add_argument("directory")
    parser.add_argument("index")
    args = parser.parse_args()

    directory = os.path.abspath(args.directory)
    index = os.path.abspath(args.index)

    entries = []
    entry_dates = []
    moods = []

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
                    keys = md.Meta.keys()
                    if 'posted' in keys and 'mood' in keys:
                        mood = int(md.Meta['mood'][0])
                        date_string = md.Meta['posted'][0].replace('"', '').replace('/', '')
                        date_obj = datetime.strptime(date_string, '%H%M %d%m%Y')
                        moods.append(mood)
                        entry_dates.append(date_obj)
                        print(os.path.basename(file.name))

                        
    # # Write the extracted data to the JSON index file
    # with open(index, 'w') as index_file:
    #     json.dump(entries, index_file, indent=4)
    date_time = pd.to_datetime(entry_dates)
    DF = pd.DataFrame()
    DF['value'] = moods
    DF = DF.set_index(date_time)
    plt.plot(DF)
    plt.gcf().autofmt_xdate()
    plt.show()



    print(f"Processed {len(entries)} files. Data saved to {index}")
