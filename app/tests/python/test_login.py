import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os

load_dotenv()

KAKAO_ID = os.getenv("KAKAO_ID")
KAKAO_PW = os.getenv("KAKAO_PW")

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    time.sleep(3)
    driver.quit()

def test_saramin_login_button(driver):
    driver.get("https://www.saramin.co.kr")
    time.sleep(2)

    login_button = driver.find_element(By.CSS_SELECTOR, 'a.btn_sign.signin')
    assert login_button.is_displayed(), "로그인 버튼이 존재하지 않습니다."
    login_button.click()
    time.sleep(2)

    # 로그인 페이지로 전환되었는지 확인
    assert "auth" in driver.current_url or "login" in driver.current_url

    kakao_login_btn = driver.find_element(By.CSS_SELECTOR, "li.login_kakao a")
    assert kakao_login_btn.is_displayed(), "카카오톡 로그인 버튼이 존재하지 않습니다."
    kakao_login_btn.click()
    time.sleep(3)  # 카카오 인증창이 팝업으로 뜸뜸

    main_window = driver.current_window_handle
    for handle in driver.window_handles:
        if handle != main_window:
            driver.switch_to.window(handle)
            break

    driver.find_element(By.ID, "loginId--1").send_keys(KAKAO_ID)
    time.sleep(0.5)
    driver.find_element(By.ID, "password--2").send_keys(KAKAO_PW)
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, "button.btn_g.highlight.submit").click()
    time.sleep(5)

    # 메인창으로 다시 포커스 전환
    driver.switch_to.window(main_window)
    time.sleep(5)

    # 이력서/자소서 메뉴 클릭
    resume_menu = driver.find_element(By.XPATH, '//span[contains(text(), "이력서/자소서")]')
    resume_menu.click()
    time.sleep(5)

    # 스크롤 내려서 하단 이력서 클릭릭
    scroll_attempts = 0
    found = False
    target_text = "신입 QA Engineer 정윤식"

    while scroll_attempts < 5:
        links = driver.find_elements(By.CSS_SELECTOR, 'a.tit.btn_action span')
        for span in links:
            if target_text in span.text:
                actions = ActionChains(driver)
                actions.move_to_element(span).perform()
                time.sleep(0.5)
                span.click()
                found = True
                break
        if found:
            break

        for _ in range(5):
            driver.execute_script("window.scrollBy(0, 300);")
            time.sleep(0.5) 

        scroll_attempts += 1
