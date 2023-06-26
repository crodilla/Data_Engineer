from flask import Flask
from config import 

app = Flask(__name__) # Para crear dicha instancia, debemos pasar como


@app.route('/')
def index():
    return 'Hello World!'