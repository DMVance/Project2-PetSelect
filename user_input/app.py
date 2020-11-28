from flask import Flask
from test_ideas_2 import size, choice, best_breed
import requests
import pandas as pd 


app = Flask(__name__)

@app.route("/")
def home():
    return "The app is up!"

@app.route("/choice")
def user_input():
    size()
    choice()
    best_breed()
    return best_breed()


    
    

if __name__ == "__main__":
    app.run(debug = True)