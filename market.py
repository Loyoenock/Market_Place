from flask import Flask, render_temlate
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')
