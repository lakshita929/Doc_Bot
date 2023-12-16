from docbot.utils import ARXIV
from docbot.config import CONFIG
from docbot.code.frontend.pages.home import MAIN_UI

import streamlit as st
from streamlit_extras.switch_page_button import switch_page


if __name__ == "__main__":
    config = CONFIG()

    arxiv = ARXIV(config)
    
    def search_helper(searchterm):
        results = arxiv.search(searchterm)
        paper_titles = [result.title for result in results]
        return paper_titles if searchterm else []

    def nav_helper(key):
        selection = st.session_state[key]
        print('Selected Page : ', selection)
        switch_page(selection)
        
    def card_helper():
        print('Clicked Card')
    
    main_ui = MAIN_UI(search_helper, nav_helper, card_helper)
    main_ui()