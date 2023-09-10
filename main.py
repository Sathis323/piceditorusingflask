from flask import Flask, render_template, request, redirect, url_for
from PIL import Image, ImageFilter
import os

app = Flask(__name__)

# Define the upload folder for images
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to process and save the uploaded image
def process_image(image):
    # Example: Applying a blur filter to the image
    edited_image = image.filter(ImageFilter.BLUR)
    return edited_image

@app.route('/', methods=['GET', 'POST'])
def index():
    edited_image = None
    if request.method == 'POST' and 'image' in request.files:
        image = request.files['image']
        if image.filename != '':
            # Save the uploaded image to the upload folder
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(image_path)

            # Process the image
            edited_image = process_image(Image.open(image_path))
            edited_image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'edited_' + image.filename)
            edited_image.save(edited_image_path)

    return render_template('index.html', edited_image=edited_image)

if __name__ == '__main__':
    app.run(debug=True)
