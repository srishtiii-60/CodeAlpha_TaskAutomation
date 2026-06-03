def chatbot_reply(user_input):
    user_input = user_input.lower().strip() # lowercase me convert kar diya
    
    if user_input == "hello" or user_input == "hi":
        return "Hi! 👋 How can I help you today?"
    
    elif user_input == "how are you":
        return "I'm fine, thanks! And you?"
    
    elif user_input == "what is your name":
        return "I'm a simple Python chatbot 🤖"
    
    elif user_input == "bye" or user_input == "goodbye":
        return "Goodbye! Have a great day! 👋"
    
    else:
        return "Sorry, I didn't understand that. Try: hello, how are you, bye"

def main():
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True: # loop chalega jab tak user bye na bole
        user = input("You: ")
        
        reply = chatbot_reply(user)
        print("Chatbot:", reply)
        
        if user.lower().strip() == "bye" or user.lower().strip() == "goodbye":
            break

main()