import streamlit as st
import requests
import datetime
import random
from bs4 import BeautifulSoup

# Initialize the tasks list
tasks = []

# Create a text input for the user to add new tasks
new_task = st.text_input('Add a new task:')

# If the user clicks the 'Add' button, add the task to the list
if st.button('Add'):
    tasks.append(new_task)

# Create a checkbox for each task in the list
for i, task in enumerate(tasks):
    if st.checkbox(task):
        # If the user checks the box, remove the task from the list
        tasks.pop(i)

# Display the remaining tasks
if tasks:
    st.write('Tasks remaining:')
    for task in tasks:
        st.write('- ' + task)
else:
    st.write('You have no tasks remaining!')


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



st.write('---')
st.sidebar.markdown('''
Created with 💜 by [Najeeb Saiyed](https://www.instagram.com/thiscloudbook/) And Srinivas''')