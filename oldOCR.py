from PIL import Image
import urllib.request
import requests
import base64
import filecmp
import time
import json
import os

API_KEY = ""

if(not(filecmp.cmp(OLDFILE , FILEPATH))):
    with open(FILEPATH, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    encoded_string = "data:image/png;base64,"+ encoded_string.decode()

    r = requests.post("https://api.ocr.space/parse/image", data={"apikey" : API_KEY, "base64Image" : encoded_string , "language" : "ger"})
