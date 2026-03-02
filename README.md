# A-Health-Game
This is a health game foe a lazy user who want discipline in his life but he can't 
class AnimeHealthAvatar:


# 🧙‍♂️  Leveling Up System

A simple RPG-style player progression system built in Python.
This project simulates how experience points (XP), leveling, and rank progression work in role-playing games.

The goal of this project is to practice **object-oriented programming**, **game logic design**, and **algorithmic thinking** using Python.

---

## 🚀 Features

* XP gain system based on player activities
* Automatic level-up mechanism
* Non-linear difficulty scaling
* Rank progression system
* XP carry-over after leveling
* Visual console progress bar
* Multiple level-ups handled automatically

---

## 🧠 How It Works

### XP Algorithm

The XP required for the next level increases as the player grows stronger.

```
XP Required = 100 × level^1.5
```

This creates a smooth progression curve:

* Early levels are fast and rewarding
* Mid levels require effort
* Higher levels feel meaningful and challenging

---

### Level-Up Logic

When earned XP exceeds the required threshold:

1. Player levels up
2. Extra XP carries over
3. Rank updates automatically
4. New XP requirement is calculated

---

## 🏆 Rank System

| Level Range | Rank              |
| ----------- | ----------------- |
| 1 – 4       | Novice Mage       |
| 5 – 9       | Intermediate Mage |
| 10 – 14     | Main Sorcerer     |
| 15+         | Archmage          |

---

## 📂 Project Structure

```
project/
│
├── player.py        # Player class and game logic
├── main.py          # Example usage
└── README.md
```

---

## ▶️ Usage

### 1. Create a Player

```python
player = Player("Yeager")
```

### 2. Gain XP

```python
player.gain_xp(120, "Completed Quest")
player.gain_xp(500, "Defeated Boss")
```

The system automatically:

* Checks level-ups
* Updates rank
* Displays progress

---

## 📊 Example Output

```
--- ⚔️ Yeager performed Completed Quest! ---
Received 120 XP.

✨ LEVEL UP! You are now Level 2 (Novice Mage)! ✨

[████------] 20/282 XP
Level: 2 | Rank: Novice Mage
```

---

## 🎯 Learning Objectives

This project demonstrates:

* Object-Oriented Programming (OOP)
* Class design and encapsulation
* Game progression algorithms
* Loop-based state management
* Clean function separation

---

## 🔮 Future Improvements

Possible extensions:

* Save/Load system (JSON)
* Health and combat mechanics
* Enemy system
* Skill tree
* GUI interface (Tkinter / Pygame)
* Database integration

---

## 🛠 Requirements

* Python 3.x
* No external libraries required

---

## 📜 License

This project is open-source and free to use for learning purposes.

---

## ✨ Author

Created as a learning project to explore programming and game system design using Python.
