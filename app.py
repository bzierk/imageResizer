from flask import Flask
from PIL import Image
import base64
from io import BytesIO
import requests

app = Flask(__name__)

@app.route("/image/<path:url>")
def check(url):


    return url

if __name__ == '__main__':
    app.run(host='0.0.0.0')
