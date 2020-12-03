from flask import Flask, request

from size import size_

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def userinput():
    errors = ""
    if request.method == "POST":
        user_size = None
        try:
            user_size = request.form["user_size"]
        except:
            errors += "issue"
        if user_size is not None:
            result = size_(user_size)
            return '''
                <html>
                    <body>
                        <p>Select a description of your ideal dog! {result}</p>
                        <p><a href="/">Click here to choose again</a>
                    </body>
                </html>
            '''.format(result=result)
    return """
    <html>
        <body>
            {errors}
            <p>What size dog do you prefer? 
                <br>Small (less than 20 pounds) 
                <br>Medium (between 21 and 60 pounds) 
                <br>Large (more than 60 pounds)</p>
            <form method = "post" action = ".">
                <p><input name="user_size" /></p>
                <p><input type = "submit" value = "submit size"/></p>
                </form>
            </body>
        </html>
        """.format(errors=errors)




    

if __name__ == "__main__":
    app.run(debug = True)