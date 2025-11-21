# Task 04 – Pattern-Matching Chatbot
Student: bharat singh chouhan  
Student ID: CA/DE1/1099  
Domain: Python Programming  

## Project Description
This project is a simple pattern-matching chatbot built using Python.  
Instead of basic if-else replies, the chatbot uses Regular Expressions (Regex) to understand user messages.  
It detects greetings, identity questions, exit messages, and general queries using pattern matching and responds accordingly.

This is a part of the CodeAlpha Python Programming Internship.

## Features
- Regex-based pattern recognition  
- Handles greetings, questions, thanks, and exit commands  
- Clean knowledge base for easy expansion  
- Converts input to lowercase for reliable matching  
- Continues conversation until the user exits  
- Includes a fallback response for unknown messages  


## How It Works
1. User input is converted to lowercase  
2. Each regex pattern in the KNOWLEDGE_BASE is checked  
3. The first matching pattern returns the response  
4. If nothing matches, a default fallback reply is sent  

## How to Run
Open terminal inside the project folder and run:

---------------------------------------------------------------------------------------------------------------------------------------------


## Example Interaction
You: hello
Bot: Hello there! How may I assist you today?

You: how are you
Bot: I am an AI, so I don't have feelings, but I'm functioning perfectly! Thanks for asking!

You: your name
Bot: I am a simple Pattern-Matching Chatbot, created using Python for the CodeAlpha task.

You: bye
Bot: Goodbye! It was great chatting with you. Come back soon!



## Notes
- This is a rule-based chatbot, not an AI model  
- All patterns can be extended by adding new regex keys  
- No external libraries required (uses only Python’s built-in re module)