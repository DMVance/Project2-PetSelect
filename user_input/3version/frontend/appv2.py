from flask import Flask, request

from size_v2 import best_breed

app = Flask(__name__)

@app.route("/")
def userinput():
    adj_list = ['smart', 'spunky', 'loyal', 'brave', 'bold', 'protective', 'sweet', 'trainable']
    dog_size = 'medium'
    data = best_breed(adj_list, dog_size)

   

if __name__ == "__main__":
    app.run(debug = True)