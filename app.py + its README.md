# A simple web application using Flask
# This app displays a welcome message on the home page

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, welcome to my Flask web app!"

if __name__ == '__main__':
    app.run(debug=True)
