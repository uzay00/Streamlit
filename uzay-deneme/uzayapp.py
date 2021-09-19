import pandas as pd
import numpy as np
#Graphs
import matplotlib.pyplot as plt

import joblib
import streamlit as st

st.title('Veri Bilimi Soru Seti')

st.write(
    """
    # Hello Uzay
    Here's our first attempt at 
    using data to create a table:
    """)

df = pd.DataFrame({
  'first column': ['A', 'B', 'C', 'D'],
  'second column': [10, 20, 30, 40]
})

df

option = st.selectbox(
    'Sizce doğru cevap hangisidir?',
     ['A', 'B', 'C', 'D'])

'You selected:', option

map_data = pd.DataFrame(
    np.random.randn(10, 2)/30 + [41.039,28.95],
    columns=['lat', 'lon'])



st.markdown('# Sorular')
st.markdown('## Soru 1')
st.map(map_data)



st.markdown('## Soru 2')
st.slider('What is your level', 0,10, step = 1)

st.markdown('## Soru 3')
st.success('Successful')
st.markdown('`This is a markdown`')
st.info("This is an information")
st.warning('This is a warning')


st.markdown('## Soru 4')
st.multiselect('Where do you work', ('London','Istanbul','Berlin'))
st.error('This is an error')


st.markdown('## Soru 4')
st.markdown('Veri dağılmını anlayalım.')
# sey initial mean
m = 0
# Change mean
m = st.slider(f'Select mean = {m}', 0,10, step = 1)
# sey initial mean
v = 1
# Change mean
v = st.slider(f'Select variance = {v}', 1,4, step = 1)

arr = np.random.normal(m, v, size=1000)


fig, ax = plt.subplots()
ax.hist(arr, bins=100)
ax.set_ylim([0, 50])
ax.set_xlim([-5, 10])
ax.grid()
st.pyplot(fig)



st.markdown('## Soru 5')
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






