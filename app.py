from flask import Flask, request, jsonify
from twilio.rest import Client
from dotenv import load_dotenv
import os


load_dotenv()


ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
FROM_WHATSAPP = os.getenv('FROM_WHATSAPP')


app = Flask(__name__)

client = Client(ACCOUNT_SID, AUTH_TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    
    incoming_message = request.values.get('Body', '').lower()
    from_number = request.values.get('From', '')

  
    if "raise a ticket" in incoming_message:
        response = "Thank you for your inquiry! Please choose an option:\n1. Previous Ticket\n2. New Ticket"
    elif "1" in incoming_message:
        response = "Please provide the IMEI image and describe the problem for your previous ticket."
    elif "2" in incoming_message:
        response = "Please provide the IMEI image and describe your problem for the new ticket."
    else:
        response = "Sorry, I didn't understand that. Please reply with 'raise a ticket'."


    message = client.messages.create(
        body=response,
        from_=FROM_WHATSAPP,
        to=from_number
    )
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(debug=True)