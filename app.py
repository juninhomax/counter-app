import os
from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder=".")
CORS(app)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(".", path)

if __name__ == "__main__":
    port = int(os.environ.get("WORKER_1") or os.environ.get("PORT", 12000))
    print(f"🚀 Starting web server on 0.0.0.0:{port}", flush=True)

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False,
        use_reloader=False
    )
