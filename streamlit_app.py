import streamlit as st
import pandas as pd
import numpy as np

from Codes import constant, pages

            
            
# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("Codes/style.css")


# Create menu and friendly welcome on sidebar
# The menu contains 3 options: HOme - Proyects - Contact me

# Sidebar: If using streamlit_option_menu
with st.sidebar:
    menu_option = pages.sidebar()

# Page 1: Home
if menu_option == 'Home':
    pages.page_home()
        
# -------------------------------
# 2.- Education
#if menu_option == 'Education':
#    pages.page_education()

# -------------------------------
# 3.- Skills
if menu_option == 'Skills':
    pages.page_skills()
            
# -------------------------------
# 4.- Proyectos
if menu_option == 'Projects':
    pages.page_proyects()

# -------------------------------
#  5.- Contact
if menu_option == 'Contact me':
    pages.page_contact()
        
        
pages.bottom_page()
    