from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
    return 'up and go'

def run():
    app.run(host="0.0.0.0", port=8080)

def keepAlive():
    server = Thread(target=run)
    server.start()