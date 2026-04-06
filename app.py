# Michaela Angus 4/6/2026

from flask import Flask
app = Flask(__name__)  # Michaela

@app.route("/")
def home_page():
    return "Hello world!!"

if __name__ == "__main__":
    app.run(debug=True, port=5002)