from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the WhatsApp Auto Messenger!"

@app.route('/send_message', methods=['POST'])
def send_message():
    # Your Twilio logic here
    return "Message Sent!"

if __name__ == "__main__":
    app.run(debug=True)
