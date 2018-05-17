from flask import Flask, jsonify                                    # importing Flask from flask library and jsonify
import random                    # importing module random from "venv/lib" that has methods that generate random numbers

from quotes import funny_quotes                                  # importing a method called funny_quotes from quotes.py


app = Flask(__name__)                                               # declaring a Flask application with params __name__


@app.route("/api/quotes")                                           # mapping url route for navigating to a page
def server_quotes_app():                        # defining a function that executes when this page is navigated to above
    quotes = funny_quotes()                                         # Calling the method from quotes.py
    nr_of_quotes = len(quotes)                                      # determinig number of quotes
    display_quote = quotes[random.randint(0, nr_of_quotes - 1)]     # selecting a quote randomly
    # jsonify compiles the selected quote into a block text
    return jsonify(display_quote)

# running the app directly """The alternative to running directly is creating instances of imported modules"""
if __name__ == "__main__":
    app.run(debug=True)   # debug = true makes the app throw exceptions for errors in code at the instance of said error


