import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
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


streamlit.text(fruityvice_response)
streamlit.header("Fruityvice Fruit Advice!")


try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
  streamlit.error("Please select a fruit to get information")
  else:
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error()

streamlit.write('The user entered ', fruit_choice)



my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("use warehouse pc_rivery_wh")
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("The fruit load list contains:")
streamlit.dataframe(my_data_row)


fruit_choice = streamlit.text_input('What fruit would you like to add?')
streamlit.write('thanks for adding ', fruit_choice)



my_cur.execute("insert into fruit_load_list values ('from strealit')");




#fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.Fruit), ['Avocado', 'Strawberries'])
#fruits_to_show = my_fruit_list.loc[fruits_selected]
#streamlit.dataframe(fruits_to_show)
#streamlit.dataframe(fruits_selected)


