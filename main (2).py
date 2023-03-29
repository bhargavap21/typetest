import streamlit as st
from st_pages import Page, show_pages, add_page_title
from streamlit_extras.app_logo import add_logo

show_pages(
    [
        Page("main.py", "Information", "🏠"),
        Page("TypingTest.py", "Typing Test", "💻")

    ]
)
from PIL import Image

image = Image.open('logo-color.png')
st.image(image, use_column_width= True )
st.title("TypeTest")
st.header("Description")
st.write("""
TypeTest is a free online platform designed for users who want to test and improve their typing skills. The website offers various typing tests ranging from 1 to 10 minutes with different difficulty levels and typing styles, including standard text, code, and passages from famous literature.

TypeTest's interface is user-friendly and straightforward, providing users with real-time feedback on their typing speed, accuracy, and words per minute (WPM) as they type. The website's statistics allow users to track their progress and identify areas for improvement.

Additionally, TypeTest provides users with practice exercises to help them develop their typing skills further. These exercises have adjustable settings such as word length, complexity, and speed, providing users with a personalized typing experience. Users can also upload their own text to practice typing on content that interests them.

TypeTest offers users the option to compete with others globally, providing users with an opportunity to compare their typing speed and accuracy with others. Additionally, the website provides a leaderboard where users can track their progress against other users.

In summary, TypeTest offers an effective and enjoyable platform for users who want to improve their typing skills, with its varied typing tests, personalized practice exercises, and global competition features.
""")
