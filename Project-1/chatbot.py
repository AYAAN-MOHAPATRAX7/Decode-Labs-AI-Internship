# Project 1: Deterministic Rule-Based AI Chatbot
# DecodeLabs - Artificial Intelligence Internship


# --------------------------------------------------
# 1. KNOWLEDGE BASE
# --------------------------------------------------

responses = {
    "hello": "Hello! Welcome to my AI chatbot. How can I help you?",
    "hi": "Hi there! What can I do for you today?",
    "hey": "Hey! Nice to meet you.",

    "who are you": "I am a deterministic, rule-based AI chatbot created for Project 1.",

    "what is ai": (
        "Artificial Intelligence is the simulation of human intelligence "
        "processes by machines."
    ),

    "what is machine learning": (
        "Machine Learning is a branch of AI where computers learn patterns "
        "from data to make predictions or decisions."
    ),

    "what is python": (
        "Python is a high-level programming language known for its "
        "simplicity and readability."
    ),

    "how does this work": (
        "I work by matching your input with predefined rules stored "
        "inside a Python dictionary."
    ),

    "how are you": "I'm doing great! I'm ready to answer your questions.",

    "help": (
        "You can ask me about AI, Machine Learning, Python, "
        "how I work, or simply greet me. Type 'exit' to quit."
    ),

    "thank you": "You're welcome! I'm happy to help.",
    "thanks": "You're welcome!",

    "what can you do": (
        "I can recognize predefined questions and provide responses "
        "using rule-based decision making."
    )
}


# --------------------------------------------------
# 2. WELCOME MESSAGE
# --------------------------------------------------

print("=" * 55)
print("        DECODELABS AI RULE-BASED CHATBOT")
print("=" * 55)
print("Bot: Hello! I am your Rule-Based AI Assistant.")
print("Bot: Ask me something or type 'exit' to end the chat.")
print("=" * 55)


# --------------------------------------------------
# 3. CONTINUOUS CONVERSATION LOOP
# --------------------------------------------------

while True:

    # Take input from the user
    user_input = input("\nYou: ")

    # --------------------------------------------------
    # 4. INPUT SANITIZATION
    # --------------------------------------------------

    clean_input = user_input.lower().strip()

    # Ignore empty input
    if not clean_input:
        print("Bot: Please enter something.")
        continue


    # --------------------------------------------------
    # 5. EXIT STRATEGY
    # --------------------------------------------------

    if clean_input in ["exit", "quit", "bye"]:
        print("Bot: Goodbye! Thanks for chatting.")
        break


    # --------------------------------------------------
    # 6. INTENT LOOKUP + FALLBACK
    # --------------------------------------------------

    reply = responses.get(
        clean_input,
        "I'm sorry, I don't understand that yet. "
        "Type 'help' to see what I can do."
    )


    # --------------------------------------------------
    # 7. DISPLAY RESPONSE
    # --------------------------------------------------

    print("Bot:", reply)