from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
#Finad emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage",page_icon=":tada:",layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_3rwasyjy.json")
img_contact_form = Image.open("images\channel.jpg")
#--- HEADER SECTION ---
with st.container():
    st.subheader("Hi, I am Vinay :wave:")
    st.title("Automation Specialist")
    st.write("I am passionate about finding ways to use Python and VBA to be more efficient and effective. ")
    st.write("[Learn More](https://www.codewithharry.com)")
# WHAT I DO
with st.container():
    st.write("---")
    left_coloumn, right_coloumn = st.columns(2)
    with left_coloumn:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I am a Youtuber creating new videos for people based on programming knowledge on python!!!
            The Key points to note are:
           - 1: Code Everyday.
           - 2: Write It Out.
           - 3: Go Interactive!.
           - Make sure you type your first program and be happy which is:.
            print("Hello, World)
           - Thank me Later!!
           - Make sure to subscribe and click on the bell icon for the notifications
            """)
        st.write("[Youtube Channel](https://www.youtube.com/channel/UCh8AtA82MJgjhJY-fpqVvVQ)")
        st.write("[My website](http://kvkmasters.ezyro.com/)")


with right_coloumn:
    st_lottie(lottie_coding, height=300, key="coding")
with st.container():
    st.write("---")
    st.header("My Channel")
    st.write("##")
    image_column, text_column=st.columns((1,2))
with image_column:
    st.image(img_contact_form)

with text_column:
    st.subheader("Channel Intro")
    st.write(
        """
        This is My Channel logo and link is down below!!
        I would Try my level best to make you happy and satisfied with my content
        Hope you will love my content and support me in this journey!!!
        Thank You
        """
    )
    st.markdown("[Click Here!!!](https://www.youtube.com/channel/UCh8AtA82MJgjhJY-fpqVvVQ)")   

