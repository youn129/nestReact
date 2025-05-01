from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv(dotenv_path="../../../.env")

# 환경 변수에서 API 키 가져오기
api_key = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(model='gpt-4o-mini')

loader = WebBaseLoader('https://github.com/facebookresearch/segment-anything-2')
docs = loader.load()

template = ChatPromptTemplate.from_template("""
    질문에 대해서 context 부분을 읽고 답변을 작성해줘:
    context: {context}
    질문: {question}
    답변:                                         
""")

# PyPDFLoader('').load()

chain = template | model | StrOutputParser()
result = chain.invoke({'context' : docs, 'question' : 'SAM2 모델 설치는 어떻게 해야 하나요?'})
print(result)