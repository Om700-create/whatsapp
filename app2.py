import os
from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()

app = Flask(__name__)


tickets = {}

@app.route('/webhook', methods=['POST'])
def webhook():
    
    incoming_msg = request.values.get('Body', '').lower().strip()
    from_number = request.values.get('From', '')
    num_media = int(request.values.get('NumMedia', 0))
    
    resp = MessagingResponse()
    
    
    if "raise a ticket" in incoming_msg:
       
        msg = resp.message("Thank you for your inquiry! Please choose an option:\n\n1. Previous Ticket\n2. New Ticket")
    elif incoming_msg in ['1', '2']:
        
        tickets[from_number] = {
            'type': 'previous' if incoming_msg == '1' else 'new',
            'status': 'awaiting_imei',
            'created_at': datetime.now().isoformat()
        }
        msg = resp.message("Please upload an image of the IMEI and describe your problem.")
    elif num_media > 0 and from_number in tickets and tickets[from_number]['status'] == 'awaiting_imei':
       
        media_url = request.values.get('MediaUrl0')
        tickets[from_number].update({
            'imei_image': media_url,
            'description': incoming_msg if incoming_msg else "No description provided",
            'status': 'completed'
        })
        msg = resp.message("Thank you for your inquiry! Our team will contact you soon.\n\nTicket Reference: #" + from_number[-6:])
    else:
        
        msg = resp.message("Sorry, I didn't understand that. Please reply with 'raise a ticket' to start.")
    
    return Response(str(resp), mimetype='text/xml')

@app.route('/status', methods=['GET'])
def status():
   
    return {'status': 'active', 'time': datetime.now().isoformat()}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)