import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.colored_header import colored_header
from streamlit_option_menu import option_menu

import pandas as pd
import numpy as np

import json
import requests

from Codes import constant
    
def open_lottie(raw_url, key, height= 120, width = 120):
    """
    Function to open and display an lottie file saved
    as json in lottie_files directory.
    """
    
    # Send an HTTP GET request to the provided raw URL on GitHub
    response = requests.get(raw_url)
        
    # Load the JSON data
    lottie_data = response.json()
            
            
    # Display lottie fig
    st_lottie(lottie_data, 
        height=height, 
        width=width, 
        speed=0.8, 
        loop=True, 
        quality='high', 
        key=key
    )

def social_icons(width=24, height=24, **kwargs):
        icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 20px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

        icons_html = ""
        for name, url in kwargs.items():
            icon_src = {
                "linkedin": "https://img.icons8.com/ios-filled/100/ff8c00/linkedin.png",
                "github": "https://img.icons8.com/ios-filled/100/ff8c00/github--v2.png",
                "email": "https://img.icons8.com/ios-filled/100/ff8c00/filled-message.png",
                "upwork": "https://img.icons8.com/ios/50/upwork.png"
            }.get(name.lower())

            if icon_src:
                icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

        return icons_html
    
    
# ------------------------
# 0.- Create sidebar
def sidebar():
    colored_header(
    label=(f"Unlock Success with Data Insights and Statistics."),
    description='',
    color_name="blue-green-10")
    
    # Horizontal menu
    menu_option = option_menu(None, ["Home", "Skills", "Projects", "Contact me"],
                            icons=['house-fill', 'bar-chart-fill', 'folder-fill', 'send-fill'],
                            menu_icon="cast", default_index=0, orientation="vertical",
                            styles={
                                "container": {"padding": "0!important", "background-color": "#fafafa"},
                                "icon": {"color": "orange", "font-size": "25px"},
                                "nav-link": {"font-size": "17px", "text-align": "left", "margin": "10px", "--hover-color": "#fffff"},
                                "nav-link-selected": {"background-color": "black"},
                            })
    
    # Url linked with logos
    linkedin_url = "https://www.linkedin.com/in/bastianbarrazam/"
    github_url = "https://github.com/bastianbm7"
    email_url = f"mailto:bastian.bm712@gmail.com"
    upwork_url = "https://www.upwork.com/freelancers/bastianb"
    with st.container():
        
        col1, col2, col3, col4 = st.columns([0.4,0.4,0.4,1])
        col1.markdown(
                social_icons(30, 30, upwork=upwork_url),
                unsafe_allow_html=True)
        col2.markdown(
                social_icons(30, 30, linkedin=linkedin_url),
                unsafe_allow_html=True)
        col3.markdown(
                social_icons(30, 30, GitHub=github_url),
                unsafe_allow_html=True)
        col4.markdown(
                social_icons(30, 30, Email=email_url),
                unsafe_allow_html=True)
        
        
    return menu_option
# ------------------------
# 1- Create Home Page
def page_home():
    
    # a.- Greetings
    st.markdown("# Hi, I'm Bastián Barraza👋")
    st.caption(constant.info["Intro"])
    st.divider()

    # Create a column with about me text and 
    # a gif from lottiefile.
    col1, col2 = st.columns(2)
    col1.markdown(constant.info["About"])
    
    # Lottie file
    with col2:
        open_lottie('https://raw.githubusercontent.com/bastianbm7/portfolio_page/main/lottie_files/statistics.json', 'stats', 300, 350)
        

# ------------------------
# 2- Create Education page
# def page_education():
    
    # Header
#    st.markdown('# Education')


# ------------------------
# 3- Create Education page
def page_skills():

    # Header
    st.markdown('# ⚒️ Skills')
    st.divider()
    
    # Create a container to organize content using 
    # Streamlit's container feature    
    with st.container():
        
        # In each skills, a column for title and
        # text is created, and a column for the logo too.
        
        # Each text is on constant.py file 
        # in Codes folder
        
        # -----------
        # a) Python
        col1, col2= st.columns(2)
        
        # Text in column 1
        col1.markdown(constant.skills["Python"])     
        # Lottie file in column 2
        with col2:
            open_lottie('https://raw.githubusercontent.com/bastianbm7/portfolio_page/main/lottie_files/python-2.json', 'python', 250, 250)
        
        st.divider()
        
        
        # -----------
        # b) R
        col1, col2= st.columns(2)
        
        # Text in column 1
        col1.markdown(constant.skills["R"])     
        
        # Lottie file in column 2
        with col2:
            open_lottie('https://raw.githubusercontent.com/bastianbm7/portfolio_page/main/lottie_files/r-5.json', 'r', 250, 250)
        
        st.divider()
        
        
        # -----------
        # c) Tableau
        col1, col2= st.columns(2)
        
        # Text in column 1
        col1.markdown(constant.skills["Tableau"])     
        # Lottie file in column 2
        with col2:
            open_lottie('https://raw.githubusercontent.com/bastianbm7/portfolio_page/main/lottie_files/tableau.json', 'tableau', 250, 250)
        
        st.divider()
        
        # -----------
        # d) MySQL
        col1, col2= st.columns(2)
        
        # Text in column 1
        col1.markdown(constant.skills["Mysql"])     
        # Lottie file in column 2
        with col2:
            open_lottie('https://raw.githubusercontent.com/bastianbm7/portfolio_page/main/lottie_files/mysql.json', 'mysql', 250, 250)
        
        st.divider()

        # -----------
        # e) GitHub
        col1, col2= st.columns(2)
        
        # Text in column 1
        col1.markdown(constant.skills["Github"])     
        # Lottie file in column 2
        with col2:
            open_lottie('https://raw.githubusercontent.com/bastianbm7/portfolio_page/main/lottie_files/github.json', 'github', 250, 250)
            
        st.divider()
        
        # -----------
        # f) Excel
        col1, col2= st.columns(2)
        
        # Text in column 1
        col1.markdown(constant.skills["Excel"])     
        # Lottie file in column 2
        with col2:
            open_lottie('https://raw.githubusercontent.com/bastianbm7/portfolio_page/main/lottie_files/microsoft-excel.json', 'excel', 250, 250)
        
        
# ------------------------
# 4- Create proyects page
def page_proyects():
    
    def create_bottom_4columns(link, col1_text, col2_text, col3_text):
        
        """
        This function is used to create a columns with specific
        topics of the project and the link to github
        """
        
        # Create 4 columns 
        col1, col2, col3, col4 = st.columns([1,1,1,0.3])
        
        # Column 1 text
        col1.markdown(col1_text)
        
        # Column 2 text
        col2.markdown(col2_text)
        
        # Column 3 text
        col3.markdown(col3_text)
        
        # Github symbol with url linked
        col4.markdown(social_icons(35, 35, github=link),
                unsafe_allow_html=True)
        
    # Urls of each project:
    github_handGesture = "https://github.com/bastianbm7/Hand_gesture"
    github_Cluster_Classification = "https://github.com/bastianbm7/Cluster_Classification_Analysis"
    github_Angine = "https://github.com/bastianbm7/Angine_classifier"
    github_Portfolio = "https://github.com/bastianbm7/portfolio_page"
    github_upWork = "https://github.com/bastianbm7/upWork_scrap"
    github_NBA_Viz = "https://github.com/bastianbm7/Shot-Analysis-CAVS2015"
    github_sharks_Game = "https://github.com/bastianbm7/BasketballGame_analysis"
    github_OrangeTelcom = "https://github.com/bastianbm7/OrangeTelcom_classifier"
    github_Resampling = "https://github.com/bastianbm7/jackknife_bootstrap"
    github_Gibbs_Sampling = "https://github.com/bastianbm7/GibssSampling_Bayesian"
    
    # Write Header
    st.markdown('# 📝 Projects')
    
    # Create 3 tabs with the different cathegories of the projects
    tab1, tab2, tab3, tab4 = st.tabs(["Publications", 
                                      "Machine Learning", 
                                "Data Science & Data Analytics", 
                                "University"])
    
    # ---- Publications projects ----
    with tab1:
        st.markdown(constant.projects['Cross_correlation'])
    
    # ---- Machine Learning projects ----
    with tab2:
        #  Hand gesture model ---- 
        
        # Text from constant file
        st.markdown(constant.projects['Hand_Gesture'])
        
        # Create bottom text
        create_bottom_4columns(github_handGesture, 
                               '**Language: English**', 
                               '**Software: Python 3.10**',
                               '**Status: Finished**')
        st.divider()
        
        #  NBA Machine Learning ----
        
        #  Cluster and Classifications analysis ----
        st.markdown(constant.projects['Cluster_Classification'])
        
        # Create bottom text
        create_bottom_4columns(github_Cluster_Classification, 
                               '**Language: English**', 
                               '**Software: Python 3.10**', 
                               '**Status: Finished**')
        st.divider()
        
        #  Angine prediction ----
        st.markdown(constant.projects['Angine'])

        # Create bottom text
        create_bottom_4columns(github_Angine, 
                               '**Language: Spanish**', 
                               '**Software: Python 3.10**', 
                               '**Status: Finished**')
    
    # ---- Data Science & Data Analytics projects ----
    with tab3:
        # Scrap upWork Page ----
        st.markdown(constant.projects['upWork'])
        
        # Create bottom text
        create_bottom_4columns(github_upWork, 
                               '**Language: English**', 
                               '**Software: Python 3.10 - MySQL**',
                               '**Status: Not Finished**')
        st.divider()
        # Portfolio ----
        st.markdown(constant.projects['Portfolio'])

        # Create bottom text
        create_bottom_4columns(github_Portfolio, 
                               '**Language: English**', 
                               '**Software: Python 3.10**',
                               '**Status: Updating**')
        st.divider()
        
        # NBA Vizualization ----
        st.markdown(constant.projects['NBA_Viz'])
        
        # Create bottom text
        create_bottom_4columns(github_NBA_Viz, 
                               '**Language: Spanish**', 
                               '**Software: Python 3.10**',
                               '**Status: Finished**')
        st.divider()
        
        #  Sharks analysis ----
        st.markdown(constant.projects['sharks_Game'])
        
        # Create bottom text
        create_bottom_4columns(github_sharks_Game, 
                               '**Language: Spanish**', 
                               '**Software: Python 3.10**',
                               '**Status: Finished**')
        st.divider()
        
    # ---- University projects ----
    with tab4:
        
        # Orange Telcom ---- 
        st.markdown(constant.projects['OrangeTelcom'])
        
        # Create bottom text
        create_bottom_4columns(github_OrangeTelcom, 
                               '**Language: Spanish**', 
                               '**Software: R 4.2.2**',
                               '**Status: Finished**')
        st.divider()
        
        # Gibbs Sampling ---- 
        st.markdown(constant.projects['Gibbs_Sampling'])

        # Create bottom text
        create_bottom_4columns(github_Gibbs_Sampling, 
                               '**Language: Spanish**', 
                               '**Software: R 4.2.2**',
                               '**Status: Finished**')
        st.divider()
        
        # Jackknife and Bootstrap ---- 
        st.markdown(constant.projects['Resampling'])
        
        # Create bottom text
        create_bottom_4columns(github_Resampling, 
                               '**Language: Spanish**', 
                               '**Software: R 4.2.2**',
                               '**Status: Finished**')

    
# ------------------------
# 4- Create contact me page
def page_contact():
    st.markdown('# 😄 Get in touch with me')
    
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
    col1.markdown(constant.contact['text'])
    col2.markdown(contact_form, unsafe_allow_html=True)
    
    
    
# ------------------------
# 6- Bottom page

def bottom_page():
    
    
    st.divider()
    st.markdown("## <center> Offered Services</center>", unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns(5)
    
    # Write in web scrapping column ----
    with col1:
        # Open lottie file
        open_lottie('https://raw.githubusercontent.com/bastianbm7/portfolio_page/main/lottie_files/web-scrapping.json', 'webscrapping', 80, 80)
        
        # Write title
        st.markdown("**Web Scrapping**")
    
    
    # Write in Data Analyst Process column ----
    with col2:
        # Open lottie file
        open_lottie('https://raw.githubusercontent.com/bastianbm7/portfolio_page/main/lottie_files/data-analyst.json', 'datanalyst', 80, 80)
        
        # Write title
        st.markdown("**Data Analyst Process**")

        
    # Write in Statistical Methods column ----
    with col3:
        # Open lottie file
        open_lottie('https://raw.githubusercontent.com/bastianbm7/portfolio_page/main/lottie_files/stats.json', 'stats2', 80, 80)
        
        # Write title
        st.markdown("**Statistical Methods**")
        
        
    # Write in Machine Learning Services column ----
    with col4:
        # Open lottie file
        open_lottie('https://raw.githubusercontent.com/bastianbm7/portfolio_page/main/lottie_files/machine-learning.json', 'machinelearning', 80, 80)
        
        # Write title
        st.markdown("**Machine Learning Services**")

        
    # Write in Data Vizualization column ----
    with col5:
        # Open lottie file
        open_lottie('https://raw.githubusercontent.com/bastianbm7/portfolio_page/main/lottie_files/data-vizualization.json', 'dataviz', 80, 80)
        
        # Write title
        st.markdown("**Data Vizualization**")
        
