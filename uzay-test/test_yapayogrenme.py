import pandas as pd
import numpy as np
#Graphs
import matplotlib.pyplot as plt

import joblib
import streamlit as st

def app():
  st.title('Yapay Öğrenme Soru Seti')


  st.markdown('## Soru 1')
  review=st.text_input("Enter the Answer ")
  st.markdown(f'Your answer is {review}')

  if st.button("Predict Sentiment"):
    st.success(f'Your answer is {review}')  






  st.latex(r''' e^{i\pi} + 1 = 0 ''')

  st.code("""
  st.markdown('## Soru 3')
  st.success('Successful')
  st.markdown('`This is a markdown`')
  st.info("This is an information")
  st.warning('This is a warning')
  """)


  st.file_uploader('File uploader')


  st.markdown('# Daha fazlasi icin')
  st.markdown('Adres: https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py')


  st.markdown('https://docs.streamlit.io/en/stable/tutorial/aws_s3.html')







