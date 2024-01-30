import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
import json
from PIL import Image

st.set_page_config(page_title="Portfolio", layout="wide")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


#----------------------Add Images Here--------------------------------
svg_file = "homepage.svg"

room_find = Image.open("room_find.png")
udemy_dash = Image.open("udemy_project_thumbnail.jpg")
grasper_app = Image.open("grasper_twitter.png")
f1_frenzy = Image.open("f1_wall.jpg")
scrub_the_strat_slam = Image.open("Scrub-the-strat.png")
la_dash = Image.open("analysis.png")
one_card_pt = Image.open("onecard-credit-card.jpg")
playo_img = Image.open("PlayoApp.jpg")
research_img = Image.open("research.png")


#---------------------------Home Page----------------------------
st.write("##")
st.subheader("Hello World :wave:")
st.title("Welcome to my portfolio")
#st.caption("Bennett'24 | Product Enthusiast")
st.write('----')

with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['About','Product Thinking','Coding Projects'],
        icons = ['person', 'lightbulb', 'code-slash'],
        orientation = 'horizontal'
    )

if selected == 'About':

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.subheader("Yuvraj Saxena")
            st.caption("Bennett'24 | Product Enthusiast")

            st.markdown(
                """
                <div style='display: flex;'>
                    <a style='display: inline-flex; margin-right: 5px; align-items: center; padding: 10px 20px; background-color: #0077B5; color: white; text-decoration: none; border-radius: 5px;' href="https://www.linkedin.com/in/yuvrajsaxena/" target="_blank">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-linkedin" viewBox="0 0 16 16">
                        <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854zm4.943 12.248V6.169H2.542v7.225zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248S2.4 3.226 2.4 3.934c0 .694.521 1.248 1.327 1.248zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016l.016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225z"/>
                        </svg>
                        <span style="margin-left: 5px;">View Linkedin Profile</span>
                    </a>
                    <a style='display: inline-flex; margin-right: 5px; align-items: center; padding: 10px 20px; background-color: #FF6252; color: white; text-decoration: none; border-radius: 5px;' href="https://drive.google.com/file/d/1-eDl0H5lEq5D7y3GKwb5YWzlpaMruOyw/view?usp=drive_link" target="_blank">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-file-earmark-text" viewBox="0 0 16 16">
                        <path d="M5.5 7a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1zM5 9.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5m0 2a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1h-2a.5.5 0 0 1-.5-.5"/>
                        <path d="M9.5 0H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V4.5zm0 1v2A1.5 1.5 0 0 0 11 4.5h2V14a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1z"/>
                        </svg>
                        <span style="margin-left: 5px;">View Resume</span>
                    </a>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col2:
            st.image(svg_file, width=350)

        st.write('---')
        with st.container():
            #col3,col4 = st.columns(2)
            # with col3:
            st.subheader("""
            Education
            - Bennett University
                - Bachelor of Technology -Computer Science
                - Grade: 9.0/10
            """)
            st.subheader("""
            Experience
            - Technical Writer Intern @ Siemens EDA
                - Estimated 30% increase in document access and navigation by editing, and assuring quality for 19+ legacy
                documents, facilitating seamless migration to a unified cloud-based service.
                - Analyzed and integrated information from legacy guides into a new guide in collaboration with the R&D team.
                - Created new content for missing features from legacy documents, enhancing comprehensive documentation.
            - Python Teaching Assistant @ Bennett University
                - Guided over 65 first-year students in weekly lab sessions in course Programming in Python
                - Created weekly tutorials with over 30 questions for course in collaboration with senior faculty
                - Communicated complex technical concepts in an easily understandable way to students, achieved a rating of
                    4.2/5
            """)

#-------------------------------------------Product thinking----------------------------------------------------------------------
if selected == "Product Thinking":
    with st.container():
        st.header("Projects")
        st.write("##")
        col7, col8 = st.columns((1,2))
        with col7:
            st.image(playo_img)
            st.image(f1_frenzy)
            # st.image(scrub_the_strat_slam)
            st.image(room_find)
            # st.image(one_card_pt)
        with col8:
            st.subheader("Product Sense: PlayO")
            st.write("This project is my take on How I would improve my favorite product? Here we discuss why I love PlayO and what are some features I think can improve the app as a whole.")
            st.markdown("[View Project](https://moored-sousaphone-354.notion.site/Favorite-Product-Feature-Suggestion-PlayO-cf1352a7662d4f6f8de7f77b6a992f08?pvs=25)")
            st.write("##")
            st.write("##")
            st.subheader("Product Design: F1 Frenzy")
            st.write("The goal of the project is to go deep into the design of the first iteration or a pre-prototype of an application, define the basis, and develop a mock-up of the app.")
            st.markdown("[View Project](https://moored-sousaphone-354.notion.site/F1-Frenzy-Product-Design-a2e508d7090a4e6783350762f56941ce)")
            st.write("##")
            # st.subheader("Scrub-the-strat-slam: A Jio Creative Labs competition")
            # st.write("The presentation contains our strategy on how we would make dishwashers a household item in India, just like washing machines. This presentation was the submission of stage 1 of the competition conducted by Unstop and Jio Creative Labs.")
            # st.markdown("[View Project](https://moored-sousaphone-354.notion.site/Scrub-the-strat-slam-8773e84a56614bd3beb629cb1583143b)")
            st.write("##")
            st.subheader("Roommate Finder - UI Project")
            st.write("An app to find yourself a roommate. From your hostel to an apartment, a one stop solution to your rent problems. The ui and prototyping was done on Figma.")
            st.markdown("[View Project](https://www.figma.com/file/y4BKjfYOicPBMmRTVMdNdH/Roommate-Finder?type=design&node-id=0%3A1&mode=design&t=i02fwrmNYdtzkPZn-1)")
            # st.subheader("One Card - Product Teardown")
            # st.write("On the way...")
            # #st.markdown("[Figma](https://www.figma.com/file/y4BKjfYOicPBMmRTVMdNdH/Roommate-Finder?type=design&node-id=0%3A1&mode=design&t=i02fwrmNYdtzkPZn-1)")
            # st.write("##")

#-----------------------------------Coding Projects----------------------------------------------------------
if selected == "Coding Projects":
    with st.container():
        st.header("My Projects")
        st.write("##")
        col5, col6 = st.columns((1,2))
        with col5:
            st.image(udemy_dash)
            st.image(la_dash)
            # st.image(research_img)
            st.image(grasper_app)
        with col6:
            st.subheader("Udemy Courses Analysis - Dashboard")
            st.write("A dashboard analysing over 1000 different courses across 4 categories built using Python and Streamlit with filters to easily switch between desired choices.")
            st.markdown("[View Project](https://yuvraj25-30g-udemy-course-analysis-app-4qa22c.streamlit.app/)")
            st.subheader("Los Angeles Crime Data Analysis")
            st.write("This project contains the analysis of the crime data collected by the LAPD converted into dashboards explaining all necessary details.")
            st.markdown("[View Project](https://public.tableau.com/app/profile/yuvraj.saxena/viz/ArrestDataCompleteAnalysis/ArrestsDataAnalytics-1)")
            st.write("##")
            st.write("##")
            # st.subheader("Data Science in Technical SEO")
            # st.write("This paper examines the application of data science methodologies to technical search engine optimization (SEO) in order to enhance website visibility and search engine rankings. We conduct a simulated study using the SEO Sample Data and SEO Crawl Dataset to demonstrate how data science and machine learning can be used to improve the technical aspects of an SEO campaign.")
            # st.markdown("[View Study](https://bennettu-my.sharepoint.com/personal/e20cse307_bennett_edu_in/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fe20cse307%5Fbennett%5Fedu%5Fin%2FDocuments%2FE20CSE307%5FEB15A%5FFull%5FPaper%2Epdf&parent=%2Fpersonal%2Fe20cse307%5Fbennett%5Fedu%5Fin%2FDocuments)")
            st.write("##")
            st.subheader("Grasper - A productivity App")
            st.write("A group project built in my second year following the scrum methodology, this app was developed to improve your productivity using well known techniques available to you in your palm. This app was build using Flutter, Dart and Firebase")
            st.markdown("[Visit Github (Feature)](https://github.com/Yuvraj25-30G/pomodoro_1)")
            # st.write("##")
