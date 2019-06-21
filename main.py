from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
    <title>Web Caesar</title>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <!-- create your form here -->
        <form action="/table" method="post">
            <label for = "text">
            	Rotate By:
			</label>
            <input type="text" name="rot" placeholder = "0">
            <textarea name="text"></textarea>
			<br>
            <input type="submit" value="Submit">
        </form> 
    </body>
</html>
"""

@app.route("/")
def encrypt(text,rot):
    new_text=rotate_string(text,rot)
    return f"<h1>{new_text}</h1>"

@app.route("/")
def index():
    return form

app.run()
