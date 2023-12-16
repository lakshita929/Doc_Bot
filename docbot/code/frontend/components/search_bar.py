from .component import COMPONENT

from streamlit_searchbox import st_searchbox


class SEARCH_BOX(COMPONENT):
    def __init__(self, search_helper):
        super(SEARCH_BOX, self).__init__(search_helper)

    def __call__(self):
        result = st_searchbox(
            self.callback,
            key="arxiv_searchbox"
        )
        
        return result