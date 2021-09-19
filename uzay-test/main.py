import streamlit as st
from multiapp import MultiApp
import test_veribilimi, test_yapayogrenme, test_derinogrenme, uzayapp


app = MultiApp()
app.add_app("Veri Bilimi", test_veribilimi.app)
app.add_app("Yapay Öğrenme", test_yapayogrenme.app)
app.add_app("Derin Öğrenme", test_derinogrenme.app)
app.add_app("Deneme", uzayapp.app)
app.run()