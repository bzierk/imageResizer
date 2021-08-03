from flask import Flask
from PIL import Image
import base64
from io import BytesIO
import requests

app = Flask(__name__)

@app.route("/image/<path:url>")
def check(url):


    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content)).convert("RGB")
        file_name = file_name_for_regular_data + ".jpg"
        img.save(file_name, "jpeg")
        status = "Image submitted."
    except Exception as e:
        status = "Error! = " + str(e)


    return status

if __name__ == '__main__':
    app.run(host='0.0.0.0')
