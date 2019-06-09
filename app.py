from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from utils import fetch_reply

app = Flask(__name__)

@app.route("/")
def index():
    str_msg = '<h3>Welcome to Entertainment chatbot.</h3> <h4>For using the chatbot, send <b>Join circle-was</b> to <b>+1 415-523-8886</b> by using your WhatsApp</h4>'
    return str_msg


@app.route('/msg', methods=['POST'])
def sms_reply():
    message = request.form.get('Body')
    sender = request.form.get('From')

    response = MessagingResponse()

    x,y = fetch_reply(message, sender)
    if y!= '':
        urls = y.split('\n')
        print(urls)
        for index in range(0, len(urls)):
            response.message('{}'.format(x)).media(urls[index])
    else:
        response.message(x)
    return str(response)

if __name__ == '__main__':
    app.run(debug=True)

