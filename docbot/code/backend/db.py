import chromadb
from .embedder import GPT4EMBEDDER


class EMBEDDING_DB:
    def __init__(self, config):
        self.config = config
        self.client = chromadb.PersistentClient(path=self.config.db_save_path)
        self.embedding_function = GPT4EMBEDDER()
        
    def get_knowledgebase(self, base_name=''):
        knowledge_base = self.client.get_or_create_collection(
                                name=base_name, 
                                embedding_function=self.embedding_function,
                                metadata={
                                    "hnsw:space" : self.config.distance_method
                                }
                            )
        return knowledge_base
    
    def get_kb_info(self, knowledge_base):
        kb_items = knowledge_base.peek()
        kb_count = knowledge_base.count()
        
        return kb_count, kb_items
        
    def add_document(self, knowledge_base, doc_text, metadata={}):
        kb_count, _ = self.get_kb_info(knowledge_base)
        
        unique_id = f'{knowledge_base.name}_doc_{kb_count+1}'
        
        if len(metadata.keys()) > 0:
            knowledge_base.add(
                documents=[doc_text],
                ids=[unique_id],
                metadatas=[metadata]
            )
        else:
            knowledge_base.add(
                documents=[doc_text],
                ids=[unique_id]
            )
        
    def add_multiple_docs(self, knowledge_base, docs, metadatas=[]):
        for i, doc in enumerate(docs):
            metadata = {}
            if len(metadatas) > 0:
                if type(metadatas[i]) == dict and len(metadatas[i].keys()) > 0:
                    metadata = metadatas[i]

            self.add_document(knowledge_base, doc, metadata)
            
    def update_or_insert(self, knowledge_base, doc_id, doc_text='', metadata='', unique_id=''):
        return
    
    def query(self, knowledge_base, query_text='', where={}, where_doc={}):
        results = knowledge_base.query(
            query_texts=[query_text],
            n_results=self.config.max_results,
            where=where,
            where_document=where_doc
        )
        
        print('Results : ')
        print(results)
        result_text = '\n\n'.join([i for i in results['documents'][0]])
        # TODO : Extract only the necessary parts from the results to be passed to the LLMs
        return result_text
    
    def get_document(self, knowledge_base, doc_id, where={}, where_doc={}):
        results = knowledge_base.get(
            ids=[doc_id],
            where=where,
            where_doc=where_doc
        )
        
        return results
    
