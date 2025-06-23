from flask import Flask, jsonify
import main

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(main.main({}))