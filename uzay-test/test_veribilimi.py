import pandas as pd
import numpy as np
#Graphs
import matplotlib.pyplot as plt

import joblib
import streamlit as st


A = [3,5,7,9]
B = [1,2,9,0]

X = np.array([3,5,7,9])
Y = np.array([1,2,9,0])


def app():
  st.title('Veri Bilimi Soru Seti')


  st.markdown('## Soru 1')
  st.code("""
  A = [3,5,7,9]
  B = [1,2,9,0]
  # A Kesisim B
  AnB = [Eksik Kod]
  """)

  st.markdown('Yukarıdaki kod bloğunda `[Eksik Kodu]` Tamamlayın')
  eksik_kod=st.text_input("Kod:")

  if st.button("Tamamla"):
    try:
      C = eval(eksik_kod)
      st.success(f'Cevabınız Doğru: {C}')
    except:
      st.error('Yanlış Cevap')
      st.warning('Şunu deneyin: set(A).intersection(set(B))')


  #####################################
  st.markdown('## Soru 2')
  st.code("""
  X = np.array([3,5,7,9])
  Y = np.array([1,2,9,0])
  # A Toplam B
  Toplam = [Eksik Kod]
  """)

  st.markdown('Yukarıdaki kod bloğunda `[Eksik Kodu]` Tamamlayın')
  eksik_kod_2=st.text_input("Kod 2:")

  if st.button("Tamamla 2"):
    try:
      C2 = eval(eksik_kod_2)
      if np.sum(C2 - eval('X + Y') == 0)== 4:
        st.success(f'Cevabınız Doğru: {C2}')
      else:
        st.error(f'Yanlış Cevap : {C2}')

    except:
      st.error(f'Yanlış Cevap : {C2}')
      st.warning('Şunu deneyin: X + Y')


  st.markdown('https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py')





