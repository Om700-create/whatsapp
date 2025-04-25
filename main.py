from twilio.rest import Client
from datetime import datetime, timedelta
import time

account_sid=""
auth_token=""

client= Client(account_sid, auth_token)

def sent_whatsapp_message(recipient_number, message_body):
    try:
        message= client.messages.client(
            from_="whatsapp:",
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print('Message sent sucessfully! Message SID{message.sid}')
    except Exception as e:
        print("An error occurred")

    

name= input("Enter the recipient_name= ")
recipient_number =input("Enter the recipient whatsapp number with country code: ")
message_body= input(f'enter the message you want to sent to{name}: ')

date_str=input("Enter the date to send the message(yyyy-mm-dd): ")
time_str= input("Enter the time to sent the message(HH:MM 24 hr format): ")

schedule_datetime=datetime.strptime(f'{date_str} {time_str}'"%Y-%m-%d %H:%M")
current_datetime=datetime.now()

time_difference= schedule_datetime - current_datetime
delay_seconds= time_difference.total_seconds()

if delay_seconds <= 0:
    print("The specified time is in past: please enter a future date and time: ")
else:
    print(f'Message schudule to be sent  to {name} at {schedule_datetime}')

    time.sleep(delay_seconds)

    sent_whatsapp_message(recipient_number, message_body)


