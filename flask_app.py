from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<p>Don't put it down, put it away</p>"

if __name__ == "__main__":
    app.run(debug=True)
