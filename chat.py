from ollama import Client
import json
import time
import os

def request(file_content):
  client = Client(host='http://192.168.0.39:11434')
  try:
    response = client.chat(model='gemma2', messages=[
      {
        'role': 'user',
        'content': f'Do not format as markdown. You are only to respond in JSON format containing the keys: mood, summary, date. mood must be entirely lowercase. date must be in the format dd-mm-yyyy. What is the mood, summary and date of this text: {file_content[:500]}'
      },
    ])

    return json.loads(response["message"]["content"])
  except Exception as e:
    print(e)
    return None



if __name__ == "__main__":
  entries = []

  for root, dirs, files in os.walk("./entries"):
    for name in files:
        if name.endswith((".md")):
            file_path = os.path.join(root, name)
            with open(file_path, "r") as file:
                file_content = file.read()

                content = request(file_content)
                if content == None:
                  time.sleep(5)
                  content = request(file_content)
                  if content == None:
                    continue

                print(f'{ file_path }: { content["mood"] }')
                output_dict = {
                  "mood": content["mood"],
                  "date": content["date"],
                  "summary": content["summary"],
                  "file": file_path
                }

                entries.append(output_dict)

  with open('./output.json', 'w') as output:
    json.dump(entries, output, indent=4)