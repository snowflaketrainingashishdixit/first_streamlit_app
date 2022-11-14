import streamlit
import pandas
streamlit.title('My Moms New healthy diner')
streamlit.header('🥣 Breakfast Menu')
streamlit.text ('🥗 Hash Browns')
streamlit.text ('🐔Veg Sausages')
streamlit.text (' 🥑Scrambled Eggs')
streamlit.text ('🍞 Mushrooms')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 


# Display the table on the page
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
streamlit.header("Fruityvice Fruit Advice!")

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.Fruit), ['Avocado', 'Strawberries'])
#fruits_to_show = my_fruit_list.loc[fruits_selected]
#streamlit.dataframe(fruits_to_show)
streamlit.dataframe(fruits_selected)


