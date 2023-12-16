import streamlit as st

from docbot.code.frontend.components import *


class MAIN_UI:
    def __init__(self, search_helper, nav_helper, card_helper):
        self.chat_sessions = CARDS(card_helper)
        self.search_bar = SEARCH_BOX(search_helper)
        self.nav_bar = NAVBAR(nav_helper)
    
    def __call__(self):
        st.title("DocBot🤖")
        nav_bar = self.nav_bar()
        
        st.write("Resume From Previous Sessions : ")
        cards = self.chat_sessions()
        
        st.write("Search for a Research Paper On Arxiv")
        search = self.search_bar()
        
        uploaded_file = st.file_uploader('Upload The Research Paper PDF', type="pdf")
        if uploaded_file is not None:
            print('File Uploaded Successfully')
            st.write('File Uploaded Successfully')
