from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask Backend Running 🚀"

@app.route("/api")
def api():
    return {"message": "Hello from Flask API"}

app.run(host="0.0.0.0", port=5000)
