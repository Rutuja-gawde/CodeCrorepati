from playsound import playsound
from colorama import init, Fore, Style
import pyttsx3
import time
from time import sleep

init(autoreset=True, convert=True)  # Auto reset colors

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

# 🎤 Get user info
print(Fore.YELLOW + "🎮 Welcome to Code Crorepati!")
speak("Welcome to Code Crorepati!")
speak("Let's start with your name.")
user_name = input("Enter your name: ")
speak(f"Hello {user_name}, let's begin the game!")

# 🎙️ Voice preference
print("\nChoose your preferred voice:")
speak("Choose your preferred voice.")
print(Fore.RED + "1. Male 👨")
print(Fore.MAGENTA + "2. Female 👩")
voice_choice = input("Enter 1 or 2: ")

# Set voice based on user preference
voices = engine.getProperty('voices')
if voice_choice == "1":
    engine.setProperty('voice', voices[0].id)  # Male
    print(Fore.CYAN + f"Hi {user_name}! You've selected Male Voice.\n")
    speak(f"Welcome {user_name}, you've selected male voice.")
else:
    engine.setProperty('voice', voices[1].id)  # Female
    print(Fore.CYAN + f"Hi {user_name}! You've selected Female Voice.\n")
    speak(f"Welcome {user_name}, you've selected female voice.")

engine.setProperty('rate', 180)
engine.setProperty('volume', 1.0)

easy_questions = [
    ["Who developed Python Programming Language", "Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum", "Niene Stom", "c"],
    ["Which type of Programming does Python support", "OOP", "Structured", "Functional", "All of the above", "d"],
    ["Is Python case sensitive", "No", "Yes", "Machine dependent", "None", "b"],
    ["Which of these is a core Python datatype", "List", "Dict", "Tuple", "All of these", "d"]
]

medium_questions = [
    ["What is the output of print(type([]))", "<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "<class 'set'>", "a"],
    ["What is the output of print(type(()))", "<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "<class 'set'>", "b"],
    ["What is used to define a block of code in Python", "Curly braces", "Parentheses", "Indentation", "Quotes", "c"]
]

hard_questions = [
    ["What does the 'join()' method do in Python", "Joins sets", "Joins lists", "Joins strings with separator", "Joins dictionaries", "c"],
    ["What is the purpose of 'self' in Python", "It defines a loop", "It refers to instance of class", "It refers to a module", "It’s a keyword for lists", "b"],
    ["Which of these is used to handle exceptions", "try/except", "if/else", "def/return", "while/break", "a"],
    ["What is list comprehension", "Method", "Loop structure", "Way to create lists concisely", "Keyword", "c"]
]
questions = easy_questions + medium_questions + hard_questions

levels = [1000, 2000, 4000, 8000, 15000, 32000, 64000, 125000, 250000, 500000, 1000000]

difficulty_tags = ["[EASY]", "[EASY]", "[EASY]", "[EASY]",
                   "[MEDIUM]", "[MEDIUM]", "[MEDIUM]",
                   "[HARD]", "[HARD]", "[HARD]", "[HARD]"]

money = 0

def delay_print(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

for i in range(len(questions)):
    question = questions[i]
    playsound("sound/question.mp3")  # 🔊 Play question music

    print(Fore.CYAN + f"\n{'='*50}")
    print(Fore.YELLOW + f"{difficulty_tags[i]} 💰 Question for Rs.{levels[i]}")
    print(Fore.CYAN + f"{'-'*50}")
    delay_print(Fore.GREEN + "Q." + question[0] + "❓")
    speak(question[0])

    print(Fore.BLUE + f"\na. {question[1]}")
    speak("Option a: " + question[1])
    print(Fore.BLUE + f"b. {question[2]}")
    speak("Option b: " + question[2])
    print(Fore.BLUE + f"c. {question[3]}")
    speak("Option c: " + question[3])
    print(Fore.BLUE + f"d. {question[4]}")
    speak("Option d: " + question[4])

    answer = input(Fore.MAGENTA + "\n👉 Enter your answer (a/b/c/d): ").lower()
    print(Fore.CYAN + "🔒 Locking your answer...")

    speak("Locking your answer")
    time.sleep(1)

    if answer == question[5]:
        playsound("sound/correct.mp3")  # 🔊 Correct answer sound
        print(Fore.GREEN + f"✅ Correct Answer! You have won Rs.{levels[i]}")
        speak(f"Correct answer, {user_name}! You have won {levels[i]} rupees.")
        money = levels[i]
    else:
        playsound("sound/wrong.mp3")  # 🔊 Wrong answer sound
        print(Fore.RED + f"❌ Wrong Answer! Game Over!")
        speak(f"Sorry {user_name}, that's the wrong answer. Game over.")
        break

print(Fore.CYAN + f"\n{'='*50}")
playsound("sound/win.mp3")  # 🔊 Final win or end sound
print(Fore.YELLOW + f"\n🎉 Thank you for playing the game, {user_name}!")
speak(f"Thank you for playing Code Crorepati, {user_name}!")
print(Fore.GREEN + f"💰 You have won Rs.{money}")
speak(f"You have won {money} rupees.")
print(Fore.CYAN + f"\n{'='*50}")
playsound("sound/clapping.mp3")  # 🔊 Applause sound
