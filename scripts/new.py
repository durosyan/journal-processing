import os
import logging
from datetime import datetime
from jinja2 import Template

logger = logging.getLogger(__name__)

if __name__ == '__main__':
	# logging.basicConfig(filename='new_entry.log', level=logging.INFO)
	# Get the current date and time
	now = datetime.now()
	formatted_date = now.strftime("%H%M%d%m%Y")

	template_file = os.path.join(os.path.dirname(__file__), "templates", "template.md")
	new_file = f"Entry_{formatted_date}.md"

	# Ask for user input
	title = input("Enter the title for the new entry: ")

	# Create a new file based on the template
	try:
		with open(template_file, "r") as f:
			print(f"opened template file: {template_file}")
			template_content = f.read()
			template = Template(template_content)
			properties = { "posted": now.strftime("%H%M %d/%m/%Y"), "title": title }
			rendered_content = template.render(properties)

		with open(new_file, "w") as f:
			print(f"created new file: {new_file}")
			f.write(rendered_content)

		# logger.info(f"created new file: {new_file}")
	except Exception as e:
		logger.info(f"failed to create new file: {new_file}")
