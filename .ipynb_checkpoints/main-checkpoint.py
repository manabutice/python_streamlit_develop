import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('streamlit 超入門')

st.sidebar.write('interactive Widgets')

text = st.sidebar.text_input('あなたの趣味を教えてください。')
condition = st.sidebar.slider('あなたの調子は？', 10, 100, 50)

'あなたの趣味:', text
'コンディション : ', condition

# if st.checkbox('show Image'):
#     img = Image.open('dog.jpg')
#     st.image(img, caption='kohei Imanishi', use_column_width=True)

