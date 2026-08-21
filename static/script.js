// ========================================================================
// ChatBot Frontend - JavaScript
// ========================================================================

// Get DOM elements
const userInput = document.getElementById('userInput');
const sendButton = document.getElementById('sendButton');
const clearButton = document.getElementById('clearButton');
const chatMessages = document.getElementById('chatMessages');
const typingIndicator = document.getElementById('typingIndicator');

// ========================================================================
// Functions
// ========================================================================

/**
 * Format the current time for display
 * @returns {string} Formatted time (HH:MM)
 */
function getCurrentTime() {
    const now = new Date();
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    return `${hours}:${minutes}`;
}

/**
 * Scroll chat messages to the bottom
 */
function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

/**
 * Display a message in the chat window
 * @param {string} message - The message text
 * @param {string} type - 'user' or 'bot'
 */
function displayMessage(message, type) {
    const messageElement = document.createElement('div');
    messageElement.className = `message ${type}-message`;

    const avatar = document.createElement('div');
    avatar.className = 'message-avatar';
    avatar.textContent = type === 'user' ? '👤' : '🤖';

    const content = document.createElement('div');
    content.className = 'message-content';
    
    // Handle multi-line responses
    const lines = message.split('\n');
    lines.forEach(line => {
        const p = document.createElement('p');
        p.textContent = line;
        content.appendChild(p);
    });

    const timeElement = document.createElement('span');
    timeElement.className = 'message-time';
    timeElement.textContent = getCurrentTime();

    messageElement.appendChild(avatar);
    messageElement.appendChild(content);
    messageElement.appendChild(timeElement);

    chatMessages.appendChild(messageElement);
    scrollToBottom();
}

/**
 * Show the typing indicator (bot is thinking)
 */
function showTypingIndicator() {
    typingIndicator.style.display = 'flex';
    scrollToBottom();
}

/**
 * Hide the typing indicator
 */
function hideTypingIndicator() {
    typingIndicator.style.display = 'none';
}

/**
 * Send a message to the backend
 * @param {string} message - The user's message
 */
async function sendMessage(message) {
    try {
        // Disable input while sending
        userInput.disabled = true;
        sendButton.disabled = true;

        // Show typing indicator
        showTypingIndicator();

        // Send request to Flask backend
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        });

        // Parse response
        const data = await response.json();

        // Hide typing indicator
        hideTypingIndicator();

        // Display bot response
        if (data.success) {
            displayMessage(data.response, 'bot');
        } else {
            displayMessage('Sorry, I encountered an error. Please try again.', 'bot');
        }

    } catch (error) {
        console.error('Error:', error);
        hideTypingIndicator();
        displayMessage('Sorry, I could not connect to the server. Please try again.', 'bot');
    } finally {
        // Re-enable input
        userInput.disabled = false;
        sendButton.disabled = false;
        userInput.focus();
    }
}

/**
 * Handle sending a message when the button is clicked
 */
function handleSendButton() {
    const message = userInput.value.trim();

    if (message === '') {
        return; // Don't send empty messages
    }

    // Display user message
    displayMessage(message, 'user');

    // Clear input
    userInput.value = '';

    // Send message to backend
    sendMessage(message);
}

/**
 * Handle clearing the chat
 */
async function handleClearChat() {
    // Confirm before clearing
    if (!confirm('Are you sure you want to clear all messages?')) {
        return;
    }

    try {
        // Send clear request to backend
        const response = await fetch('/clear', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        });

        const data = await response.json();

        if (data.success) {
            // Clear all messages from the chat window
            chatMessages.innerHTML = '';

            // Show welcome message
            const welcomeMessage = `Hello! I'm ChatBot. Welcome! 👋

I can chat with you, answer questions about myself, and have a friendly conversation.

Type 'help' to see what I can do, or just say hello!`;
            displayMessage(welcomeMessage, 'bot');
        }

    } catch (error) {
        console.error('Error clearing chat:', error);
        alert('Could not clear chat. Please try again.');
    }

    userInput.focus();
}

// ========================================================================
// Event Listeners
// ========================================================================

// Send button click
sendButton.addEventListener('click', handleSendButton);

// Enter key to send message
userInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        handleSendButton();
    }
});

// Clear button click
clearButton.addEventListener('click', handleClearChat);

// Focus input on page load
window.addEventListener('load', function() {
    userInput.focus();
});

// ========================================================================
// Initialize
// ========================================================================

console.log('ChatBot Interface loaded successfully!');
