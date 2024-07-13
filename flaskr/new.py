import os
import logging
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

logger = logging.getLogger(__name__)

def main():
    mylib.do_something()
    logger.info('Finished')

if __name__ == '__main__':
	logging.basicConfig(filename='new_entry.log', level=logging.INFO)

	# Get the current date and time
	now = datetime.now()
	formatted_date = now.strftime("%H%M%d%m%Y")

	template_file = "./templates/template.md"
	new_file = f"Entry_{formatted_date}.md"

	# Create a new file based on the template
	try:
		os.system(f"cp {template_file} {new_file}")
		logger.info(f"created new file: {new_file}")

		# Update the 'posted' field in the new file
		with open(new_file, "r+") as f:
		    lines = f.readlines()
		    for i, line in enumerate(lines):
		        if "posted:" in line:
		            lines[i] = f'posted: "{now.strftime("%H%M %d/%m/%Y")}"\n'
		            break
		    f.seek(0)
		    f.writelines(lines)
	except Exception as e:
		logger.info(f"failed to create new file: {new_file}")

