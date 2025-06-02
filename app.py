from flask import Flask, render_template, request, jsonify, session
from logic import init_game, check_guess, save_score, load_scores
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    data = request.get_json()
    if not data or 'level' not in data:
        return jsonify({'status': 'error', 'message': 'Missing difficulty level'}), 400
    
    level = data['level'].lower()
    if level not in ['easy', 'medium', 'hard']:
        return jsonify({'status': 'error', 'message': 'Invalid difficulty level'}), 400
    
    # Initialize game and save start_time as ISO string to session
    init_game(session, level)
    # Save start_time as ISO format string for JSON serializability
    session['start_time'] = datetime.now().isoformat()
    return jsonify({'status': 'started'})

@app.route('/guess', methods=['POST'])
def guess():
    data = request.get_json()
    if not data or 'guess' not in data:
        return jsonify({'status': 'error', 'message': 'Missing guess'}), 400
    
    try:
        guess_num = int(data['guess'])
    except ValueError:
        return jsonify({'status': 'error', 'message': 'Invalid guess, must be an integer'}), 400

    if 'number' not in session:
        return jsonify({'status': 'error', 'message': 'Game not started'}), 400

    result = check_guess(guess_num, session)

    if result['result'] == 'correct':
        try:
            start_time = datetime.fromisoformat(session['start_time'])
            elapsed = int((datetime.now() - start_time).total_seconds())
        except Exception:
            elapsed = -1  # fallback if time parse fails

        save_score(session['difficulty'], result['attempts'], elapsed)
        result['time'] = elapsed

    return jsonify(result)

@app.route('/scoreboard')
def scoreboard():
    scores = load_scores()
    return jsonify(scores)

if __name__ == '__main__':
    app.run(debug=True)
