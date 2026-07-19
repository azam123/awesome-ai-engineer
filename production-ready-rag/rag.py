from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from config import *
llm=ChatOpenAI(model=LLM_MODEL,temperature=0)
p=ChatPromptTemplate.from_template('Context:{context}\nQuestion:{question}')
def ask(db,q):
 docs=db.as_retriever(search_type='mmr',search_kwargs={'k':4}).invoke(q);ctx='\n\n'.join([d.page_content for d in docs]);return (p|llm).invoke({'context':ctx,'question':q}).content
