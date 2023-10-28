import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.colored_header import colored_header
from streamlit_option_menu import option_menu
from streamlit_toggle import st_toggle_switch

import pandas as pd
import numpy as np

from Codes import constant, pages

import os
import requests

    
# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("Codes/style.css")


# Create menu and friendly welcome on sidebar
# The menu contains 3 options: HOme - Proyects - Contact me
    
with st.sidebar:
    # Horizontal menu
    menu_option = option_menu(None, ["Home", "Education", "Skills", "Proyects", "Contact me"],
                            icons=['house-fill', 'bar-chart-fill''bar-chart-fill', 'bar-chart-fill', 'send-fill'],
                            menu_icon="cast", default_index=0, orientation="vertical",
                            styles={
                                "container": {"padding": "0!important", "background-color": "#fafafa"},
                                "icon": {"color": "orange", "font-size": "25px"},
                                "nav-link": {"font-size": "17px", "text-align": "left", "margin": "10px", "--hover-color": "#fffff"},
                                "nav-link-selected": {"background-color": "black"},
                            })
    

# Page 1: Home
if menu_option == 'Home':
    pages.page_home()
        
# -------------------------------
# 2.- Education
if menu_option == 'Education':
    pages.page_education()

# -------------------------------
# 3.- Skills
if menu_option == 'Skills':
    pages.page_skills()
            
# -------------------------------
# 4.- Proyectos
if menu_option == 'Proyects':
    pages.page_proyects()

# -------------------------------
#  5.- Contact
if menu_option == 'Contact me':
    pages.page_contact()
        
        
    
    