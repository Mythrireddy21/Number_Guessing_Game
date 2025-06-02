# Number Guessing Game

A web-based Number Guessing Game built with Python Flask, where users try to guess a randomly generated number within a selected difficulty range. The game includes difficulty levels, a timer, and a scoreboard that tracks players’ performance saved in a CSV file.

## Features

- **Difficulty Levels:** Easy (1–20), Medium (1–50), Hard (1–100)
- **Real-time Feedback:** Informs if the guess is too high or too low
- **Timer:** Tracks the time taken to guess the correct number
- **Attempts Counter:** Counts the number of attempts per game
- **Scoreboard:** Stores scores (difficulty, attempts, time) in a CSV file and displays them


## Technologies Used

- Python 3
- Flask (web framework)
- HTML, CSS, JavaScript (frontend)
- CSV file for persistent scoreboard storage


## Project Structure
```
Number_Guessing_Game/
│
├── app.py               # Main Flask application
├── logic.py             # Game logic and CSV scoreboard functions
├── scoreboard.csv       # CSV file storing scores (auto-created)
├── requirements.txt     # Python dependencies
├── templates/
│   └── index.html       # Frontend HTML file
└── static/
    └── style.css        # CSS styles
```

## Installation & Setup

1. **Clone the repository:**

```bash
git clone https://github.com/Mythrireddy21/Number_Guessing_Game.git
cd Number_Guessing_Game
````

2. **Create and activate a virtual environment (optional but recommended):**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

*(requirements.txt should include `Flask` and `flask-cors`)*

4. **Run the Flask app:**

```bash
python app.py
```

5. **Open your browser and navigate to:**
```
http://127.0.0.1:5000
```

## How to Play

1. Select a difficulty level and click **Start**.
2. Enter your guess in the input box and click **Submit**.
3. The app will tell you if your guess is too high or too low.
4. Keep guessing until you find the correct number.
5. Your attempts and time taken will be recorded in the scoreboard.
6. Restart the game at any time using the **Restart** button.
7. View all previous game scores in the **Scoreboard** section.



## Customization

* You can add more difficulty levels or change the ranges in `logic.py` under `difficulty_levels`.
* The scoreboard uses a CSV file (`scoreboard.csv`) — you can clear or edit it manually if needed.
* Styling can be customized in `static/style.css`.


## License

This project is licensed under the MIT License.

```
Enjoy playing the Number Guessing Game! 🎯
```