import requests
import json

#webhook_url = 'your beeceptor url'

webhook_url_to_send = 'your local server\port accessed via ngrok secure tunnel'

devices = {'devices' : {'data': {'id1' : 1234567890, 'id2': 1324223}}}

r = requests.post(webhook_url_to_send, data=json.dumps(devices), headers={'Content-Type': 'application/json'})

