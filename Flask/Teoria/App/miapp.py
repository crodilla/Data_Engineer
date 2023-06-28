from flask import Flask
app = Flask(__name__)

if __name__ == "__main__":
    app.run()

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

