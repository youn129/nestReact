# 연습용입니다

# import os
# from dotenv import load_dotenv
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# import pyperclip
# from selenium.webdriver.chrome.options import Options

# load_dotenv(dotenv_path='../../.env')

# userId = os.getenv('NAVER_ID')
# userPw = os.getenv('NAVER_PW')

# 옵션 = Options()
# 옵션.add_argument(r'user-data-dir=C:\Users\user\AppData\Local\Google\Chrome\User Data\Default')

# driver = webdriver.Chrome(options=옵션)
# driver.get('https://nid.naver.com/nidlogin.login?svctype=262144')
# print("네이버 로그인 페이지가 열렸습니다.")

# time.sleep(2)

# pyperclip.copy(userId)
# driver.find_element(By.CSS_SELECTOR, '#id').send_keys(Keys.CONTROL, 'v')

# time.sleep(1)

# pyperclip.copy(userPw)
# driver.find_element(By.CSS_SELECTOR, '#pw').send_keys(Keys.CONTROL, 'v')

# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR, '#pw').send_keys(Keys.ENTER)

# time.sleep(2)
# driver.get('https://m.blog.naver.com/FeedList.naver')
# time.sleep(1.5)
# driver.get('https://blog.editor.naver.com/editor?deviceType=mobile&returnUrl=https%3A%2F%2Fm.blog.naver.com%2FGoWriteForm.naver')

# time.sleep(1.5)
# driver.find_element(By.CSS_SELECTOR, '.documentTitle_blog .se_textarea').send_keys('테스트용_ 블로그 제목입니다.')

# driver.find_element(By.CSS_SELECTOR, '.se_sectionArea .se_editable').send_keys('테스트용_ 블로그 내용입니다. \n 파이썬으로 댓글봇 연습중입니다.') 
# # 브라우저 유지
# try:
#     input("작업을 완료한 후 Enter를 눌러 브라우저를 닫으세요...")
# finally:
#     # 브라우저 종료
#     print("브라우저를 닫습니다.")
#     driver.quit()