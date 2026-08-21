# ChatBot - AI Assistant Application

A simple, professional, and beginner-friendly web-based chatbot built with Python Flask. This chatbot provides a modern interface for interactive conversations with intelligent response handling.

## Features

✨ **Core Features:**
- 🤖 AI-style chatbot with intelligent response detection
- 💬 Real-time message sending and receiving
- 📱 Responsive design (works on desktop and mobile)
- 🎨 Modern, clean interface with smooth animations
- ⏰ Timestamps for all messages
- 💾 Conversation memory during the current session
- 🔄 Clear chat history with confirmation
- ⌨️ Send messages with Enter key or button click
- 💡 Typing indicator while bot is responding
- 🛡️ Error handling (application won't crash from user input)

✅ **Chatbot Capabilities:**
- Greeting detection (hello, hi, hey, good morning, etc.)
- Personalized responses about the bot itself
- Common questions handling:
  - What is your name?
  - Who are you?
  - How are you?
  - What can you do?
- Help command with detailed instructions
- Unknown question handling with polite responses
- Natural, varied responses (uses randomized response templates)

## Technologies Used

- **Backend:** Python 3.13 + Flask
- **Frontend:** HTML5 + CSS3 + JavaScript
- **No API keys required** for the basic version

## Project Structure

```
chatbot/
│
├── venv/                    # Python virtual environment
│
├── app.py                   # Flask backend application
├── chatbot.py               # Chatbot engine and logic
├── requirements.txt         # Python dependencies
├── README.md                # This file
├── .gitignore               # Git ignore rules
│
├── templates/
│   └── index.html           # HTML frontend
│
└── static/
    ├── style.css            # Styling
    └── script.js            # Frontend JavaScript
```

## Installation

### Prerequisites
- Windows, Mac, or Linux
- Python 3.13+
- pip (Python package manager)

### Step 1: Navigate to Your Project Directory

Open Command Prompt or PowerShell and navigate to your chatbot folder:

```bash
cd path\to\chatbot
```

### Step 2: Activate Virtual Environment

**Windows (Command Prompt):**
```bash
venv\Scripts\activate
```

**Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

You should see `(venv)` at the beginning of your terminal prompt.

### Step 3: Install Dependencies

With the virtual environment activated, install the required packages:

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- Werkzeug (Flask dependency)

## How to Run

1. **Activate the virtual environment** (if not already activated)
2. **Run the Flask application:**

```bash
python app.py
```

You should see output like:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

3. **Open your browser** and go to:
   ```
   http://127.0.0.1:5000
   ```

4. **Start chatting!** Type your message and press Enter or click Send.

5. **Stop the server:** Press `Ctrl + C` in your terminal

## Usage Examples

Here are some messages you can try:

| Input | Bot Response |
|-------|---|
| `hello` | Greeting response |
| `hi` | Greeting response |
| `good morning` | Morning greeting |
| `what is your name?` | Introduces itself as ChatBot |
| `who are you?` | Describes what it is |
| `how are you?` | Responds positively |
| `what can you do?` | Lists capabilities |
| `help` | Shows help information |
| `random message` | Polite unknown response |

## Project Files Explained

### Backend Files

**`chatbot.py`** - The chatbot engine
- Contains the `ChatBot` class with response logic
- Detects user intents (greeting, questions, etc.)
- Stores conversation history
- Generates appropriate responses

**`app.py`** - Flask web server
- Handles HTTP requests from the frontend
- Provides the `/chat` endpoint for messages
- Provides the `/clear` endpoint to clear chat
- Serves the HTML, CSS, and JavaScript files

### Frontend Files

**`templates/index.html`** - The chatbot interface
- HTML structure for the chat window
- Message display area
- Input field and send button
- Clear button and styling hooks

**`static/style.css`** - Styling and design
- Modern gradient color scheme
- Responsive layout
- Message bubble styles
- Animations and transitions
- Mobile-friendly design

**`static/script.js`** - Frontend interactivity
- Handles button clicks and keyboard input
- Sends messages to Flask backend
- Displays messages in the chat window
- Shows/hides typing indicator
- Manages chat clearing

## How the Application Works

1. **User opens the browser** → Loads the chatbot interface
2. **User types a message** → JavaScript captures it
3. **Message is sent to Flask** → via POST request to `/chat` endpoint
4. **Flask passes message to ChatBot** → The chatbot engine processes it
5. **ChatBot generates response** → Based on intent detection
6. **Response sent back to browser** → as JSON
7. **JavaScript displays the response** → in the chat window
8. **Conversation continues** → User can type more messages

## Troubleshooting

### "Port 5000 already in use"
Another application is using port 5000. You can:
- Close other applications using port 5000
- Or modify `app.py` to use a different port (change `port=5000` to `port=5001`, etc.)

### "ModuleNotFoundError: No module named 'flask'"
The dependencies are not installed. Make sure:
- Virtual environment is activated (you should see `(venv)` in your terminal)
- Run `pip install -r requirements.txt`

### Chatbot not responding
- Check that Flask is running (you should see the "Running on..." message)
- Check browser console (F12) for JavaScript errors
- Check terminal for Flask errors

### Virtual environment not activating
- **Windows:** Try using `venv\Scripts\activate.bat` or PowerShell with `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

## Future Improvements

Here are features you can add later:

- 🔊 Text-to-speech responses
- 🎤 Voice input recognition
- 💾 Save chat history to file
- 🌐 Integration with real APIs (weather, news, etc.)
- 🔐 User authentication and personalization
- 📊 Chat analytics and statistics
- 🎯 More advanced NLP and intent detection
- 🌍 Multiple language support
- 💬 Support for multiple concurrent conversations

## License

This project is open source and free to use.

## Getting Help

If you encounter any issues:

1. Check the troubleshooting section above
2. Read the error message carefully
3. Check the browser console (F12 in most browsers)
4. Check the terminal for Flask error messages

## Enjoy Your ChatBot! 🎉

This is a great portfolio project to showcase your Python and web development skills. You can:
- Share the code on GitHub
- Describe it in your resume
- Present it in job interviews
- Use it as a foundation for more advanced chatbots

Happy coding!
