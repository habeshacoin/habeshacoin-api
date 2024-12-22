const express = require('express');
const app = express();
app.use(express.json());

app.post('/webhook', (req, res) => {
    console.log('Webhook received:', req.body);

    // Add custom logic to process the webhook data here
    const transactionID = req.body['transaction ID'];
    console.log(`Transaction ID: ${transactionID}`);

    res.status(200).send('Webhook received successfully!');
});

app.listen(3000, () => {
    console.log('Webhook listener running on port 3000');
});
