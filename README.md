# imageResizer

Image resizing microservice currently hosted on Heroku.

## Usage

Calls can be made to https://cs361-image-resize-app.herokuapp.com/width/height/image_url

#### Parameters
Width - in pixels
Height - in pixels
Image URL - URL for the image you'd like to resize, should end in .jpg or .png

<b>Example</b>
https://cs361-image-resize-app.herokuapp.com/200/200/https://cdn2.bulbagarden.net/upload/thumb/2/21/001Bulbasaur.png/250px-001Bulbasaur.png



Original image:

![Original pic](https://cdn2.bulbagarden.net/upload/thumb/2/21/001Bulbasaur.png/250px-001Bulbasaur.png)

250px X 250px

Processed image:

![Processed pic](https://i.imgur.com/SZHQwx3.png)

200px X 200px


#### Returns
Service will return a JSON file with the image encoded as a base64 string which can be converted into any desired image type.
