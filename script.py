from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello , this is portfolio of two roommates!"

@app.route("/about")
def about_us():
    return "We are roommates at VESIT"

if __name__ == "__main__":
    app.run(debug=True)