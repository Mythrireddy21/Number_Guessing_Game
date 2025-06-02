let timerInterval;
let startTime;

function startGame() {
    const level = document.getElementById("difficulty").value;

    fetch('/start_game', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ level })
    }).then(() => {
        document.querySelector('.game-area').style.display = 'block';
        document.getElementById('feedback').textContent = '';
        document.getElementById('guessInput').value = '';
        document.getElementById('guessInput').disabled = false;
        startTime = Date.now();
        startTimer();
    });
}

function startTimer() {
    clearInterval(timerInterval);
    timerInterval = setInterval(() => {
        const seconds = Math.floor((Date.now() - startTime) / 1000);
        document.getElementById('timer').textContent = seconds;
    }, 1000);
}

function submitGuess() {
    const guess = parseInt(document.getElementById("guessInput").value);

    fetch('/guess', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ guess })
    })
    .then(res => res.json())
    .then(data => {
        const feedback = document.getElementById("feedback");

        if (data.result === 'low') {
            feedback.textContent = `📉 Too low! Attempts: ${data.attempts}`;
        } else if (data.result === 'high') {
            feedback.textContent = `📈 Too high! Attempts: ${data.attempts}`;
        } else if (data.result === 'correct') {
            clearInterval(timerInterval);
            feedback.innerHTML = `
                🎉 Correct! The number was <strong>${data.number}</strong><br>
                Attempts: ${data.attempts}<br>
                Time: ${data.time} seconds
            `;
            document.getElementById('guessInput').disabled = true;
            loadScoreboard();
        }
    });
}

function loadScoreboard() {
    fetch('/scoreboard')
    .then(res => res.json())
    .then(data => {
        const tbody = document.querySelector("#scoreboard tbody");
        tbody.innerHTML = '';
        data.forEach(row => {
            const tr = document.createElement('tr');
            row.forEach(cell => {
                const td = document.createElement('td');
                td.textContent = cell;
                tr.appendChild(td);
            });
            tbody.appendChild(tr);
        });
    });
}

window.onload = loadScoreboard;
