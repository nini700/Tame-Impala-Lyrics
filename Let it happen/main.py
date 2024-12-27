from flask import Flask, render_template, send_from_directory
import time
import sys
from threading import Thread

app = Flask(__name__)

lyrics_data = {
    'lyrics': [
        "i cannot vanish",
        "you will not scare me",
        "try to get through it",
        "try to push through it",
        "you were not thinking that i will not do it",
        "they be lovin' someone",
        "and i'm another story",
        "take the next ticket",
        "take the next train",
        "why would i do it?",
        "anyone'd think that"
    ],
    'delays': [0.3, 0.2, 0.3, 0.4, 0.7, 0.4, 0.5, 0.7, 0.6, 0.5, 0.3]
}


@app.route('/')
def home():
    return render_template('index.html', lyrics=lyrics_data['lyrics'])


@app.route('/styles.css')
def serve_css():
    return send_from_directory('templates', 'styles.css')

if __name__ == '__main__':
    app.run(debug=True, port=5000)