import re

# 1. Chatbot Knowledge Base (Structured Responses)
# Key: Regular Expression pattern
# Value: Corresponding response
KNOWLEDGE_BASE = {
    # Greeting / Start
    r"^(hi|hello|hey|hola)[\s!.]*$": "Hello there! How may I assist you today?",

    # Status / Well-being
    r"how are you|how's it going": "I am an AI, so I don't have feelings, but I'm functioning perfectly! Thanks for asking!",

    # Identity / Name
    r"your name|who are you": "I am a simple **Pattern-Matching Chatbot**, created using Python for the CodeAlpha task.",

    # Capability / Function
    r"what can you do|help me": "I can answer basic questions and chat with you. Try asking me about my name!",

    # Gratitude
    r"thank you|thanks": "You're most welcome! Is there anything else I can help with?",

    # Exit / End
    r"^(bye|exit|quit|stop)[\s!.]*$": "Goodbye! It was great chatting with you. Come back soon!"
}


def get_chatbot_response(user_input):
    """
    Checks user input against defined patterns using Regular Expressions.
    """
    # Convert input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Iterate through the knowledge base
    for pattern, response in KNOWLEDGE_BASE.items():
        # Check if the user input matches the regular expression pattern
        # re.search looks for the pattern anywhere in the string
        if re.search(pattern, user_input):
            return response

    # Default fallback response if no pattern matches
    return "Hmm, I couldn't quite understand that. Could you rephrase your question?"


def main_chat_loop():
    """Main loop for the interactive chat session."""
    print("--- 👋 Welcome to the Pattern-Matching Chatbot! ---")
    print("Ask me anything simple, or type 'bye' to exit.")
    print("-" * 45)

    while True:
        user_message = input("You: ")

        # Check for exit commands explicitly before processing
        if re.search(r"^(bye|exit|quit|stop)", user_message.lower()):
            # The response will be handled by the KNOWLEDGE_BASE lookup,
            # but we use the input here to trigger the loop break.
            response = get_chatbot_response(user_message)
            print("Bot:", response)
            break

        response = get_chatbot_response(user_message)
        print("Bot:", response)


if __name__ == "__main__":
    main_chat_loop()
