from flask import Flask, render_template
import os

app = Flask(__name__)

print("Current Folder:", os.getcwd())
print ("Static Folder Exists:", os.path.exists("static/style.css"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/navigation")
def navigation():
    return render_template("navigation.html")

if __name__ == "__main__":
    app.run(debug=True)