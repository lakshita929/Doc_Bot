import sys

sys.path.insert(0, './')

from tests.test_factory import TEST_BUNDLE

from docbot.config.config import CONFIG
from docbot.code.backend.db import EMBEDDING_DB

conf = CONFIG()
db_conf = conf.embedding_db

db = EMBEDDING_DB(db_conf)

kb = db.get_knowledgebase('test_db')


test_bundle = TEST_BUNDLE('embedding_db_test_bundle')

@test_bundle.add_test(test_name='test_add_single_doc', default_params={'kb': kb, 'doc_text': 'hello world', 'meta': {'type':'greeting'}})
def test_add_doc(kb, doc_text, meta):
    db.add_document(kb, doc_text, meta)
    count, items = db.get_kb_info(kb)
    
    if count > 0:
        return True
    else:
        raise Exception('Could not add document')


@test_bundle.add_test(test_name='test_add_multiple_docs', default_params={'kb': kb, 'docs': ['hello world', 'hello world 2'],'metas': [{'type':'greeting'}, {'type':'greeting'}]})
def test_add_multiple_docs(kb, docs, metas):
    db.add_multiple_docs(kb, docs, metas)
    count, items = db.get_kb_info(kb)
    
    if count > 0:
        return True
    else:
        raise Exception('Could not add document')


@test_bundle.add_test(test_name='test_query', default_params={'kb': kb, 'query_text': '2'})
def test_query(kb, query_text):
    results = db.query(kb, query_text)
    print(results)