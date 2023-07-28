import streamlit as st
import requests
import datetime
import random
from bs4 import BeautifulSoup


# set page title
st.set_page_config(page_title="Study Is Fun", page_icon=":calendar:", layout="wide")

# set main content
st.markdown("<h1 style='text-align: center;'>GO STUDY NOW!!</h1>", unsafe_allow_html=True)







# set sidebar
st.sidebar.title("Time & Date")
st.sidebar.write(f"Today is {datetime.datetime.today().strftime('%Y-%m-%d')}")
st.sidebar.write(f"The time is {datetime.datetime.now().strftime('%H:%M')}")




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

from PIL import Image
import requests
from io import BytesIO
import streamlit as st

# Set the desired image size
new_size = (450, 220)

# Retrieve the image from the URL
response = requests.get('https://th.bing.com/th/id/R.3eb9df7d04dee93e5c5f74e24b303e4c?rik=gqA%2bWSzfiguQtw&riu=http%3a%2f%2fwww.quickmeme.com%2fimg%2f17%2f177267736820af562917a449903ab1a0e08161f1f453e2c46f0f99fa75d10d8d.jpg&ehk=ks0og6xikuFIXmoz8JuiJ3ed2i4yI1lFvTqpn3QFw20%3d&risl=&pid=ImgRaw&r=0')
img = Image.open(BytesIO(response.content))

# Resize the image using the LANCZOS interpolation method
img = img.resize(new_size, resample=Image.LANCZOS)

# Display the image in Streamlit
st.image(img, caption='Image credit: Bing', use_column_width=True)


st.write('---')
st.sidebar.markdown('''
Created with 💜 by [Najeeb Saiyed](https://www.instagram.com/thiscloudbook/) And Srinivas''')


