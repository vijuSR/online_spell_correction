import os
import json
from flask import Flask, render_template, jsonify
from spell_correct import get_candidates_with_distance, generate_rank

app = Flask(__name__)

FILE_PATH = "./lexicon.json"


def read_lexicon_file(file_path):
    with open(file_path, 'r') as fp:
        js = json.load(fp)
    return list(set(js))


candidates = read_lexicon_file(FILE_PATH)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<query>", methods=['GET'])
def get_result(query):
    return jsonify(result=get_candidates_with_distance(query, candidates))


@app.route("/ranked/<query>", methods=['GET'])
def get_rank(query):
    return jsonify(result=generate_rank(query, candidates))


if __name__ == '__main__':
    app.secret_key = 'random bytes'
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
