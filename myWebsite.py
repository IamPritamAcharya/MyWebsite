import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from PIL import Image
from pathlib import Path
from blog_content import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.set_page_config(page_title="Pritam's Site", page_icon=":crown:", layout="wide")
local_css("style//main.css")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json

# Social Media

SOCIAL_MEDIA = {
    "LinkdIn" : "https://www.linkedin.com/in/pritamacharya/",
    "Instagram" : "https://www.instagram.com/pritam.ach/",
    "Youtube" : "https://youtu.be/dQw4w9WgXcQ?si=LRDaAUPKqSn7LUKW"

}

# load assets

lottie_coding1 = "https://lottie.host/f0c38411-abd4-4505-9a4d-bf70edb3d427/Fkd1l6X76S.json"
lottie_coding2 = "https://lottie.host/64988bfe-440e-4bf5-80af-c31cb9aa295c/6F4BBMhmJx.json"
contactMe = "https://lottie.host/e968c2ab-014a-4a8c-abac-af4617552995/FzLOB6vOM9.json"
educationCss = "https://lottie.host/7984ef8b-58aa-4051-84c8-646128586dba/TLLFCTcNcy.json"
achivementsCss = "https://lottie.host/8093e3f7-478f-4692-8ee6-2458d5343db0/A20PtOqlhY.json"

project1 = Image.open("temp1.png")
project2 = Image.open("temp2.png")
project3 = Image.open("temp3.png")
pfp = Image.open("pfp.png")
achivements1 = Image.open("certiSE.png")

# bar
# Navigation bar
selected = option_menu(
    menu_title=None,
    options=["Home", "Blogs", "Contact"],
    icons=["house", "book", "envelope"],
    orientation="horizontal"
)

# HOME
#-------------------------------------------------------------------------------------------------------------

if selected == "Home":
    st.write("---")
    # Header
    col1, col2, col3 = st.columns((0.5,1,2))
    with col3:
        a1,a2,a3 = st.columns((1,1.3,1))
        with a2:
            st.markdown("<h1 style='font-size:18px; color:#d0d7fe;'>Hello, I'm 👋</h1>", unsafe_allow_html=True)
        b1,b2,b3 = st.columns((0.7,7,0.7))
        with b2:
            st.markdown("<h1 style='font-size:60px; color:#d0d7fe;'>Pritam Acharya</h1>", unsafe_allow_html=True)
        c1,c2,c3 = st.columns((1,2.6,1))
        with c2:
            st.markdown("<h1 style='font-size:30px; color:#68658c;'>AI/ML Enthusiast</h1>", unsafe_allow_html=True)

        st.write("#")
        cols = st.columns(len(SOCIAL_MEDIA))   
        for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
            cols[index].write(f"[{platform}]({link})")
        
        
            
    with col2:
        st.image(pfp, width=280)
    st.write("##")
        

    # What i Do
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            
            st.write(
                """
                Hey there! I'm Pritam Acharya, and I believe in getting things done efficiently and ahead of schedule whenever possible. My interest in computer science, especially AI/ML, comes from a genuine curiosity about how technology can make the world better.

I'm pretty good with Python and Java, and I know my way around C and C#. But honestly, I'm always learning and trying to get better.

In my free time, you'll find me watching anime, playing Valorant, or getting lost in a good book. I'm a bit of an introvert, not the best at small talk, but I'm always up for a deep conversation.

I love exploring new stuff, whether it's libraries in programming or the latest binge-worthy series. My favorite movie is "[The Theory of Everything](https://en.wikipedia.org/wiki/The_Theory_of_Everything_(2014_film))," and there's this song called "[Machine Learning](https://youtu.be/Y5x8xvDnLXk?si=sJZVVSxNl9H5Qo2w)" by J.maya that I really dig.

So yeah, that's me—just a guy who's passionate about tech, enjoys his hobbies, and tries to keep things simple.
                """
            )
            st.write("##")
        
        with right_column:
            st_lottie(lottie_coding1, height=450, key="coding")

    with st.container():
        st.write("---")
        coll1, coll2, coll3 = st.columns((2,2,1))

        with coll2:
            st.markdown("<h1 style='font-size:45px; color:#8363ac;'>Education</h1>", unsafe_allow_html=True)
        
        c0l1, c0l2 = st.columns(2)
        with c0l1:
            st_lottie(educationCss, height = 350, key = "education")
        with c0l2:
            st.write("#")
            st.write("#")
            st.write("#")
            st.write(
                """
                · Secured 96.6% in 10th grade examinations from Kendriya Vidyalaya Nayagarh.\n
                · Achieved 89% in 12th grade examinations from Kendriya Vidyalaya Nayagarh.\n
                · Currently a fresher at IGIT Sarang with a CGPA of 9.7.
                """
            )
        st.write("#")


    with st.container():
        st.write("---")
        st.markdown("<h1 style='font-size:45px; color:#a378db;'>My Standout Projects</h1>", unsafe_allow_html=True)
        st.write("In total I have 12 Projects. You can view all of them on my LinkdIn ([Click here](https://www.linkedin.com/in/pritamacharya/)).")
        image_column, text_column = st.columns((1,2))

        with image_column:
            st.image(project1)
        with text_column:
            st.header("[Image to Music Converter using AI/ML](https://drive.google.com/file/d/1t45GsVHsmTA4kN14FUeCF9W5zqQ4eVJR/view?usp=sharing)")
            st.write(
            """
                Utilizing cutting-edge transformer models, this project converts images into musical compositions. Leveraging computer vision and natural language processing, it generates musical sequences based on the content extracted from uploaded images. The process involves image captioning to extract semantic meaning, which then serves as a prompt for the music generation model after being processed by another gpt which generates the prompt for the music generation model. The resulting audio compositions offer a unique fusion of visual and auditory experiences.
            """)

    with st.container():
        image_column, text_column = st.columns((1,2))

        with image_column:
            st.image(project2)
        with text_column:
            st.header("[DinoGame](https://drive.google.com/file/d/1t45GsVHsmTA4kN14FUeCF9W5zqQ4eVJR/view?usp=sharing)")
            st.write(
            """
                An aesthetic version of the Chrome Dinosaur Game.
            """)
            st.markdown("[Download Game](https://drive.google.com/file/d/1lcH2s97iktHTUyFN1eFeITREM5Hh7Aim/view?usp=sharing)")

    with st.container():
        image_column, text_column = st.columns((1,2))

        with image_column:
            st.image(project3)
        with text_column:
            st.header("[AI-Powered Rap Generator](https://drive.google.com/file/d/1arQQpG2mzO1zxLomAwlKrtwW5k3kPBYq/view?usp=sharing)")
            st.write(
            """
                This is a cutting-edge Python script designed to revolutionize the world of rap music through the power of artificial intelligence. Here's a breakdown of its functionality:
It reads a lyric provided by the user from a txt file. The text is reorganized and by using a pre trained model it converts the text to speech which sounds like rap due to the reorganization. It's a simple yet creative project.
            """)
    st.write("#")
    st.write("#")

    with st.container():
        st.write("---")
        coll1, coll2, coll3 = st.columns((2,2.25,1))

        with coll2:
            st.markdown("<h1 style='font-size:45px; color:#8386bd;'>Achievements</h1>", unsafe_allow_html=True)
        with coll1:
            st.empty()
        with coll3:
            st.empty()
        left_column,middle_column, right_column = st.columns((1,1,1))
        with left_column:
            
            #st.image(achivements1)
            st_lottie(achivementsCss, height=450, key="achivement1")
            st.write("##")
        
        with middle_column:
            st.write("#")
            st.image(achivements1)
            st.write("Software Intern Certificate from HackerRank [(for more)](https://www.linkedin.com/in/pritamacharya/)")
            st.write("---")
            
            
    
        with right_column:
            st_lottie(achivementsCss, height=450, key="achivement2")
        st.write("#")
        st.write("---")
        
    
#-------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------


# BLOGS
#-------------------------------------------------------------------------------------------------------------
if selected == "Blogs":
    st.write("---")
    st_lottie(lottie_coding2, height=130, key="coding")

    blog_titles = list(blogs.keys())
    selected_blog = st.selectbox("Select a blog", blog_titles)
    
    if selected_blog:
        blog = blogs[selected_blog]
        st.write(blog["content"])
        st.image(blog["image"], use_column_width=True)

#-------------------------------------------------------------------------------------------------------------

# CONTACT
contact_form = """
<form action="https://formsubmit.co/pritamach.exe@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your Name" required>
    <textarea name="message" placeholder="Your Message here"></textarea>
    <button type="submit">Send</button>
</form>
"""
if selected == "Contact":
    local_css("style//style.css")
    st.write("---")


    c1, c2, c3 = st.columns((0.5,2,0.5))
    with c2:
        x1, x2, x3 = st.columns((1,1.8,1))
        with x2:
            st.header("Get In Touch With Me!")
            st.write("##")
        st.write("Email: pritamach.exe@gmail.com")
        st.write("#")
        st.markdown(contact_form, unsafe_allow_html=True)
        st_lottie(contactMe, height=450, key="contact")
    with c1:
        st.empty()
    with c3:
        st.empty()
