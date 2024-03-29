# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user database (replace with a real database)
users = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        return redirect(url_for('dashboard'))
    else:
        return 'Invalid credentials. Please try again.'

@app.route('/dashboard')
def dashboard():
    return 'Welcome to the secured dashboard!'

if __name__ == '__main__':
    app.run(debug=True)
