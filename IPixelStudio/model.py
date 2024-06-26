from langchain_community.llms import EdenAI

import os

import base64
from io import BytesIO

from PIL import Image


def print_base64_image(prompt,resol,api):
    try:
        os.environ['EDENAI_API_KEY'] = api

        text2image = EdenAI(feature="image", resolution=resol, provider='deepai')
        image_output = text2image(prompt)

        # binary data
        decoded_data = base64.b64decode(image_output)

        # Create an in-memory stream to read the binary data
        image_stream = BytesIO(decoded_data)

        # Open the image using PIL
        image = Image.open(image_stream)

        return image
    except Exception as e:
        return Image.open(r"C:\Users\SAI SURYA TEJA\PycharmProjects\TexttoImage\images.jpeg")






