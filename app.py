from flask import Flask, render_template, request
import os
import exifread
from PIL import Image
from pypdf import PdfReader

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():

    file = request.files['file']

    filepath = os.path.join(
        app.config['UPLOAD_FOLDER'],
        file.filename
    )

    file.save(filepath)

    metadata = {}

    # Basic File Information
    metadata["File Name"] = file.filename

    metadata["File Size"] = (
        str(round(os.path.getsize(filepath) / 1024, 2))
        + " KB"
    )


    # Image Metadata Detection
    if file.filename.lower().endswith(('.jpg', '.jpeg', '.png')):

        img = Image.open(filepath)

        metadata["Image Format"] = img.format
        metadata["Image Width"] = str(img.width) + " pixels"
        metadata["Image Height"] = str(img.height) + " pixels"

    # PDF Metadata Detection
    elif file.filename.lower().endswith('.pdf'):

        pdf = PdfReader(filepath)

        metadata["File Type"] = "PDF Document"

        metadata["Number of Pages"] = str(len(pdf.pages))


        info = pdf.metadata

        if info:

            for key, value in info.items():
                metadata[str(key)] = str(value)

        else:

            metadata["PDF Status"] = "No PDF metadata found"
        # EXIF Metadata
        with open(filepath, 'rb') as image:

            tags = exifread.process_file(image)

            if tags:
                for tag in tags:
                    metadata[tag] = str(tags[tag])

            else:
                metadata["EXIF Status"] = "No EXIF metadata found"


    return render_template(
        'result.html',
        filename=file.filename,
        metadata=metadata
    )


if __name__ == '__main__':
    app.run(debug=True)