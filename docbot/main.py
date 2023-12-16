from thefuzz import thefuzz

from docbot.config.config import CONFIG
from docbot.utils.pdf_reader import EXTRACT
from docbot.utils.arxiv_search import ARXIV


class DOCBOT:
    def __init__(self):
        self.config = CONFIG()
        self.arxiv_interface = ARXIV(self.config)
        self.pdf_reader = EXTRACT(self.config)
        self.embedding_db = EMBEDDING_DB(self.config)
        self.llm = LLM(self.config)
        
    def _search_and_download(self, paper_title):
        possible_papers = [i.title for i in self.arxiv_interface.search(paper_title)]
        selected_paper = 0
                
        for i, paper in enumerate(possible_papers):
            score = fuzz.token_sort_ratio(paper.lower(), paper_title.lower())
            if score > 95:
                selected_paper = i
                
        print('Are you looking for any of these papers?')
        # TODO : Get User Selection from interface and download that paper
        
        save_path = self.arxiv_interface.download(possible_papers[selected_paper])
        
        return save_path
        
    def run(self, paper_path='', paper_title=''):
        if len(paper_path) == 0 and len(paper_title) == 0:
            print('Please provide a paper path or paper title')
            return
        
        if len(paper_path) > 0:
            paper_text = self.pdf_reader.extract_text(paper_path)
        elif len(paper_title) > 0:
            # Search on arxiv and download the paper
            save_path = self._search_and_download(paper_title)
            
            # Extract the pdf text and the references and download each reference 
            # and save the pdfs and extract their texts as well to create the knowledge base
            
            paper_txt = self.pdf_reader.extract_text(save_path)
        
        # TODO : Add to knowledge base
        # self.embedding_db.add(paper_txt)
        
        references = self.pdf_reader.extract_references(paper_txt)
                
        for reference in references:
            save_path = self._search_and_download(reference)
            txt = self.pdf_reader.extract_text(save_path)
            self.embedding_db.add(txt)