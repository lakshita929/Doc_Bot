from .component import COMPONENT

from streamlit_card import card

class CARDS(COMPONENT):
    def __init__(self, card_helper):
        super(CARDS, self).__init__(card_helper)
        
    def __call__(self):
        res = card(
            title="Streamlit Card",
            text="This is a test card",
            styles={
                "card": {
                    "width": "150px",
                    "height": "150px",
                    "border-radius": "20px",
                    "box-shadow": "0 0 10px rgba(0,0,0,0.5)"
                }
            },
            on_click=self.callback
        )