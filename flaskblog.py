from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Olá Mundão veio sem porteira!<h1>"
if __name__ == '__main__':
    app.run(debug = True)
