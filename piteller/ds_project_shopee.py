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
data = pd.read_csv("sample_data.csv")
data = data.rename(str.lower, axis='columns')

# image = Image.open("house.png")
image = Image.open("online-shopping.jpg")

st.title("Welcome to the PITeller")
st.image(image, use_column_width=True)


#checking the data
st.write("Do you want to learn more about your customer shopping behavior? PITeller has the answer for you!")
st.markdown( "Don't you believe that? Let's try and see!")
check_data = st.checkbox("Check the sample data")
if check_data:
    # st.write(data.head())
    st.write(data.head())
st.write("Now let's find about  Customer Purchase Intention!")




#input the numbers

pagevalues  = st.slider('What is the page value from google analytics?', float(data.pagevalues.min()), float(data.pagevalues.max()), float(data.pagevalues.mean()))
exitrates  = st.slider('What is the exit rates from google analytics?', float(data.exitrates.min()), float(data.exitrates.max()), float(data.exitrates.mean()))
administrative_duration  = st.slider('administrative_duration', float(data.administrative_duration.min()), float(data.administrative_duration.max()), float(data.administrative_duration.mean()))
productrelated_duration  = st.slider('productrelated_duration', float(data.productrelated_duration.min()), float(data.productrelated_duration.max()), float(data.productrelated_duration.mean()))
bouncerates  = st.slider('bouncerates', float(data.bouncerates.min()), float(data.bouncerates.max()), float(data.bouncerates.mean()))
productrelated  = st.slider('productrelated', float(data.productrelated.min()), float(data.productrelated.max()), float(data.productrelated.mean()))
month  = st.selectbox('month', ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] )
visitortype  = st.selectbox('visitortype', ['Returning_Visitor', 'New_Visitor', 'Unkown'] )


month_Jan = month_Feb =  month_Mar = month_Apr = month_May = month_Jun = month_Jul =  month_Aug = month_Sep = month_Oct = month_Nov = month_Dec = 0
if month == 'Jan':
    month_Jan = 1
elif month == 'Feb':
    month_Feb = 1
elif month == 'Mar':
    month_Mar = 1
elif month == 'Apr':
    month_Apr = 1
elif month == 'May':
    month_May = 1
elif month == 'Jun':
    month_Jun = 1
elif month == 'Jul':
    month_Jul = 1
elif month == 'Aug':
    month_Aug = 1
elif month == 'Sep':
    month_Sep = 1
elif month == 'Oct':
    month_Oct = 1
elif month == 'Nov':
    month_Nov = 1
elif month == 'Dec':
    month_Dec = 1

visitortype_New_Visitor = visitortype_Returning_Visitor = visitortype_Unkown = 0
if visitortype == 'New_Visitor':
    visitortype_New_Visitor = 1
elif visitortype == 'Returning_Visitor':
    visitortype_Returning_Visitor = 1
elif visitortype == 'Unkown':
    visitortype_Unkown = 1


## My Ml Models
clf_rf_f = load('clf_rf_f.joblib')
predictions = clf_rf_f.predict([[pagevalues,exitrates,administrative_duration,productrelated_duration,bouncerates,productrelated,month_Jan,month_Feb,month_Mar,month_Apr,month_May,month_Jun,month_Jul,month_Aug,month_Sep,month_Oct,month_Nov,month_Dec,visitortype_New_Visitor,visitortype_Returning_Visitor,visitortype_Unkown]])[0]


#checking prediction 
if st.button("Run me!"):
    st.header("The Customer Most Probably ")
    if predictions ==1:
        st.header("BUYS")
    if predictions ==0:
        st.header("DOES NOT BUY")


