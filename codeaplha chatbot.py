# CodeAlpha Internship
# Task 4: Basic Chatbot

def chatbot():
    print("=================================")
    print("        WELCOME TO CHATBOT")
    print("=================================")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower().strip()

        # Greetings
        if user == "hello" or user == "hi" or user == "hey":
            print("Bot: Hello! Nice to meet you.")

        # How are you
        elif user == "how are you":
            print("Bot: I'm fine! Thanks for asking.")

        # Name
        elif user == "what is your name" or user == "your name":
            print("Bot: My name is CodeAlpha Chatbot.")

        # Help
        elif user == "help":
            print("Bot: You can say hello, ask my name, ask how I am, or say bye.")

        # Thanks
        elif user == "thank you" or user == "thanks":
            print("Bot: You're welcome!")

        # Goodbye
        elif user == "bye" or user == "exit":
            print("Bot: Goodbye! Have a great day.")
            break

        # Unknown input
        else:
            print("Bot: Sorry, I don't understand that.")


# Start chatbot
chatbot()