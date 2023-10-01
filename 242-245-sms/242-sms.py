# Use Twilio API

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "gr43egh4ert5h63nrtyjn56yj6yj5j"
# Your Auth Token from twilio.com/console
auth_token  = "nhurf89e0y78534hg78yu035rguy7890"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+4300000000000", 
    from_="+4300000000000",
    body="Hello from Python!")

print(message.sid)