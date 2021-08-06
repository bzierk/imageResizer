from flask import Flask, send_file
from PIL import Image
import base64
from io import BytesIO
import requests
import os

app = Flask(__name__, static_url_path='/static')

# @app.route("/<path:url>")
@app.route("/<width>/<height>/<path:url>")
def check(width, height, url):

    file_name_for_regular_data = url[-10:-4]
    # org_name = url[:-4]

    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content)).convert("RGB")
        file_name = file_name_for_regular_data + ".png"
        img.save("/static/" + file_name, "png")
        # response = requests.get(url)
        # img = Image.open(BytesIO(response.content)).convert("RGB")
        # img.thumbnail((int(width), int(height)))
        # img.show()
        #
        # file_name = org_name + ".jpg"
        # img.save(file_name, "jpeg")
        #
        # # return send_file(img, mimetype='image/jpg')
        # status = file_name

        status = "Image sent to server."
        return status
    except Exception as e:
        status = "Error! = " + str(e)

    return status

if __name__ == '__main__':
    app.run(host='0.0.0.0')
