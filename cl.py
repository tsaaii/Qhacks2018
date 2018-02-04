# Pip install the client:
# pip install clarifai
# gotta install these before

from clarifai.rest import ClarifaiApp
from clarifai.rest import Video as ClVideo

app = ClarifaiApp(api_key='a9fc6d37cd5f429bb1069b89c590a2af')# my api
model = app.models.get('general-v1.3')
video = ClVideo(filename='/Users/Owner/Desktop/323.mp4')
model.predict([video])
####################
