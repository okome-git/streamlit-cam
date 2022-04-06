import streamlit as st
import cv2
import time
from PIL import Image

st.markdown("# Camera Application")

device1 = 0
device2 = 1
# = user_input = st.text_input("input your video/camera device", "0")

cap1 = cv2.VideoCapture(device1)
cap2 = cv2.VideoCapture(device2)

col1, col2 = st.columns(2)

with col1:
    image_loc1 = st.empty()
with col2:
    image_loc2 = st.empty()

while cap1.isOpened:
    ret1, img1 = cap1.read()
    ret2, img2 = cap2.read()
    time.sleep(0.01)
    img1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    img2 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
    image_loc1.image(img1)
    image_loc2.image(img2)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()