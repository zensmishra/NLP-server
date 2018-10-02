import requests
import json

url = "http://localhost:5000/nlp/"

def post_message_to_nlpserver(message):
    payload = {"message" : message }
    headers = {
        'Content-Type': "application/json",
        'Cache-Control': "no-cache"
        }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    return json.loads(response.text)