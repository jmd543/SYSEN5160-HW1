# SYSEN5160 HW#1 - Testing out different Streamlit elements
# JMD543

import altair as alt
import math
import pandas as pd
import streamlit as st

# Text Elements - Titles & Latex Math Equations
    # Titles
    st.title("My First Time Coding in Python!")
    
    # Latex Math Equations
    st.latex(r'''
        E = mc^2
        ''')

# Data Display Elements - Tables & Metrics
    # Static Tables
    LOL = pd.DataFrame(
        np.random.randn(5,5), # Random matrix of numbers 5 rows x 5 columns
        columns = ('# of Bananas, # of Apples, # of Oranges, # of Mangoes, # of Peaches')
    st.table(LOL)

    # Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "72°F", "+2.7°F") # label, value, delta
    col2.metric("Wind", "12mph", "+4.0%")
    col3.metric("Humidity", "90%", "+1.7%")
    
# Chart Elements - Scatterplots on Maps & Simple Bar charts
    # Scatterplots on Maps
    import streamlit as st
    import pandas as pd
    import numpy as np

    BOS = pd.DataFrame(
         np.random.randn(1000, 2) / [50, 50] + [42.36, -71.05], # [lat -# = South, long -# = West]
         columns=['lat', 'lon'])
    st.map(BOS)

    # Simple Bar Charts
    BARchart = pd.DataFrame(
         np.random.randn(50, 3),
         columns=["Blueberries", "Apricots", "Strawberries"])
    st.bar_chart(BARchart)

# Input Widgets - Button & Radio & Selectbox & Slider & Date Input
    # Button
    if st.button('Say hello'):
        st.write('Why hello beautiful ^u^)')
        
    # Radio
    food = st.radio(
     "What's your favorite meal of the day?",
     ('Breakfast', 'Lunch', 'Dinner', 'Dessert'))

    if food == 'Breakfast':
         st.write('You selected Breakfast.')
    else:
         st.write("You didn't select Breakfast.")
        
    # Selectbox
    option = st.selectbox(
     'What would you like to improve about yourself?',
     ('Fitness', 'Nutrition', 'Pain relief'))
    st.write('You selected:', option)
        
    #Slider    
    weight = st.slider('How much do you weigh?', 0, 250, 110) # Question, Min, Max, Value
    st.write("You weigh", weight, 'pounds')

    # Date Input
    BDay = st.date_input(
     "When's your birthday?",
     datetime.date(1996, 5, 1))
    st.write('Your birthday is:', Bday)
        
# Media Elements - Image & Audio & Video
    # Video
    st.video("https://www.youtube.com/watch?v=fc_dscz6dm0")
    # All credit bleongs to original artist

# Display Progress & Status
    # Progress Bar
    import time
    bar = st.progress(0)
    for percent_complete in range(100):
         time.sleep(0.1)
         bar.progress(percent_complete + 1)

    # Spinner
    with st.spinner('Please sit back and relax....'):
        time.sleep(5)
    st.success('Results are in!')
        
    # Balloons
    st.balloons()
