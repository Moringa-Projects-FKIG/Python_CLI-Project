# 🩸 The Midnight Murder

## 📖 About the Project

*The Midnight Murder* is a Python command-line investigation game set in the Midnight Hotel.

During the hotel's annual Gala Night, the owner, *Hassan, is found dead inside his private office at **11:47 PM*. The cause of death is poison.

There are four suspects, and each one has a motive, an alibi, and a secret.

The player's job is to investigate the case, interview suspects, search locations, collect clues, and identify the murderer.

The murderer is randomly selected for each new investigation, making the game different each time.

---

## 🎮 Game Features

- 🕵️ Interview four suspects
- 🔎 Search different hotel locations for clues
- 📋 View discovered clues
- 🎭 Different possible murderers
- 🎲 Random murderer selection
- 💾 Save an investigation
- 📂 Load a saved investigation
- ❌ Make an accusation
- 🎨 Colored CLI interface and ASCII graphics
- ✅ Input validation

---

## 👥 Suspects

### Lance
*Occupation:* Chef

*Motive:* Hassan planned to fire him.

*Secret:* He was about to lose his job.

*Alibi:* He claims he was working in the kitchen.

---

### Chris
*Occupation:* Businessman

*Motive:* Hassan knew about his financial problems.

*Secret:* He owed the hotel a large amount of money.

*Alibi:* He claims he was with his girlfriend.

---

### Melody
*Occupation:* Journalist

*Motive:* Hassan knew a dangerous family secret.

*Secret:* She was protecting her brother.

*Alibi:* She claims she was interviewing guests.

---

### Michael
*Occupation:* Hotel Manager

*Motive:* Hassan discovered missing hotel money.

*Secret:* He had been secretly taking hotel money.

*Alibi:* He claims he was checking hotel rooms.

---

## 📍 Investigation Locations

The player can investigate four locations:

- Lobby
- Kitchen
- Office
- Garden

Each location contains evidence that can help the player solve the case.

---

## 🧑‍💻 Object-Oriented Programming

The project demonstrates the main principles of Object-Oriented Programming:

### Encapsulation
Data and related behavior are grouped inside classes such as Suspect and Investigation.

### Abstraction
Complex actions are simplified through methods such as:

- interview()
- search()
- accuse()
- save()
- load()

### Inheritance
Different suspect types inherit from the main Suspect class:

- Chef
- Businessman
- Journalist
- Manager

### Polymorphism
Each suspect type has its own version of the introduction() method, allowing different suspect types to respond differently.

---

## 💾 Data Persistence

The game uses a JSON file to save investigation progress.

Saved data includes:

- Current murderer
- Discovered clues
- Interviewed suspects

The saved investigation can be loaded later.

---

## 📁 Project Structure

```text
Midnight_Murder/
│
├── main.py
├── README.md
│
├── data/
│   └── saved_game.json
│
└── pages/
    ├── _init_.py
    │
    ├── Faith/
    │   ├── _init_.py
    │   └── suspects.py
    │
    ├── Gladys/
    │   ├── _init_.py
    │   └── clues.py
    │
    ├── Iman/
    │   ├── _init_.py
    │   └── investigation.py
    │
    └── Kennedy/
        ├── _init_.py
        └── game.py