import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My Moms New healthy diner')
streamlit.header('๐ฅฃ Breakfast Menu')
streamlit.text ('๐ฅ Hash Browns')
streamlit.text ('๐Veg Sausages')
streamlit.text (' ๐ฅScrambled Eggs')
streamlit.text ('๐ Mushrooms')
streamlit.header('๐๐ฅญ Build Your Own Fruit Smoothie ๐ฅ๐')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 


# Display the table on the page
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)







#streamlit.text(fruityvice_response)
#create a reoeatavke code block called function
def get_fruityvice_Data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
#new section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    back_from_function = get_Fruityvice_Data(fruit_choice)
    streamlit.datafram(back_from_function)
   # fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
   # fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   # streamlit.dataframe(fruityvice_normalized)
 
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


