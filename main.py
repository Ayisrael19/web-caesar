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
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <!-- create your form here -->
        <form action="/" method="post">
            <label for = "text">
            	Rotate By:
			</label>
            <input type="text" name="rot" placeholder = "0">
            <textarea name="text">{0}</textarea><br>
            <input type="submit" value="Submit">
        </form> 
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    text =(request.form.get('text'))
    rot = int((request.form.get('rot')))
    new_text=rotate_string(text,rot)
    return form.format(new_text)

@app.route("/")
def index():
    return form.format(" ")

app.run()
