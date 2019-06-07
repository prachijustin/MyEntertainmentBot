from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from utils import fetch_reply

app = Flask(__name__)




@app.route('/', methods=['POST'])
def sms_reply():
    message = request.form.get('Body')
    sender = request.form.get('From')

    response = MessagingResponse()

    response.message(fetch_reply(message, sender))

    return str(response)

if __name__ == '__main__':
    app.run(debug=True)

