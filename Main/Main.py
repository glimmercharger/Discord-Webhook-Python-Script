import requests
import json

webhook_url = "Your-Discord-Webhook-url"

# The message you want to send
message_content = "You got this Cool project from @glimmercharger on GitHub!"

# The data to be sent in the POST request
# 'content' is the key for a basic message. 
# Please leave this thats how the project works!
data = {
    "content": message_content
}

# The headers to specify the content type
headers = {
    "Content-Type": "application/json"
}

# Send the POST request
response = requests.post(webhook_url, data=json.dumps(data), headers=headers)

# Check if the request was successful
if response.status_code == 204:
    print("Message sent successfully!")
else:
    print(f"Failed to send message. Status code: {response.status_code}")
    print(response.text)
