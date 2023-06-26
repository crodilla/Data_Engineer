from flask import Flask
<<<<<<< HEAD
from config import 

app = Flask(__name__) # Para crear dicha instancia, debemos pasar como
=======


app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config")
app.config.from_pyfile("config.py")
>>>>>>> 3e0e813e0ebe30255faa2393e2c8cb8cd4ac0000


@app.route('/')
def index():
<<<<<<< HEAD
    return 'Hello World!'
=======
    return "<h1>Hello World !</h1>"

# app.add_url_rule("/","index",index)

@app.route("/user/<name>")
def user(name: str):
    return "<h1>Hello , {}!</h1>".format(name)

@app.route("/user1/<name>")
def user1(name):
    return "<h1>Bye, {}!</h1>".format(name)
>>>>>>> 3e0e813e0ebe30255faa2393e2c8cb8cd4ac0000
