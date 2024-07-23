import argparse
import os
import markdown
from datetime import datetime, timedelta
import glob

def calculate_average_mood(entries):
    """
    Calculate the average mood from a list of journal entries.

    Args:
        entries (list): List of dictionaries representing journal entries.
            Each dictionary should have a 'date' key with a datetime object
            and a 'mood' key with an integer representing the mood.

    Returns:
        float: The average mood calculated from the list of entries.
    """
    total_mood = sum(entry['mood'] for entry in entries)
    average_mood = total_mood / len(entries)
    return average_mood

def custom_date_parser(date_string):
    """
    Custom date parser to convert a string to a datetime object.

    Args:
        date_string (str): The date string to be parsed.

    Returns:
        datetime: The parsed datetime object.
    """
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
            if ('posted' in md.Meta or 'date' in md.Meta) and 'mood' in md.Meta and 'title' in md.Meta:
                mood = int(md.Meta['mood'][0])
                title = md.Meta['title'][0].replace('"', '')
                date_obj = None
                if 'posted' in md.Meta:
                    date_obj = custom_date_parser(md.Meta['posted'][0])
                else:
                    date_obj = custom_date_parser(md.Meta['date'][0])
                entries.append({'date': date_obj, 'mood': mood, 'title': title})

    entries.sort(key=lambda entry: entry['date'])
    average_mood = calculate_average_mood(entries)
    print(f"Total number of entries: {len(entries)}")
    print(f"Total average mood: {average_mood}")

    three_weeks_ago = datetime.now() - timedelta(weeks=1)
    recent_entries = [entry for entry in entries if entry['date'] >= three_weeks_ago]
    average_mood_recent = calculate_average_mood(recent_entries)
    print(f"Average mood for the last week: {average_mood_recent}")
    print(f"Number of entries in the last week: {len(recent_entries)}")