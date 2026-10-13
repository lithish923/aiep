"""
EXPERIMENT 4 — RULE-BASED CHATBOT
Source: 22IT702 LAB MANUAL (Page 8)
Note: Implemented procedurally without 'def'
"""

print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    try:
        user = input("You: ").strip().lower()
    except EOFError:
        print("\nChatbot: Goodbye!")
        break

    if user == "hello":
        print("Chatbot: Hi! How can I help you?")
    elif user == "how are you":
        print("Chatbot: I am functioning well. Thank you!")
    elif user == "what is ai":
        print("Chatbot: AI stands for Artificial Intelligence.")
    elif user == "bye":
        print("Chatbot: Goodbye!")
        break
    else:
        print("Chatbot: Sorry, I don't understand.")
