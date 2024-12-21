import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
patterns_responses = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you?", ["I'm doing great, thank you!", "I'm good, how about you?", "I'm fine, thanks for asking!"]),
    (r"what is your name?", ["I am a chatbot created by ChatGPT.", "You can call me Chatbot."]),
    (r"quit", ["Goodbye!", "See you later!", "Bye!"]),
    (r"(.*)", ["I'm sorry, I didn't quite understand that.", "Could you please rephrase your question?"])
]

# Create the chatbot using patterns and reflections
chatbot = Chat(patterns_responses, reflections)

def start_chat():
    print("Hello! I am a chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
        if user_input.lower() == "quit":
            break

# Start the chatbot
start_chat()
