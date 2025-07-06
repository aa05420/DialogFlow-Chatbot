# 📦 DialogFlow Shipment Tracker Chatbot (Flask API)

This project is a **DialogFlow-integrated chatbot** that provides **real-time shipment updates** based on an order ID. It uses a **Flask-based webhook** that connects DialogFlow to an external shipment tracking API.

---

## 🚀 Features

- 🔗 Integrates DialogFlow with a custom Flask webhook
- 📬 Responds to user queries about shipment status using external REST API
- 🧠 DialogFlow handles natural language queries like:  
  **"When will my order 12345 ship?"**
- 📅 Parses and formats ISO datetime into human-readable format

---

## 🏗️ How It Works

1. **User** sends a message in DialogFlow:  
   `"What is the status of order 12345?"`

2. **DialogFlow** extracts the `orderId` using its NLU engine and sends it to your `/webhook` endpoint.

3. **Flask server**:
   - Receives the webhook POST request.
   - Extracts `orderId` from DialogFlow's JSON payload.
   - Makes a `POST` request to the external shipment tracking API.
   - Parses the `shipmentDate` and returns a formatted response.

---

## 🧾 Sample DialogFlow Request Payload

```json
{
  "queryResult": {
    "parameters": {
      "orderId": "12345"
    }
  }
}
🧪 Sample Response
json
Copy
Edit
{
  "fulfillment_text": "The shipment for order 12345 is scheduled for 07-15-2025 13:45:00 UTC."
}
📁 File Overview
app.py – Flask server with:

/ route: basic "Hello, World!" check

/webhook route: main DialogFlow fulfillment logic

Uses requests and datetime for API communication and time formatting

🧰 Setup Instructions
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/aa05420/DialogFlow-Chatbot.git
cd DialogFlow-Chatbot
2. Create a virtual environment (recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install Flask requests
4. Run the Flask app
bash
Copy
Edit
python app.py
The app will start on http://localhost:5000.

📌 Tip: Use ngrok to expose your local server for DialogFlow webhook testing:

bash
Copy
Edit
ngrok http 5000
🌐 External Shipment API
This app makes a POST request to:

bash
Copy
Edit
https://orderstatusapi-dot-organization-project-311520.uc.r.appspot.com/api/getOrderStatus
With payload:

json
Copy
Edit
{ "orderId": "12345" }
Expected response:

json
Copy
Edit
{
  "shipmentDate": "2025-07-15T13:45:00.000Z"
}
🛡️ Error Handling
If the external API fails or returns unexpected data, the bot replies:

"Sorry, an error occurred while processing your request."

📌 Notes
Make sure the orderId entity is set up correctly in your DialogFlow agent.

Ensure the external API is accessible and returns shipmentDate in expected ISO format.

Date is converted from UTC ISO to MM-DD-YYYY HH:MM:SS.

