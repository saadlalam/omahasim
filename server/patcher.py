import json
import random
import logging
import time
import hashlib

from flask import Flask
app = Flask(__name__)

UPDATES_PATH = r'C:\Users\saad\Desktop\Nerding\PyEnv\omaha\omahasim\server\updateHistory\updates.json'


def file_as_bytes(file):
    with file:
        return file.read()


@app.route('/')
def get():  
    hashed = hashlib.md5(file_as_bytes(open(UPDATES_PATH, 'rb'))).hexdigest()
    return hashed
if __name__ == "__main__":
    print("server up and listening...")
    app.debug = True
    app.run(host='0.0.0.0', port=8888)
    

