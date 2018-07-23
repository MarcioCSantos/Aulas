from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Olá Mundão veio sem porteira!"
if __name__ == '__main__':
    app.run(debug = True)
