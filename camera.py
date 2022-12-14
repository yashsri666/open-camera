import cv2
import streamlit as st

st.title("Webcam Live Feed")
run = st.button('Start Webcam')
stop = st.button('Stop Webcam')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
if stop:
    camera.release()