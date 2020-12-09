from flask import Flask, request
from size.py import size


app = Flask(__name__)

@app.route("/")
def home():
    return "The app is up!"

@app.route("/choice")
def user_input():
    return """
    <html>
        <body>
            <p>What size dog do you prefer? <br>Small (less than 20 pounds) <br>Medium (between 21 and 60 pounds) <br>Large (more than 60 pounds)</p>
                <form methods = ["GET", "POST"] action = ".">
                    <p><input size = "user_size" /></p>
                    <p><input type = "submit" value = "size"/></p>
                </form>
            <br>
            <src = "results/adj_list.html">

            </body>
        </html>
        """



    

if __name__ == "__main__":
    app.run(debug = True)