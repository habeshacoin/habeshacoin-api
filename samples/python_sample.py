import requests

url = "https://check.habeshacoin.com/track_transaction"
headers = {
    "X-API-KEY": "your_api_key_here"
}
data = {
    "bank_name": "CBE",
    "account_number": "10001234567",
    "transaction_id": "FT24351VL4NX",
    "reference": "unique_reference",
    "callback": "https://yourdomain.com/webhook",
    "chat_id": "123456789"
}

try:
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print("API Response:", response.json())
    else:
        print("Error:", response.text)
except Exception as e:
    print("An error occurred:", str(e))
