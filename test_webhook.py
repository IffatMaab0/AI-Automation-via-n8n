import requests

user_msg = "tell me a joke"
req_msg = {"message": user_msg }


# localhost (my PC)
#    ↓
# n8n runs here
#    ↓
# ngrok tunnels it
#    ↓
# public URL (internet access)


url = "https://squeegee-repulsion-browsing.ngrok-free.dev/webhook-test/75d82094-071a-42cb-bcf0-97a76871ab2a"


response = requests.post(url, json =req_msg)

print(response.status_code)
print(response.json()[0]["output"])