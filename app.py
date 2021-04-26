from flask import Flask
from flask import render_template # render_template loads the '.html' file from the templates directory. (default flask property)
from flask import request

app = Flask(__name__)

@app.route("/hello", methods=['POST', 'GET']) # 

def index():
    greeting = "HEllo World!"
    
    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"
        return render_template("index.html", greeting=greeting)
    else:
        return render_template("hello_form.html") 
    
if __name__ == "__main__":
    app.run()   
