def chatbot():
    print("Chatbot: Hi! I'm a rule-based chatbot. How can I assist you today?")
    print("(Type 'exit' to end the conversation)")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Responses based on predefined rules
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm functioning as expected! How about you?")
        elif "your name" in user_input:
            print("Chatbot: I'm a simple rule-based chatbot, here to assist you.")
        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {current_time}.")
        elif "day" in user_input:
            from datetime import datetime
            current_day = datetime.now().strftime("%A")
            print(f"Chatbot: Today is {current_day}.")
        elif "weather" in user_input:
            print("Chatbot: I can't fetch live weather updates yet, but it's always good to keep an umbrella handy!")
        elif "what is your name"  in user_input:
            print ("my name chartboot in ai generated")   
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Could you rephrase it?")


chatbot()
