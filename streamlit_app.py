import streamlit
streamlit.title('My Parents new healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kasle, Spinach & rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🍌🥭Build Your Own Fruit Smoothie🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruitSelected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado' , 'Strawberries']) 
fruit_to_Show = my_fruit_list.loc[fruitSelected]

streamlit.dataframe(fruit_to_Show)

import requests
fruityvice_response = requests.get("https://fruitvice.com/api/fruit/watermelon")
streamlit.text(fruitvice_response)
