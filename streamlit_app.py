import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.colored_header import colored_header
from streamlit_extras.grid import grid
from streamlit_option_menu import option_menu
from streamlit_toggle import st_toggle_switch

import pandas as pd
import numpy as np

import os
import requests
import json


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
    
# Create menu and friendly welcome on sidebar
# The menu contains 3 options: HOme - Proyects - Contact me
    
with st.sidebar:
    # Header
    colored_header(
        label=("My Portfolio"),
        description='',
        color_name="blue-green-70")
    
    # Horizontal menu
    menu_option = option_menu(None, ["Home", "Proyects", "Contact me"],
                            icons=['house-fill', 'bar-chart-fill', 'send-fill'],
                            menu_icon="cast", default_index=0, orientation="vertical",
                            styles={
                                "container": {"padding": "0!important", "background-color": "#fafafa"},
                                "icon": {"color": "orange", "font-size": "25px"},
                                "nav-link": {"font-size": "17px", "text-align": "left", "margin": "10px", "--hover-color": "#fffff"},
                                "nav-link-selected": {"background-color": "black"},
                            })
    

# Page 1: Home
if menu_option == 'Home':
    def home_page():
        # 1.- Brief about me
        colored_header(
            label=("Hi, I'm Bastián Barraza👋"),
            description='A Data Analytics Freelancer and data lover.',
            color_name="blue-green-70")
        
        
        st.markdown('Brief about me')
        
        # --------------------
        # 2.- Skills
        
        # Create a container to organize content using 
        # Streamlit's container feature
        with st.container():
            st.markdown('### ⚒️ Skills')
            col1, col2, col3 = st.columns([1, 1, 1])
            
            # Display python logo in first column, first row
            with col1:
                open_lottie('python-2.json', 'python')
                with st.expander(""):
                    st.write("asd")
                    
            # Display R logo in second column, first row
            with col2:
                open_lottie('r-5.json', 'r')
                with st.expander(""):
                    st.write("asd")
            
            # Display tableau logo in third column, first row
            with col3:
                open_lottie('tableau.json', 'tableau')
                with st.expander(""):
                    st.write("asd")
                    
            # Display mysql logo in first column, second row
            with col1:
                open_lottie('mysql.json', 'mysql')
                with st.expander(""):
                    st.write("asd")
            
            # Display excel logo in second column, second row
            with col2:
                open_lottie('microsoft-excel.json', 'excel')
                with st.expander(""):
                    st.write("asd")
                    
            # Display github logo in third column, second row
            with col3:
                open_lottie('github.json', 'github')
                with st.expander(""):
                    st.write("asd")
                    
        
        # --------------------
        # 3.- Courses
        
        
        # --------------------
        # 4.- Proyectos: Short Cut
        
        
        # --------------------
        #  5.- Contact: Shortcut
        
        
    home_page()
    