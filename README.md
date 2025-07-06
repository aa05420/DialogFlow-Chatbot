
DialogFLow
This is a web-integrated chatbot built using Google DialogFlow, designed to provide conversational interactions through a simple front-end UI. The project demonstrates how to integrate DialogFlow’s natural language understanding with a web interface using JavaScript, Node.js, and Express.js.

💡 Features
✅ Google DialogFlow integration

💬 Web-based user interface for chatbot interaction

🌐 Uses Express.js as backend server

🔐 Includes environment configuration for secure API key management

🔄 Real-time communication via HTTP

📁 Project Structure
bash
Copy
Edit
DialogFlow-Chatbot/
│
├── public/               # Frontend files (HTML, CSS, JS)
│   └── index.html        # Chat UI
│   └── script.js         # AJAX for sending user input to server
│
├── server.js             # Node.js backend server
├── package.json          # Node project dependencies
├── .env                  # Environment variables (DialogFlow credentials)
└── README.md             # Project documentation
⚙️ Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/aa05420/DialogFlow-Chatbot.git
cd DialogFlow-Chatbot
2. Install Dependencies
bash
Copy
Edit
npm install
3. Setup DialogFlow Credentials
Create a Google Cloud project with DialogFlow API enabled.

Generate a service account key (JSON) from Google Cloud Console.

Save it in the root directory and name it dialogflow-key.json (or update the path in code).

Create a .env file:

ini
Copy
Edit
GOOGLE_APPLICATION_CREDENTIALS=dialogflow-key.json
PROJECT_ID=your-dialogflow-project-id
4. Run the Server
bash
Copy
Edit
node server.js
Then open http://localhost:3000 in your browser.

🛠️ Technologies Used
DialogFlow (ES)

Node.js

Express.js

HTML / CSS / JavaScript

dotenv


🧠 Future Improvements
Add speech-to-text input

Improve UI/UX with chat history and avatars


