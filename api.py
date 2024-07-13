# api.py
from flask import Flask, jsonify
from flask_cors import CORS
from db_connection import fetch_tweets

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains on all routes

@app.route('/api/tweets', methods=['GET'])
def get_tweets():
    tweets = fetch_tweets()
    return jsonify(tweets)

if __name__ == '__main__':
    app.run(debug=True)
