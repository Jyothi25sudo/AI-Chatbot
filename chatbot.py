# ============================================================================
# ChatBot Engine - Handles chatbot responses using Groq API
# ============================================================================

import os
from datetime import datetime
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

class ChatBot:
    """AI chatbot using Groq's Llama API for intelligent responses."""
    
    def __init__(self):
        """Initialize the chatbot with Groq API client."""
        # Get API key from environment variable
        api_key = os.getenv('GROQ_API_KEY')
        
        if not api_key:
            raise ValueError(
                "GROQ_API_KEY not found in .env file. "
                "Please add your API key to .env: GROQ_API_KEY=your_key_here"
            )
        
        # Initialize Groq client
        self.client = Groq(api_key=api_key)
        
        # Store conversation history
        self.conversation_history = []
        
        # System prompt for the chatbot
        self.system_prompt = """You are a friendly and helpful AI assistant named ChatBot. 
You are helpful, creative, and conversational. 
Keep responses concise (1-3 sentences usually) unless asked for more detail.
Be warm and engaging in your tone.
If you don't know something, say so honestly."""
    
    def get_response(self, user_message):
        """
        Generate a response using Groq API based on user message.
        
        Args:
            user_message (str): The user's message
            
        Returns:
            str: The chatbot's response from Groq API
        """
        try:
            # Store in conversation history
            self.conversation_history.append({
                "user": user_message,
                "timestamp": datetime.now().strftime("%H:%M")
            })
            
            # Prepare messages for API
            messages = [
                {
                    "role": "system",
                    "content": self.system_prompt
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ]
            
            # Call Groq API with a currently available model
            response = self.client.chat.completions.create(
                model="openai/gpt-oss-20b",  # Free, fast model on Groq
                messages=messages,
                temperature=0.7,
                max_tokens=500,
                top_p=1,
                stream=False
            )
            
            # Extract response text
            bot_response = response.choices[0].message.content
            
            # Store bot response in history
            self.conversation_history.append({
                "bot": bot_response,
                "timestamp": datetime.now().strftime("%H:%M")
            })
            
            return bot_response
        
        except Exception as e:
            # Handle API errors gracefully
            error_message = f"I encountered an issue: {str(e)}"
            self.conversation_history.append({
                "bot": error_message,
                "timestamp": datetime.now().strftime("%H:%M")
            })
            return error_message
    
    def get_conversation_history(self):
        """
        Get the current conversation history.
        
        Returns:
            list: List of conversation messages
        """
        return self.conversation_history
    
    def clear_history(self):
        """Clear the conversation history."""
        self.conversation_history = []


# Create a global chatbot instance
try:
    chatbot = ChatBot()
except ValueError as e:
    print(f"Error initializing chatbot: {e}")
    # Create a dummy chatbot that will show the error
    chatbot = None
