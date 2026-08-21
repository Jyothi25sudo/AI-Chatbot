# ============================================================================
# Flask ChatBot Application - Backend
# ============================================================================

from flask import Flask, render_template, request, jsonify
from chatbot import chatbot

# Create Flask application
app = Flask(__name__)

# ============================================================================
# Routes
# ============================================================================

@app.route('/')
def home():
    """Render the chatbot home page."""
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    """
    Handle chatbot messages.
    Receives user message and returns bot response.
    """
    try:
        # Check if chatbot initialized successfully
        if chatbot is None:
            return jsonify({
                'error': 'Chatbot not initialized. Please check your .env file and API key.',
                'success': False
            }), 500
        
        # Get data from the JavaScript frontend
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        # Validate message
        if not user_message:
            return jsonify({
                'error': 'Message cannot be empty',
                'success': False
            }), 400
        
        # Get chatbot response
        bot_response = chatbot.get_response(user_message)
        
        # Return response as JSON
        return jsonify({
            'success': True,
            'response': bot_response,
            'user_message': user_message
        }), 200
    
    except Exception as e:
        # Handle errors safely
        return jsonify({
            'error': f'An error occurred: {str(e)}',
            'success': False
        }), 500


@app.route('/clear', methods=['POST'])
def clear_chat():
    """Clear the conversation history."""
    try:
        if chatbot is None:
            return jsonify({
                'error': 'Chatbot not initialized.',
                'success': False
            }), 500
        
        chatbot.clear_history()
        return jsonify({
            'success': True,
            'message': 'Chat history cleared!'
        }), 200
    except Exception as e:
        return jsonify({
            'error': f'Error clearing chat: {str(e)}',
            'success': False
        }), 500


@app.route('/history', methods=['GET'])
def get_history():
    """Get the conversation history (for debugging)."""
    if chatbot is None:
        return jsonify({
            'success': False,
            'history': [],
            'error': 'Chatbot not initialized'
        }), 500
    
    return jsonify({
        'success': True,
        'history': chatbot.get_conversation_history()
    }), 200


# ============================================================================
# Error Handlers
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({
        'error': 'Page not found',
        'success': False
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({
        'error': 'Internal server error',
        'success': False
    }), 500


# ============================================================================
# Main
# ============================================================================

if __name__ == '__main__':
    # Check if chatbot is initialized
    if chatbot is None:
        print("⚠️  WARNING: Chatbot could not be initialized!")
        print("Make sure you have:")
        print("1. Created a .env file in the project folder")
        print("2. Added your Groq API key: GROQ_API_KEY=your_key_here")
        print("3. Installed dependencies: pip install -r requirements.txt")
    else:
        print("✅ Chatbot initialized successfully!")
    
    # Run Flask development server
    # The server will be available at http://127.0.0.1:5000
    app.run(debug=True, host='127.0.0.1', port=5000)
