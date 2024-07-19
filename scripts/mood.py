import argparse
import os
import markdown
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import glob

def calculate_average_mood(entries):
    total_mood = sum(entry['mood'] for entry in entries)
    average_mood = total_mood / len(entries)
    return average_mood

def custom_date_parser(date_string):
    # Custom, faster date parsing can be implemented if applicable
    return datetime.strptime(date_string.replace('"', '').replace('/', ''), '%H%M %d%m%Y')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="personal markdown journal")
    parser.add_argument("directory")
    args = parser.parse_args()

    directory = os.path.abspath(args.directory)
    md_files = glob.glob(f"{directory}/**/*.md", recursive=True)

    entries = []
    
    for file_path in md_files:
        with open(file_path, "r") as file:
            file_content = file.read()
            md = markdown.Markdown(extensions=['meta'])
            md.convert(file_content)
            if 'posted' in md.Meta and 'mood' in md.Meta:
                mood = int(md.Meta['mood'][0])
                date_obj = custom_date_parser(md.Meta['posted'][0])
                entries.append({'date': date_obj, 'mood': mood})
                print(os.path.basename(file.name))


    entries.sort(key=lambda entry: entry['date'])
    average_mood = calculate_average_mood(entries)
    print(f"Average mood: {average_mood}")

    DF = pd.DataFrame(entries)
    plt.scatter(DF['date'], DF['mood'])
    plt.gcf().autofmt_xdate()
    plt.show()