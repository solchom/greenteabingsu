import streamlit as st  #streamlit를 st로 정의
import pandas as pd     #pandas를 pd로 정의
import numpy as np      #numpy를 np로 정의
import tkinter as tk


st.title(':green[녹차빙수]')    #제목

st.header('위해인의 :green[녹차빙수] 뿌리기 프로젝트 ') #부제목

st.header(':green[녹차빙수] 사진')  #설명

from PIL import Image   #녹차빙수 사진
image = Image.open('green tea bingsu.png')  #사진
st.image(image, caption='녹차빙수에용') #작은글씨


st.write('## 위해인 :red[파괴]')    #설명

#위해인 파괴 영상
video_file = open('myvideo.mp4', 'rb')  #영상
video_bytes = video_file.read()
st.video(video_bytes)

#사진 다운로드
with open("ugly.png", "rb") as file:
    btn = st.download_button(
            label="혐짤 다운로드",
            data=file,
            file_name="ugly.jpg",
            mime="image/png"
          )