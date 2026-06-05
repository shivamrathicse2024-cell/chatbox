import random
from datetime import datetime

print("=" * 40)
print("      SIMPLE PYTHON CHATBOT")
print("=" * 40)

name = input("Enter your name: ")

greetings = [
    f"Hello {name}!",
    f"Hi {name}!",
    f"Nice to meet you {name}!"
]

print(random.choice(greetings))

while True:

    msg = input(f"\n{name}: ").lower().strip()

    if msg in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif msg == "how are you":
        print("Bot: I'm doing great. Thanks for asking!")

    elif msg == "your name":
        print("Bot: I am a Python ChatBot.")

    elif msg == "my name":
        print(f"Bot: Your name is {name}.")

    elif msg == "time":
        print("Bot:", datetime.now().strftime("%H:%M:%S"))

    elif msg == "date":
        print("Bot:", datetime.now().strftime("%d-%m-%Y"))

    elif msg == "joke":

        jokes = [
            "Why do programmers hate nature? Too many bugs.",
            "Python is my favourite snake.",
            "Debugging is like being a detective in your own crime movie."
        ]

        print("Bot:", random.choice(jokes))

    elif msg == "help":

        print("\nAvailable Commands:")
        print("hello")
        print("how are you")
        print("your name")
        print("my name")
        print("time")
        print("date")
        print("joke")
        print("bye")

    elif msg in ["bye", "exit", "quit"]:

        print(f"Bot: Goodbye {name}! Have a nice day.")
        break

    elif msg == "thanks":

        print("Bot: You're welcome!")

    else:

        responses = [
            "Sorry, I don't understand.",
            "Can you try another command?",
            "I am still learning."
        ]

        print("Bot:", random.choice(responses))
