# WhatsApp Auto-Messenger with Twilio

A ticket management system automated through WhatsApp using Twilio's API.

## 🚀 What This Project Does

- Automates customer support via WhatsApp
- Creates a ticketing system with:
  - Ticket initiation ("Raise a ticket")
  - Ticket categorization (New/Previous)
  - IMEI image collection
  - Automated acknowledgments
- Built with Python Flask and Twilio WhatsApp API

## 🛠️ What You Just Implemented

1. **Local Setup**:
   - Created a Flask server with conversation logic
   - Configured Twilio WhatsApp sandbox
   - Set up ngrok for local testing

2. **Working Features**:
   - Button-like interaction via text commands
   - Multi-step conversation flow
   - Basic ticket tracking (in memory)

## ⚙️ Production Requirements (For Office Use)

To move from sandbox to production:

### 📋 Prerequisites
1. **Twilio Production WhatsApp Number**:
   - Apply via [Twilio Console](https://www.twilio.com/whatsapp/request)
   - Approval takes 2-3 weeks
   - Cost: $1/month + usage fees

2. **WhatsApp Business Profile**:
   - Required for official business account
   - Verify your business via Facebook Business Manager

3. **Server Hosting**:
   - Recommended: Heroku (Free tier available) or AWS (~$7/month)

### 💰 Estimated Costs

| Component               | Cost               |
|-------------------------|--------------------|
| Twilio WhatsApp Number  | $1/month           |
| Message Fees            | $0.0055/msg sent   |
|                        | $0.0085/msg received|
| Server Hosting (Heroku) | Free - $7/month    |
| ngrok (Optional)        | Free - $8/month    |

Total estimated: $10-$20/month for moderate usage (~1000 messages)

## 🖥️ How to Run

### Development
```bash
# Install dependencies
pip install flask twilio python-dotenv

# Run locally
python app.py

# In another terminal
ngrok http 5000
Production
Set environment variables:

ACCOUNT_SID=your_twilio_sid
AUTH_TOKEN=your_twilio_token
FROM_WHATSAPP=whatsapp:+1234567890
Deploy to Heroku:

bash
heroku create
git push heroku main
🔍 Testing Instructions
Send "Raise a ticket" to your Twilio number

Follow the prompts (1/2 → IMEI image → confirmation)

➡️ Next Steps
Add database persistence (Firebase/SQLite)

Implement admin dashboard

Apply for WhatsApp Business API for official buttons

📄 License
MIT


Key features of this README:
1. Clear separation between development and production requirements
2. Cost breakdown table for easy budgeting
3. Simple copy-paste deployment commands
4. Future roadmap included
5. License information

You can modify any section as needed. The cost estimates are based on Twilio's standard pricing - actual costs may vary based on your message volume.