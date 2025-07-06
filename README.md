# 📦 DialogFlow Shipment Tracker Chatbot (Flask API)

This is a DialogFlow-integrated chatbot that provides real-time shipment updates based on an order ID. It uses a Flask-based webhook to connect with an external API and return shipment information in a user-friendly format.

## 🚀 Features

- Connects DialogFlow to a Flask backend
- Handles natural language queries for shipment tracking
- Sends order ID to an external API and retrieves shipment date
- Formats ISO date into readable output
- Includes basic error handling for failed API calls

## 📁 What's in this Project

DialogFlow-Chatbot/
│
├── app.py # Main Flask server with webhook logic
├── requirements.txt # Python dependencies (Flask, requests)
└── README.md # Project documentation

`app.py` contains:
  - `/` route to test the server
  - `/webhook` route to handle POST requests from DialogFlow
  - Logic to send `orderId` to an external API and return shipment status

- External API used:
https://orderstatusapi-dot-organization-project-311520.uc.r.appspot.com/api/getOrderStatus

csharp
Copy
Edit

## 🧪 Example

**User says:**  
"What is the status of order 12345?"

**Bot replies:**  
"The shipment for order 12345 is scheduled for 07-15-2025 13:45:00 UTC."

## 🛡️ Error Handling

If something goes wrong, the bot responds with:  
"Sorry, an error occurred while processing your request."

