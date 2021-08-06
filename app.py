from flask import Flask, jsonify
from PIL import Image
import base64
from io import BytesIO
import requests

app = Flask(__name__, static_url_path='/static')

@app.route("/<width>/<height>/<path:url>")
def check(width, height, url):

    file_name_for_regular_data = url[-10:-4]

    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content)).convert("RGB")
        file_name = file_name_for_regular_data + ".png"
        img.thumbnail((int(width), int(height)))
        img.save(file_name, "png")

        with open(file_name, 'rb') as image_file:
            base64_bytes = base64.b64encode(image_file.read())

        base64_string = base64_bytes.decode('utf-8')
        json_data = {file_name: base64_string}

        return jsonify(json_data)

    except Exception as e:
        status = "Error! = " + str(e)

    return status

if __name__ == '__main__':
    app.run(host='0.0.0.0')
