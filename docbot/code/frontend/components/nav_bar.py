from streamlit_option_menu import option_menu

from .component import COMPONENT


class NAVBAR(COMPONENT):
    def __init__(self, nav_helper):
        super(NAVBAR, self).__init__(nav_helper)
    
    def __call__(self):
        navbar = option_menu(
                                None, 
                                ["Home", "Chat"],
                                icons=['house', 'chat'],
                                on_change=self.callback, 
                                key='nav_menu', 
                                orientation="horizontal"
                            )

        return navbar