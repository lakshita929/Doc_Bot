import sys

sys.path.insert(0, './')

from tests.test_factory import TEST_BUNDLE

from docbot.config.config import CONFIG
from docbot.code.backend.llm import LLM
from docbot.code.backend.db import EMBEDDING_DB

conf = CONFIG()
db_conf = conf.embedding_db
llm_conf = conf.llm

db = EMBEDDING_DB(db_conf)

kb = db.get_knowledgebase('test_db')

test_bundle = TEST_BUNDLE('llm_test_bundle')

llm = LLM(llm_conf)

llm.chat_session(db, kb)