import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    ['hi', ['Hello!', 'Hi there!', 'Hey!']],['namaste', ['Namaste!', 'Namaskar!', 'Pranam!']]
    ['how are you', ['I am good, thank you!', 'I\'m doing well, thanks for asking.']],
    ['what is your name', ['My name is Chatbot.', 'I\'m Chatbot!']],['namaste', ['Namaste!', 'Namaskar!', 'Pranam!']]
    ['bye', ['Goodbye!', 'See you later!', 'Bye!']],
    ['default', ['I don\'t understand that. Can you ask me something else?']]
]
pairs.extend([
    ['what can you do', ['I can answer your questions, chat with you, or provide information on various topics.']],
    ['tell me a joke', ['Why don’t scientists trust atoms? Because they make up everything!']],
    ['what is the weather today', ['I\'m sorry, I cannot provide real-time information. You can check a weather website or app for that.']],
    ['tell me about yourself', ['I am a simple chatbot created by Abdur Rahman Adil using Python and NLTK.', 'I am here to chat with you and answer your questions.']],
    ['who created you', ['I was created by a person Named:Abdur Rahman Adil.']],
    ['do you like pizza', ['I am a chatbot, so I don\'t have preferences like humans do.']],
    ['how old are you', [' I am just a piece of software created for a assignment on 24-04-2024.']],
    ['what is the meaning of life', ['The meaning of life is a philosophical question that has been debated for centuries.']],
    ['where are you from', ['I exist in the realm of the internet, so I don\'t have a physical location.']],
    ['what is 1 + 1', ['1 + 1 equals 2.']],
    ['what is your favorite color', ['I don\'t have a favorite color because I am just a program.']],
    ['are you a robot', ['Yes, I am a chatbot, which is a type of artificial intelligence.']],
    ['what is the capital of France', ['The capital of France is Paris.']],
    ['who is the president of the United States', ['I\'m sorry, I cannot provide real-time information.']],
    ['how do I cook pasta', ['You can boil water, add salt, put in the pasta, and cook until it is al dente.']],
    ['tell me a fun fact', ['Did you know that an octopus has three hearts?']],
    ['what time is it', ['I\'m sorry, I cannot provide real-time information. You can check your device\'s clock for the current time.']],
    ['what is your favorite book', ['As a chatbot, I don\'t have the ability to read books or have preferences.']],
    ['what is the largest mammal', ['The blue whale is the largest mammal.']],
    ['what is the capital of Japan', ['The capital of Japan is Tokyo.']],
    ['what is your favorite movie', ['I don\'t have the ability to watch movies or have preferences.']],
    ['what is your favorite food', ['I am just a program and don\'t have the ability to eat food.']],
    ['what is the square root of 16', ['The square root of 16 is 4.']]
])


# Create a Chatbot with the defined pairs and reflections
chatbot = Chat(pairs, reflections)

# Define a function to chat with the bot
def chat():
    print("Hello! I'm a  chatbot. You can start talking to me. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
        if user_input.lower() == 'bye':
            break

# Call the chat function to start chatting
chat()

