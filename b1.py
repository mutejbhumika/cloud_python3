from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '\n\n\t\tBHUMIKA 21BCS7843'

if __name__ == '__main__':
    app.run(debug=True)
