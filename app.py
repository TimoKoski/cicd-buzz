import os
import signal
import platform
import datetime
from flask import Flask
from buzz import generator

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate_buzz():
    page = '<html><body>'
    page += '<p>{}</p>'.format(str(datetime.datetime.now()))
    page += '<p>platform.node(): {}</p>'.format(platform.node())
    page += '<h1>{}</h1>'.format(generator.generate_buzz())
    page += '</body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
