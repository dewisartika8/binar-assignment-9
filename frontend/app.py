from flask import Flask, render_template, request, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        response = requests.post('http://localhost:5000/api/register', json={'email': email, 'password': password})
        if response.status_code == 201:
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Registration failed. Please try again.', 'danger')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        response = requests.post('http://localhost:5000/api/login', json={'email': email, 'password': password})
        if response.status_code == 200:
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Please check your credentials.', 'danger')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)