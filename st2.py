import streamlit as st 
import pyogrio

st.title('시군구별 합계출산율')

from PIL import Image

img=Image.open('Figure_1.png',"rb")

st.image(img)
