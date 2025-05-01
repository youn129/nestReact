from langchain_openai import ChatOpenAI
import os
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv(dotenv_path="../../../.env")

# 환경 변수에서 API 키 가져오기
api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model='gpt-4o-mini')

template = ChatPromptTemplate.from_messages(
    [
    ('system', '너는 지금부터 영어를 한글로 번역해주는 봇이야'),
    ('human', '{a}')
    ]
)


result = model.invoke(template.format_messages(a='I like kimchi'))
print(result.content)