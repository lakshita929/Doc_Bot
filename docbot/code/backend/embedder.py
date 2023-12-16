import numpy as np
from gpt4all import GPT4All, Embed4All
from chromadb import Documents, EmbeddingFunction, Embeddings

class GPT4EMBEDDER(EmbeddingFunction):
    def __init__(self):
        super(GPT4EMBEDDER, self).__init__()
        self.embedder = Embed4All()
        
    def __call__(self, input: Documents) -> Embeddings:
        embeddings = []
        for i in input:
            embedding = self.embedder.embed(i)
            embeddings.append(embedding)
            
        return embeddings