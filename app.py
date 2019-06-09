from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from utils import fetch_reply

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")


@app.route('/sms', methods=['POST'])
def sms_reply():
    message = request.form.get('Body')
    sender = request.form.get('From')

    response = MessagingResponse()

    x,y = fetch_reply(message, sender)
    urls = y.split('\n')
    print(urls)
    for index in range(0, len(urls)):
        response.message('{}'.format(x)).media(urls[index])
    #print(str(response))
    return str(response)

if __name__ == '__main__':
    app.run(debug=True)

