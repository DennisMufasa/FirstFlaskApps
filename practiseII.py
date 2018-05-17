from flask import Flask, render_template, request
import users

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/student')
def student():
    return render_template('Students.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    login = users.search(username, password)
    if login:
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)


