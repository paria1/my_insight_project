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

# pagevalues  = st.slider('What is the page value from google analytics?', float(data.pagevalues.min()), float(data.pagevalues.max()), float(data.pagevalues.mean()))
# exitrates  = st.slider('What is the exit rates from google analytics?', float(data.exitrates.min()), float(data.exitrates.max()), float(data.exitrates.mean()))
# administrative_duration  = st.slider('administrative_duration', float(data.administrative_duration.min()), float(data.administrative_duration.max()), float(data.administrative_duration.mean()))
# productrelated_duration  = st.slider('productrelated_duration', float(data.productrelated_duration.min()), float(data.productrelated_duration.max()), float(data.productrelated_duration.mean()))
# bouncerates  = st.slider('bouncerates', float(data.bouncerates.min()), float(data.bouncerates.max()), float(data.bouncerates.mean()))
# productrelated  = st.slider('productrelated', float(data.productrelated.min()), float(data.productrelated.max()), float(data.productrelated.mean()))
# month  = st.selectbox('month', ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] )
# visitortype  = st.selectbox('visitortype', ['Returning_Visitor', 'New_Visitor', 'Unkown'] )



pagevalues  = st.slider('What is the page value from google analytics?', float(data.pagevalues.min()), 300., 70.)
exitrates  = st.slider('What is the exit rates from google analytics?', float(data.exitrates.min()), float(data.exitrates.max()), .07)
administrative_duration  = st.slider('administrative_duration', float(data.administrative_duration.min()), float(600.), float(100.))
productrelated_duration  = st.slider('productrelated_duration', float(0), float(3600), float(120))
bouncerates  = st.slider('bouncerates', float(data.bouncerates.min()), float(data.bouncerates.max()), .1)
productrelated  = st.slider('productrelated', float(data.productrelated.min()), 200., float(30))
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
prob = clf_rf_f.predict_proba([[pagevalues,exitrates,administrative_duration,productrelated_duration,bouncerates,productrelated,month_Jan,month_Feb,month_Mar,month_Apr,month_May,month_Jun,month_Jul,month_Aug,month_Sep,month_Oct,month_Nov,month_Dec,visitortype_New_Visitor,visitortype_Returning_Visitor,visitortype_Unkown]])


import PIL
from PIL import Image
percent = round(prob[:,1][0],2)*100  # Percent for gauge
output_file_name = 'new_gauge.png'
x = 825
y = 825
loc = (x, y)
percent = percent / 100
rotation = 180 * percent  # 180 degrees because the gauge is half a circle
rotation = 90 - rotation  # Factor in the needle graphic pointing to 50 (90 degrees)
dial = Image.open('needle.png')
dial = dial.rotate(rotation, resample=PIL.Image.BICUBIC, center=loc)  # Rotate needle

gauge = Image.open('gauge.png')
gauge.paste(dial, mask=dial)  # Paste needle onto gauge
gauge.save(output_file_name)



buy_string = "Prediction Probability = " +  str(int(round(prob[:,1][0],2)*100)) + '%'
not_buy_string = "Prediction Probability = " +  str(int(round(prob[:,0][0],2)*100)) + '%'
# print(prob[:,0])
#checking prediction 
if st.button("Run me!"):
    st.header("The Customer Most Probably ")
    if predictions ==1:
        st.header("BUYS")
        st.header(buy_string)
    if predictions ==0:
        st.header("DOES NOT BUY")
        st.header(not_buy_string)
        
image = Image.open('new_gauge.png')

#st.title("Welcome to the PITeller")
st.image(image, width=300)


