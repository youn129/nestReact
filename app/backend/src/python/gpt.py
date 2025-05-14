# 연습용입니다

# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# # .env 파일에서 환경 변수 로드
# load_dotenv(dotenv_path="../../../.env")

# # 환경 변수에서 API 키 가져오기
# api_key = os.getenv("OPENAI_API_KEY")

# # OpenAI 클라이언트 초기화
# client = OpenAI(api_key=api_key)

# # Chat Completion 생성

# try:
#     response = client.images.generate(
#     model="dall-e-3",
#     prompt="pixel art of a 2d game character sprite",
#     size="1024x1024",
#     quality="standard",
#     n=1,
# )
#     # 결과 출력
#     print(response.data[0].url)
# except Exception as e:
#     print(f"An error occurred: {e}")