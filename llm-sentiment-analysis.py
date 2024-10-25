#! pip install openai
import json
from openai import OpenAI
client = OpenAI(api_key=APIKEY)

bill_title = "Coup d'Etat au Honduras"

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Make a sentiment analysis on the below text. Ensure to respond in a JSON format with 2 fields: 'score' (score between 0 and 1) and 'explanation'. \n {}".format(bill_title)
        }
    ]
)

print(completion.choices[0].message)
json.loads(completion.choices[0].message.content[8:-4])
