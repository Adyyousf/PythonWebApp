from flask import Flask
from flask import render_template # render_template loads the '.html' file from the templates directory. (default flask property)
from flask import request

app = Flask(__name__)

@app.route("/hello") #setting route as to where the corresponding thing lies on server. (i.e. after https://example.com/hello)

def index():
    name = request.args.get('name', 'Nobody') # using request.args to get data from the browser. (here 'Nobody' is a default value to display if name isn't specified)
    greet = request.args.get('greet', 'Hello')
    
    if name:
        greeting = f"{greet}, {name}" # contruct a greeting from the new name.
    else:
        greeting = "Hello, World"
    
    return render_template("index.html", greeting=greeting) # load templates/index.html and replace {greeting} inside it with greeting variable from the .py script. 
    
if __name__ == "__main__":
    app.run()   
