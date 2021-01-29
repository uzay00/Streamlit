import streamlit as st
import pickle
import pandas as pd
from PIL import Image



html_temp = """
<div style="background-color:rgba(0, 0, 255, 0.3);padding:7px">
<h2 style="border:2px solid white;color:white;text-align:center;">Telco Company Customer Churn Prediction Model</h2>
</div>"""
st.markdown(html_temp,unsafe_allow_html=True)
im = Image.open("image.jpeg")
st.image(im, width=700)#, caption="Telco Churn Prediction")

model = pickle.load(open("my_model", "rb"))

st.sidebar.info('Services')

st.info('Account Info')

service=st.sidebar.selectbox("Internet service type", ('DSL', 'Fiber optic'))
security=st.sidebar.selectbox("Customer has online security", ('Yes', 'No'))
backup=st.sidebar.selectbox("Customer has online backup", ('Yes', 'No'))
protection=st.sidebar.selectbox("Customer has device protection", ('Yes', 'No'))
support=st.sidebar.selectbox("Customer has technical support", ('Yes', 'No'))
contract=st.selectbox("Contract type", ('Month-to-month', 'One year', 'Two year'))
tenure=st.slider("How long been as a customer (month)",1, 72)
monthly=st.slider("Monthly charge",0, 150)
total=st.slider("Total amount charge", 0,9000, step=50)

my_dict = {
    "tenure": tenure,
    "Internet Service": service,
    "Online Security": security,
    "Online Backup": backup,
    "Device Protection": protection,
    "Tech Support": support,
    "Contract":contract,
    "Monthly Charges":monthly,
    "Total Charges":total}

df = pd.DataFrame.from_dict([my_dict])

columns=['tenure', 'MonthlyCharges', 'TotalCharges', 'InternetService_DSL',
       'InternetService_Fiber optic', 'OnlineSecurity_No',
       'OnlineSecurity_Yes', 'OnlineBackup_No', 'OnlineBackup_Yes',
       'DeviceProtection_No', 'DeviceProtection_Yes', 'TechSupport_No',
       'TechSupport_Yes', 'Contract_Month-to-month', 'Contract_One year',
       'Contract_Two year']


df2 = pd.get_dummies(df).reindex(columns=columns, fill_value=0)

prediction = model.predict(df2)

st.table(df)

if st.button('Predict'):
    if prediction == 'Yes':
        st.warning('Yes, the customer will terminate the service.')
    else:
        st.success('No, the customer is happy with Telco Services.')



