import streamlit as st
st.write('# 녹차빙수')
st.write('## 위해인의 녹차빙수 뿌리기 프로젝트')
st.write('## 위해인 부셔버려')
video_file = open('myvideo.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)