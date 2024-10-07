from openai import OpenAI
import os
import pprint
import json
import dotenv

# Load environment variables
dotenv.load_dotenv()

# Set OpenAI API credentials
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),  
)
deployment_name = os.getenv("DEPLOYMENT_NAME")

prompt = """
Your task is to look at the picture and detailed describe position of circled numbers on each row.

The table is organized into several columns and rows, likely used for recording data or scores. Here’s a breakdown based on the visible parts:

- **Column Headings**: The first column on the left is list numbers in sequential order (1 through 34), which denote numbers of targets. The next two columns are labeled "1. sip" and "2. sip," indicating two different measurements.

- **Cell Entries**: Each row contains numbers, which range from 0 to 11. Some cells are circled, indicating that those values have particular importance and that they were selected for emphasis.

- **Row Format**: Each row represents a one target,  corresponding to scores across the two trials indicated by the columns.

- **Total Row**: At the bottom, there's a row that appears to summarize or total data, with a label “Body/Total” and a figure that resembles a cumulative count or score. Ignore this block.

The table is designed to collect and analyze score across two iterations with a focus on numerical scores.

Please provide a detailed description of the circled numbers in each row, including their position and the values they represent.
"""

urls = [
    "https://github.com/klofac/pokusy/blob/main/vyplnena_bodovacka.jpg?raw=true",
]

outputs = []

for url in urls:
  response = client.chat.completions.create(
    model=deployment_name,
    messages=[
      {
        "role": "user",
        "content": [
          {"type": "text", "text": prompt},
          {
            "type": "image_url",
            "image_url": {
              "url": url,
            },
          },
        ],
      }
    ],
    max_tokens=4000,
  )

  print(response.choices[0].message.content)


