from flask import Flask, request, abort
import requests
from discord import Webhook, RequestsWebhookAdapter

app = Flask(__name__)

@app.route('/webhook_receiver', methods=['POST'])
def webhook_receiver():
    discorder_url_to_forward = 'your discord web hook url'
    if request.method == 'POST':
        print(request.json)
        #r = requests.post(discorder_url_to_forward, data=request.json)
        webhook = Webhook.from_url(discorder_url_to_forward, adapter=RequestsWebhookAdapter())
        webhook.send(request.json)
        return 'success', 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run()

