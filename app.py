from flask import Flask, jsonify
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

# List of jokes
jokes = [
    "Why don't programmers like nature? It has too many bugs.",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why did the scarecrow win an award? He was outstanding in his field!",
    "What do you call a fake noodle? An impasta!",
    "Why did the math book look so sad? Because it had too many problems.",
    "What do you call a can opener that doesn't work? A can't opener!",
    "Why don't eggs tell jokes? They'd crack up!",
    "What do you call a pig that does karate? A pork chop!",
    "Why can't a nose be 12 inches long? Because then it would be a foot!",
    "What do you call a dinosaur that crashes his car? Tyrannosaurus wrecks!"
]

@app.route('/api/joke', methods=['GET'])
def get_joke():
    return jsonify({
        'joke': random.choice(jokes)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)