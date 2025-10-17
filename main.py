# Simple AI Chatbot for businesses
# Works in Replit or Vercel
# Can use user's name and guide them toward a sale

import time

def chatbot():
    print("Hello! I’m your friendly assistant 🤖")
    
    # Ask for the user's name
    name = input("Before we start, what’s your first name? ")
    print(f"Nice to meet you, {name}!")

    # Main chat loop
    while True:
        user_input = input(f"{name}, what would you like to talk about today? (type 'exit' to quit) ")
        
        if user_input.lower() == "exit":
            print(f"Thanks for chatting, {name}! Have a great day! 🌟")
            break
        
        # Example chatbot responses
        if "buy" in user_input.lower() or "product" in user_input.lower():
            print(f"{name}, our product can really help you! Would you like a link to get it?")
        elif "help" in user_input.lower():
            print(f"No worries, {name}! I’m here to help. What do you need assistance with?")
        else:
            print(f"Interesting, {name}! Tell me more about that.")

        time.sleep(1)  # small pause to feel more natural

# Run the chatbot
chatbot()
