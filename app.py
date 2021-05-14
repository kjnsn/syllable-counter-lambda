from flask import Flask, request, jsonify
from textblob import TextBlob
import json
import pyphen
import os
import sys
import nltk

nltk.data.path.append("/var/task/nltk_data")

app = Flask(__name__)


@app.route("/")
def handler():
    text = request.args.get('text', '')

    # Extract the words from the text.
    blob = TextBlob(str(text))

    headers = {'Access-Control-Allow-Origin': '*'}

    dic = pyphen.Pyphen(lang="en_US")
    return jsonify(list(map(dic.inserted, blob.words))), 200, headers


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
