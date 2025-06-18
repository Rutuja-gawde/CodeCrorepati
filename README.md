# 🧠 Code Crorepati - Python Quiz Game

A fun and interactive Python quiz game inspired by *Kaun Banega Crorepati (KBC)*.  
This game uses **text-to-speech**, **sound effects**, **colorful terminal UI**, and **progressive difficulty levels** to make your quiz experience exciting!

---

## 🎮 Features

- 🗣️ Text-to-Speech using `pyttsx3`
- 🔊 Playsound effects for correct, wrong, and level-up
- 🎨 Colorful interface using `colorama`
- 📊 Multiple levels of difficulty (Easy, Medium, Hard)
- 🧠 Progressive money reward system
- 💬 Voice selection: Male / Female
- 👤 Player name input & personalized interaction

---

## 🛠 Requirements

- Python 3.x
- `colorama`
- `pyttsx3`
- `playsound==1.2.2`

Install all requirements using:

```bash
pip install -r requirements.txt
````

---

## 🚀 How to Run

```bash
python main.py
```

---

## 📁 File Structure

```
├── CodeCrorepati.py     # Game logic
├── question.mp3         # Sound when a question appears
├── correct.mp3          # Correct answer sound
├── wrong.mp3            # Wrong answer sound
├── win.mp3              # Game win sound
├── clapping.mp3         # Applause at the end
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🧪 Debug Tips

🐞 In case of failure (e.g., sound not playing or TTS issue), debug by adding:

```python
print("Request URL:", response.url)  # Debug
print("Response Content:", response.text)  # Debug
```

---
## 📌 Notes
This game is designed purely for practice and fun 🎯

You can enhance it with:

GUI (Tkinter or PyQt)

Timer for each question

Scoreboard and Leaderboard

Database storage for high scores

---
## 🙋‍♂️ Author

Developed by **Rutuja Gawde**🐱‍🐉

🚀 Just a beginner learning by building cool stuff!

💬 Feedback? Suggestions? Always welcome 😄

---

