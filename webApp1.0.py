from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/student')
def student():
    return render_template('Students.html')


@app.route('/bootstrap')
def bs():
    return render_template('bootstrap.html')


@app.route('/recap')
def recap():
    return render_template('recap.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
