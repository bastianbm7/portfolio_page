import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.colored_header import colored_header
from streamlit_option_menu import option_menu
from streamlit_toggle import st_toggle_switch

import pandas as pd
import numpy as np

import json

from Codes import constant


def open_lottie(filename, key, height= 120, width = 120):
    """
    Function to open and display an lottie file saved
    as json in lottie_files directory.
    """
    
    # Path of lottie file
    path = f"lottie_files\\{filename}"
    
    # Open lottie file
    with open(path,"r") as file: 
        url = json.load(file) 
    
    # Display lottie fig
    st_lottie(url, 
        height=height, 
        width=width, 
        speed=0.8, 
        loop=True, 
        quality='high', 
        key=key
    )

    

def page_home():
    # 1.- Brief about me
    st.markdown("# Hi, I'm Bastián Barraza👋")
    st.caption(constant.info["Intro"])
    st.divider()
    st.markdown(constant.info["About"])
    
def page_education():
        st.markdown('# Education')

        
def page_skills():
    # Create a container to organize content using 
    # Streamlit's container feature
    
    st.markdown('# ⚒️ Skills')
    st.divider()
    
    with st.container():
        col1, col2= st.columns(2)
        
        # Display python logo in first column, first row
        col1.markdown("""### Python
                      I feel confident 
                      """)     
        with col2:
            open_lottie('python-2.json', 'python')
        
        
        col1, col2= st.columns(2)
        # Display R logo in second column, first row
        col1.markdown("""### R
                      I feel confident 
                      """)     
        with col2:
            open_lottie('r-5.json', 'r')
        
        col1, col2= st.columns(2)
        # Display tableau logo in third column, first row
        col1.markdown("""### Tableau
                      I feel confident 
                      """)     
        with col2:
            open_lottie('tableau.json', 'tableau')
        
        col1, col2= st.columns(2)
        # Display mysql logo in first column, second row
        col1.markdown("""### MySQL
                      I feel confident 
                      """)     
        with col2:
            open_lottie('mysql.json', 'mysql')
        
        
        col1, col2= st.columns(2)
        # Display excel logo in second column, second row
        col1.markdown("""### Excel
                      I feel confident 
                      """)     
        with col2:
            open_lottie('microsoft-excel.json', 'excel')
            
            
        col1, col2= st.columns(2)
        # Display github logo in third column, second row
        col1.markdown("""### Github
                      I feel confident 
                      """)     
        with col2:
            open_lottie('github.json', 'github')
            
            
            
            
            
def page_proyects():
    st.markdown('# Proyects')
    
    
    
def page_contact():
    st.markdown('# Contact me')
    
    email = constant.info["Email"]
    contact_form = f"""
    <form action="<https://formsubmit.co/{email}>" method="POST">
        <input type="hidden" name="_captcha value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    
    col1, col2 = st.columns(2)
    
    col1.empty()
    col2.markdown(contact_form, unsafe_allow_html=True)