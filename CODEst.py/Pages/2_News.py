
import streamlit as st
import requests
import datetime
import random
from bs4 import BeautifulSoup
st.set_page_config(page_title="Study Is Fun", page_icon=":calendar:", layout="wide")




# set sidebar
st.sidebar.title("Time & Date")
st.sidebar.write(f"Today is {datetime.datetime.today().strftime('%Y-%m-%d')}")
st.sidebar.write(f"The time is {datetime.datetime.now().strftime('%H:%M')}")



NEWS_API_KEY = "0be402260e51450aa7e5c96b2c93a2c5"




# function to get news headlines
def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    response = requests.get(url).json()
    articles = response["articles"]
    headlines = []
    for article in articles:
        st.subheader("🔹" + article["title"])

st.title("Todays Top Highlights News!")

get_news()



def ChangeWidgetFontSize(wgt_txt, wch_font_size = '12px'):
    htmlstr = """<script>var elements = window.parent.document.querySelectorAll('p'), i;
                for (i = 0; i < elements.length; ++i) 
                    { if (elements[i].textContent.includes(|wgt_txt|)) 
                        { elements[i].style.fontSize ='""" + wch_font_size + """'; } }</script>  """

    htmlstr = htmlstr.replace('|wgt_txt|', "'" + wgt_txt + "'")
    components.html(f"{htmlstr}", height=0, width=0)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css(r"C:\Users\Najeeb\Desktop\My Flight\style.css")


st.write('---')
st.sidebar.markdown('''
Created with 💜 by [Najeeb Saiyed](https://www.instagram.com/thiscloudbook/) And Srinivas''')