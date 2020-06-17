#import package
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import time
import json
from joblib import dump, load

#import the data
data = pd.read_csv("Data Clean.csv")
data1 = pd.read_csv("sample_data.csv")
# image = Image.open("house.png")
image = Image.open("online-shopping.jpg")

st.title("Welcome to the PITeller")
st.image(image, use_column_width=True)

## import some data
# min_dict = json.loads('min_dict.json')
# max_dict = json.loads('max_dict.json')
# st.write("max_dict", max_dict)

#checking the data
st.write("Do you want to learn more about your customer shopping behavior? PITeller has the answer for you!")
st.markdown( "Don't you believe that? Let's try and see!")
check_data = st.checkbox("Check the sample data")
if check_data:
    # st.write(data.head())
    st.write(data1.head())
st.write("Now let's find about  Customer Purchase Intention!")




#input the numbers
pagevalues = st.slider("What is the page value from google analytics?"
    ,int(data1.PageValues.min())
    ,int(data1.PageValues.max())
    ,int(data1.PageValues.mean()) )

exitrates = st.slider("What is the exit rates from google analytics?"
    ,float(data1.ExitRates.min())
    ,float(data1.ExitRates.max())
    ,float(data1.ExitRates.mean()) )





#splitting your data


## My Ml Models
clf_rf_f = load('clf_rf_f.joblib')
predictions = clf_rf_f.predict([[pagevalues,exitrates]])[0]


#checking prediction house price
if st.button("Run me!"):
    st.header("The Customer Most Probably ")
    if predictions ==1:
        st.header("BUYS")
    if predictions ==0:
        st.header("DOES NOT BUY")
    
    #.format(int(predictions)))
    #st.subheader("Your range of prediction is USD {} - USD {}".format(int(predictions-errors),int(predictions+errors) ))