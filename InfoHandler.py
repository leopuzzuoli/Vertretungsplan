#This program gets the input from the DSB server and processes, then saves it so they can be used by Bot.js
print("STARTING SERVICE....")
from PIL import Image
import urllib.request
import requests
import base64
import filecmp
import time
import json
import os

print("LOADING COMPLETE")
print("GETTING DATA")
#PATH OF FILE TO OCR

subscription_key = ""
FILEPATH = "/Users/leonardo/Desktop/index.jpg"
OLDFILE = "/Users/leonardo/Documents/Files/Vertretungsplan/Vplaene/index.jpg"
#get data from server (PNG)

#make get request

#get images from get request

#process data with OCR (if the last image != the new one)
#-------------------------------------------------------------------------------

# Replace <Subscription Key> with your valid subscription key.
assert subscription_key

# You must use the same region in your REST call as you used to get your
# subscription keys. For example, if you got your subscription keys from
# westus, replace "westcentralus" in the URI below with "westus".
#
# Free trial subscription keys are generated in the westcentralus region.
# If you use a free trial subscription key, you shouldn't need to change
# this region.
vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"

analyze_url = vision_base_url + "analyze"

# Set image_path to the local path of an image that you want to analyze.
image_path = FILEPATH

# Read the image into a byte array
image_data = open(image_path, "rb").read()
headers    = {'Ocp-Apim-Subscription-Key': subscription_key,
              'Content-Type': 'application/octet-stream'}
params     = {'visualFeatures': 'Categories,Description,Color'}
response = requests.post(
    analyze_url, headers=headers, params=params, data=image_data)
response.raise_for_status()

# The 'analysis' object contains various fields that describe the image. The most
# relevant caption for the image is obtained from the 'description' property.
Vertretungsplan = response.json()
print(Vertretungsplan)
#-------------------------------------------------------------------------------
#save data as JSON

with open(os.getcwd() + "/Vplaene/aktuekllerplan.json", 'w') as outfile:
    json.dump(Vertretungsplan, outfile)

print("File saved")

#only check every 10 minutes and only between 5:00 AM and 12:AM
currenttime = time.localtime(time.time())
if(currenttime.tm_hour < 5):
    print("it is between 12:00 AM and 5:00 AM. Going to sleep")
    time.sleep((((5 - currenttime.tm_hour) - 1)* 60 * 60) + ((61 - currenttime.tm_min)* 60))
else:
    time.sleep(10 * 60)
