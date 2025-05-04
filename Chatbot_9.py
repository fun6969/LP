def chatbot():
    print("Welcome to ShopBot! How can I assist you today?")
    print("Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input in ['exit', 'quit', 'bye']:
            print("ShopBot: Thank you for visiting. Have a great day!")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("ShopBot: Hello! How can I help you?")

        elif "hours" in user_input or "time" in user_input:
            print("ShopBot: We're open from 9 AM to 9 PM, Monday to Saturday.")

        elif "products" in user_input or "items" in user_input:
            print("ShopBot: We sell electronics, clothing, and home essentials. What are you looking for?")

        elif "support" in user_input or "help" in user_input:
            print("ShopBot: You can reach our support at support@shopbot.com or call 123-456-7890.")

        elif "location" in user_input or "address" in user_input:
            print("ShopBot: We're located at 123 Main Street, Springfield.")

        elif "return" in user_input or "refund" in user_input:
            print("ShopBot: You can return items within 30 days with a receipt.")

        else:
            print("ShopBot: I'm sorry, I didn't understand that. Can you rephrase your question?")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
