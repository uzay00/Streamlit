import streamlit as st
import pickle
import pandas as pd


html_temp = """
<div style="background-color:tomato;padding:10px">
<h1 style="color:white;text-align:center;">Car Price Prediction </h1>
</div>"""
st.markdown(html_temp,unsafe_allow_html=True)

model = pickle.load(open("my_model", "rb"))

hp=st.slider("What is the hp of your car?", 60, 200, step=5)
km=st.slider("What is the km of your car", 0,100000, step=500)
car_model=st.selectbox("Select model of your car", ('Audi A1', 'Audi A2', 'Audi A3'))
body_type=st.selectbox("Select body type of your car", ('Convertible', 'Coupe', 'Off-Road', 'Other', 'Sedans', 'Station wagon', 'Compact'))
color=st.selectbox("What is the color of your car", ('Beige', 'Red', 'Brown','White','Grey','Blue','Silver','Black','Violet','Yellow','Green','Bronze','Orange'))
gear=st.selectbox("What is the gearing type of your car", ('Automatic', 'Manual', 'Semi-automatic'))
extras=st.multiselect("Select extras for your car", ('Alloy wheels', 'Cab or rented Car', 'Catalytic Converter','Handicapped enabled','Right hand drive','Roof rack','Shift paddles','Ski bag','Sport package','Sport seats','Sport suspension','Touch screen','Trailer hitch','Tuned car','Voice Control','Winter tyres'))


my_dict = {
    "hp": hp,
    "km": km,
    "make_model": car_model,
    "body_type": body_type,
    "Body Color": color,
    "Gearing Type": gear,
    "Extras":extras
}

df = pd.DataFrame.from_dict([my_dict])

columns=['hp',
         'km',
 'make_model_A1', 'make_model_A2', 'make_model_A3',
 'body_type_Convertible', 'body_type_Coupe', 'body_type_Off-Road', 'body_type_Other', 'body_type_Coupe', 'body_type_Sedans',
 'body_type_Station wagon', 'body_type_Compact'
 'Body Color_Black', 'Body Color_Blue', 'Body Color_Bronze', 'Body Color_Brown', 'Body Color_Green', 'Body Color_Grey', 'Body Color_Orange', 'Body Color_Red', 'Body Color_Silver', 'Body Color_Violet', 'Body Color_White', 'Body Color_Yellow', 'Body Color_Beige',
 'Gearing Type_Manual', 'Gearing Type_Semi-automatic', 'Gearing Type_Automatic']

df1 = df.drop(['Extras'], axis = 1)

df1 = pd.get_dummies(df1).reindex(columns=columns, fill_value=0)

df_extra = df['Extras'].str.get_dummies(',')

df = df1.join(df_extra)

prediction = model.predict(df)

st.success("The estimated price of your car is €{}. ".format(int(prediction[0])))

