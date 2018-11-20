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
    page = '<!DOCTYPE html>'
    page += '<html>'
    
    page += '<head>'
    page += '<meta charset="utf-8">'
    page += '<meta name="viewport" content="width=device-width, initial-scale=1">'
    page += '<title>DevOps Buzz Generator</title>'
    page += '</head>'
    
    page += '<body>'
    page += '<p>{}</p>'.format(str(datetime.datetime.now()))
    page += '<p>platform.node(): {}</p>'.format(platform.node())
    for i in range(10):
        page += '<h2>{}</h2>'.format(generator.generate_buzz())
    page += '</body>'
    
    page += '</html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
