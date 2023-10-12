import streamlit as st
import requests
from PIL import Image

url = 'https://api.nasa.gov/planetary/apod?' \
      'api_key=xoxdnyT173gfdDDfwcerbMAGAvlGjeZxhjNWnsEe'

response = requests.get(url)
content = response.json()

title = content['title']
image_url = content['url']
explanation = content['explanation']

image_response = requests.get(image_url)

#  Write image to the image.jpg file
with open('image.jpg', 'wb') as file:
    file.write(image_response.content)

# Create streamlit page with a wide layout
st.set_page_config(layout='wide')

st.title(title)
image = Image.open('image.jpg')
st.image(image, caption=title)
st.write(explanation)