# HabeshaCoin Transaction Tracking API

This repository provides documentation and sample code for integrating with the HabeshaCoin Transaction Tracking API. 

The API enables businesses to track transactions using bank names, account numbers, transaction IDs, or images of payment receipts. Customers receive real-time responses and webhook notifications for seamless tracking.

---

## API Overview

### Base URL
`https://check.habeshacoin.com/track_transaction`

### Authentication
Every request must include the `X-API-KEY` header. To obtain your API key, contact us via:
- **Telegram Support:** [@habeshacoin_support](https://t.me/habeshacoin_support)
- **Email:** info@habeshacoin.com

### Required Form Data Fields
| Field           | Type    | Description                                                                 |
|-----------------|---------|-----------------------------------------------------------------------------|
| `bank_name`     | string  | Must be one of: `CBE`, `TELEBIRR`, `BOA`, `EBIRR`.                          |
| `account_number`| string  | Mandatory for `CBE` and `BOA`.                                              |
| `image`         | file    | Image of the transaction receipt (optional if `image_url` or `transaction_id` is provided). |
| `image_url`     | string  | URL of the transaction receipt image (optional if `image` or `transaction_id` is provided). |
| `transaction_id`| string  | Unique transaction identifier (optional if `image` or `image_url` is provided). |
| `reference`     | string  | Unique reference number sent in the request and returned in the response.   |
| `callback`      | string  | Customer's callback URL for webhook notifications.                          |
| `chat_id`       | string  | Telegram chat ID, returned as-is in the response for tracking purposes.      |

---

## Response Format
### Success Response
```json
{
    "data": {
        "Credited account name": "YOHANNES DAMTEW",
        "Credited account number": 10001234567,
        "Payer Name": "YOHANNES DAMTEW",
        "Payment Date": "01-01-2025 00:00:00",
        "amount": 4000.0,
        "chat_id": "123456789",
        "checked_url": "https://abyssiniabank.com/FT24351VL4NX",
        "customer": {
            "credits": 100,
            "name": "Habesha Coin"
        },
        "reference": "e1e20355-ce1f-4acb-b339-f01ee1027e01",
        "transaction ID": "FT24351VL4NX"
    },
    "message": "Transaction tracking is in progress",
    "status": "in progress"
}
```

### Webhook Payload
```php
array (
  'transaction ID' => 'FT24351VL4NX',
  'Payer Name' => 'YOHANNES DAMTEW',
  'amount' => 4000.0,
  'Credited account name' => 'YOHANNES DAMTEW',
  'Credited account number' => '10001234567',
  'Payment Date' => '01-01-2025 00:00:00',
  'chat_id' => '123456789',
  'reference' => 'e1e20355-ce1f-4acb-b339-f01ee1027e01',
  'checked_url' => 'https://abyssiniabank.com/FT24351VL4NX',
  'customer' => 
  array (
    'name' => 'Habesha Coin',
    'credits' => 100,
  ),
)
```

---

## Usage

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/habeshacoin/habeshacoin-api.git
   cd habeshacoin-api
   ```

### Sample Code

#### Python Example
```python
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
response = requests.post(url, headers=headers, data=data)
print(response.json())
```

### Webhook Listener Example (Node.js)
```javascript
const express = require('express');
const app = express();
app.use(express.json());

app.post('/webhook', (req, res) => {
    console.log('Webhook received:', req.body);
    res.sendStatus(200);
});

app.listen(3000, () => {
    console.log('Webhook listener running on port 3000');
});
```

---

## Credits and Billing
To use the API, customers need credits. Each successful response deducts credits. To top up your balance, contact us:
- **Telegram Support:** [@habeshacoin_support](https://t.me/habeshacoin_support)
- **Email:** info@habeshacoin.com

---

## License
[MIT](LICENSE)

---

## Support
For any issues, please create an issue in this repository or reach out via our support channels.
