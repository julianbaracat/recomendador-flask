from flask import Flask, jsonify
import main
import os

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(main.main({}))
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
