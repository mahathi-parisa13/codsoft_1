import tkinter as tk
from tkinter import scrolledtext
import datetime
import random
import webbrowser
import pyttsx3

engine = pyttsx3.init()

root = tk.Tk()

root.title("CampusMate AI")

root.geometry("900x700")

root.configure(bg="#0f172a")

engine.setProperty('rate', 170)

def speak(text):

    engine.say(text)

    engine.runAndWait()

def bot_response(message):

    text = message.lower()

    if "hello" in text or "hi" in text:

        return random.choice([
            "Hello! Welcome to CampusMate AI.",
            "Hi! How can I help you today?",
            "Hey! Nice to see you."
        ])

    elif "time" in text:

        return "Current time is " + datetime.datetime.now().strftime("%I:%M %p")

    elif "date" in text:

        return "Today's date is " + datetime.datetime.now().strftime("%d-%m-%Y")

    elif "joke" in text:

        jokes = [
            "Why do programmers hate bugs? Because bugs hate debugging.",
            "Why was the computer cold? It left its Windows open.",
            "Why do Python developers wear glasses? Because they cannot C."
        ]

        return random.choice(jokes)

    elif "motivate" in text:

        return "Success starts with consistency. Keep learning every day."

    elif "sad" in text or "stress" in text:

        return "Take a deep breath. Small progress every day leads to success."

    elif "weather" in text:

        return "Today's weather is pleasant and sunny."

    elif "open youtube" in text:

        webbrowser.open("https://youtube.com")

        return "Opening YouTube"

    elif "open google" in text:

        webbrowser.open("https://google.com")

        return "Opening Google"

    elif "python" in text:

        return "Python is a powerful programming language used in AI and web development."

    elif "ai" in text:

        return "Artificial Intelligence helps machines think and learn like humans."

    elif "exam" in text:

        return "Practice previous papers and revise important concepts regularly."

    elif "bye" in text:

        return "Goodbye! Have a wonderful day."

    else:

        return "Sorry, I did not understand that."

def loading_animation():

    chat_area.insert(tk.END, "\nCampusMate AI is typing")

    root.update()

    for i in range(3):

        chat_area.insert(tk.END, ".")

        root.update()

        root.after(250)

def send_message():

    user_message = entry_box.get()

    if user_message.strip() == "":

        return

    chat_area.config(state=tk.NORMAL)

    chat_area.insert(tk.END, "\n\nYou: ", "user")

    chat_area.insert(tk.END, user_message)

    response = bot_response(user_message)

    loading_animation()

    chat_area.insert(tk.END, "\nCampusMate AI: ", "bot")

    chat_area.insert(tk.END, response)

    chat_area.config(state=tk.DISABLED)

    chat_area.yview(tk.END)

    entry_box.delete(0, tk.END)

    speak(response)

header = tk.Frame(root, bg="#1e293b", height=90)

header.pack(fill=tk.X)

logo = tk.Label(
    header,
    text="CampusMate AI",
    bg="#1e293b",
    fg="#38bdf8",
    font=("Arial", 28, "bold")
)

logo.pack(pady=20)

chat_frame = tk.Frame(root, bg="#0f172a")

chat_frame.pack(
    padx=20,
    pady=20,
    fill=tk.BOTH,
    expand=True
)

chat_area = scrolledtext.ScrolledText(
    chat_frame,
    wrap=tk.WORD,
    font=("Arial", 14),
    bg="#111827",
    fg="white",
    insertbackground="white",
    relief=tk.FLAT,
    padx=20,
    pady=20
)

chat_area.pack(fill=tk.BOTH, expand=True)

chat_area.config(state=tk.DISABLED)

chat_area.tag_config(
    "user",
    foreground="#38bdf8",
    font=("Arial", 14, "bold")
)

chat_area.tag_config(
    "bot",
    foreground="#22c55e",
    font=("Arial", 14, "bold")
)

bottom_frame = tk.Frame(root, bg="#0f172a")

bottom_frame.pack(
    fill=tk.X,
    padx=20,
    pady=20
)

entry_box = tk.Entry(
    bottom_frame,
    font=("Arial", 16),
    bg="#1e293b",
    fg="white",
    insertbackground="white",
    relief=tk.FLAT
)

entry_box.pack(
    side=tk.LEFT,
    fill=tk.X,
    expand=True,
    ipady=14,
    padx=(0, 10)
)

send_button = tk.Button(
    bottom_frame,
    text="Send",
    font=("Arial", 16, "bold"),
    bg="#38bdf8",
    fg="white",
    activebackground="#0ea5e9",
    relief=tk.FLAT,
    padx=25,
    pady=10,
    command=send_message
)

send_button.pack(side=tk.RIGHT)

welcome_message = "Welcome to CampusMate AI! Ask me anything."

chat_area.config(state=tk.NORMAL)

chat_area.insert(tk.END, "CampusMate AI: ", "bot")

chat_area.insert(tk.END, welcome_message)

chat_area.config(state=tk.DISABLED)

root.mainloop()
