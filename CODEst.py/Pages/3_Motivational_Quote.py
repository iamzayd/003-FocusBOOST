import streamlit as st
import streamlit as st
import requests
import datetime
import random
from bs4 import BeautifulSoup


# set page title
st.set_page_config(page_title="Study Is Fun", page_icon=":calendar:", layout="wide")



# set sidebar
st.sidebar.title("Time & Date")
st.sidebar.write(f"Today is {datetime.datetime.today().strftime('%Y-%m-%d')}")
st.sidebar.write(f"The time is {datetime.datetime.now().strftime('%H:%M')}")


# set main content
st.title("Motivational Quote")

# function to get a motivational quote
def get_motivational_quote():
    url = "https://www.oberlo.com/blog/motivational-quotes"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    quotes = soup.find_all('span', {'style': 'font-weight: 400;'})
    quote = random.choice(quotes).text.strip()
    
    if len(quote) > 36:
        return quote
    else:
        return get_motivational_quote()
    


    # display motivational message
quote = get_motivational_quote()
st.subheader(quote)


st.write('---')
st.sidebar.markdown('''
Created with 💜 by [Najeeb Saiyed](https://www.instagram.com/thiscloudbook/) And Srinivas''')