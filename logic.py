import random
from datetime import datetime
import csv

difficulty_levels = {
    'easy': (1, 20),
    'medium': (1, 50),
    'hard': (1, 100)
}

def init_game(session, level):
    low, high = difficulty_levels[level]
    session['number'] = random.randint(low, high)
    session['attempts'] = 0
    session['difficulty'] = level
    # Store datetime as ISO format string (JSON serializable)
    session['start_time'] = datetime.now().isoformat()

def check_guess(guess, session):
    session['attempts'] += 1
    number = session.get('number')

    if guess < number:
        return {'result': 'low', 'attempts': session['attempts']}
    elif guess > number:
        return {'result': 'high', 'attempts': session['attempts']}
    else:
        return {'result': 'correct', 'attempts': session['attempts'], 'number': number}

def save_score(level, attempts, time_taken):
    with open('scoreboard.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([level, attempts, time_taken])

def load_scores():
    scores = []
    try:
        with open('scoreboard.csv', newline='') as file:
            reader = csv.reader(file)
            scores = [row for row in reader]
    except FileNotFoundError:
        # If no scoreboard file exists, return empty list
        pass
    return scores
