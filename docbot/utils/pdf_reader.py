import string
from pdfminer.high_level import extract_text

class EXTRACT:
    def __init__(self, config):
        self.config = config
    
    def extract_text(self, pdf_path):
        text = extract_text(pdf_path)
        return text
    
    def extract_references(self, text):
        ref_idx = text.lower().index('references')
        possible_refs = text[ref_idx+len('references')+1:]
        possible_refs = possible_refs.split('[')
        possible_refs = [i[i.index(']')+1:] for i in possible_refs if ']' in i]
        possible_refs = [i.replace('\n', ' ') for i in possible_refs]
        possible_refs = [i.strip() for i in possible_refs]
        possible_refs = [i.translate(str.maketrans('', '', string.punctuation)) for i in possible_refs]
        
        return possible_refs