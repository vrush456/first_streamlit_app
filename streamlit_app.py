import streamlit

streamlit.title('My Parents New Healthy diner')

streamlit.header('Breakfast Menu')
streamlit.title('🥣 Omega 3 & Blueberry oatmeal')
streamlit.title('🥗 Kale , Spinach & Rocket smoothie')
streamlit.title('🐔 Hard-Boiled free-range Egg')
streamlit.title('🥑🍞 Avocado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
