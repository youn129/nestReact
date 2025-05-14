# 연습용입니다.

# import os
# from dotenv import load_dotenv
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import urllib.request

# load_dotenv(dotenv_path='../../.env')

# username = os.getenv('INSTA_USERNAME')
# password = os.getenv('INSTA_PASSWORD')

# try:
#     # Chrome 드라이버 실행
#     driver = webdriver.Chrome()
#     driver.get('https://instagram.com')
#     print("Instagram 페이지 로드 완료")

#     time.sleep(3)

#     # 로그인
#     print("로그인 시도 중...")
#     driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys(username)
#     password_field = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
#     password_field.send_keys(password)
#     password_field.send_keys(Keys.ENTER)
#     print("로그인 완료")

#     # 해시태그 페이지로 이동
#     time.sleep(3)  # 로그인 후 대기
#     driver.get('https://www.instagram.com/explore/search/keyword/?q=%23%EB%94%B8%EA%B8%B0')
#     print("해시태그 페이지로 이동 완료")

#     # 첫 번째 사진 클릭
#     wait = WebDriverWait(driver, 10)  # 최대 10초 대기
#     first_post = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '._aagv')))
#     print("첫 번째 게시물 클릭 준비 중...")
#     ActionChains(driver).move_to_element(first_post).click().perform()
#     print("첫 번째 게시물 클릭 완료")

#     # 페이지 로드 대기
#     time.sleep(3)

#     # 반복적으로 이미지 저장 및 다음 버튼 클릭
#     for i in range(1, 6):  # 최대 5개의 게시물 처리
#         try:
#             # 현재 게시물의 이미지 요소 가져오기
#             print(f"게시물 {i}의 이미지 URL 가져오는 중...")
#             image_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'article img')))
#             이미지 = image_element.get_attribute('src')
#             print(f"이미지 URL: {이미지}")

#             # 이미지 저장
#             print(f"이미지 저장 중... ({i}.jpg)")
#             urllib.request.urlretrieve(이미지, f'{i}.jpg')
#             print(f"이미지 저장 완료: {i}.jpg")

#             # 다음 버튼 클릭
#             print("다음 버튼 클릭 중...")
#             next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[aria-label="다음"]')))
#             ActionChains(driver).move_to_element(next_button).click().perform()
#             print("다음 버튼 클릭 완료")

#             # 페이지 로드 대기
#             time.sleep(3)

#         except Exception as e:
#             print(f"오류 발생: {e}")
#             break

#     print("이미지 저장 및 탐색 완료")

# except Exception as e:
#     print(f"오류 발생: {e}")

# finally:
#     # 브라우저 종료
#     print("브라우저 종료 중...")
#     driver.quit()
