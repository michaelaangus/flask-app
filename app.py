# Michaela Angus 4/6/2026

from flask import Flask, render_template
app = Flask(__name__)  

@app.route("/about")
def home_page():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True, port=5002)