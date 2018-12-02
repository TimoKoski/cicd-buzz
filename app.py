import os
import signal
import platform
import datetime
from flask import Flask
from buzz import generator

# https://coder-coder.com/how-to-make-simple-website-html/

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate_buzz():
    page = '<!DOCTYPE html>'
    page += '<html>'
    
    page += '<head>'
    page += '<meta charset="utf-8">'
    page += '<meta name="viewport" content="width=device-width, initial-scale=1">'
    page += '<meta name="author" content="Adrian Yorke">'
    page += '<title>DevOps Buzz Generator</title>'
    #page += '<link rel="shortcut icon" type="image/x-icon" href="/favicon.ico">'
    #page += '<link rel="shortcut icon" type="image/x-icon" href={{ url_for("images", filename="favicon.ico") }}>'
    #page += '<link rel="icon" href="/images/favicon-32x32.png">'
    #page += '<link rel="shortcut icon" href="/favicon/devops_cycle_1_flat-512.png">'
    #page += '<link rel="icon" type="image/png" href="/favicon/devops_cycle_1_flat-512.png">'
    page += '</head>'
    
    page += '<body>'
    page += '<p>{}</p>'.format(str(datetime.datetime.now()))
    page += '<p>platform.node(): {}</p>'.format(platform.node())
    page += '<h1>{}</h1>'.format(generator.generate_buzz())
    page += '</body>'
    
    page += '</html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
