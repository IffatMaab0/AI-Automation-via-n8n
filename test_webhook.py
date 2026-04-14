import requests

user_msg = "what's up"
req_msg = {"message": user_msg }

url = "https://squeegee-repulsion-browsing.ngrok-free.dev/webhook-test/75d82094-071a-42cb-bcf0-97a76871ab2a"


response = requests.post(url, json =req_msg)

print(response.status_code)