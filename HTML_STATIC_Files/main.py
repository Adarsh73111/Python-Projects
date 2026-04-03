# --- TOPIC 397: Rendering HTML Files with Flask ---
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # render_template automatically looks inside the 'templates' folder
    # for a file named 'index.html' and sends it to the browser.
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)