import time
import pytest
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

# 경로 설정 및 환경 변수 로드
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
load_dotenv()

from tests.python.pages.saramin.login_page import LoginPage
from tests.python.pages.saramin.main_page import MainPage
from tests.python.pages.saramin.resume_page import ResumePage

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

def test_saramin_login_and_resume_open(driver):
    driver.get("https://www.saramin.co.kr")
    time.sleep(2)

    login_page = LoginPage(driver)
    login_page.click_login_button()
    login_page.click_kakao_login_button()
    login_page.switch_to_kakao_popup()
    login_page.enter_kakao_credentials(KAKAO_ID, KAKAO_PW)

    driver.switch_to.window(driver.window_handles[0])
    time.sleep(5)

    main_page = MainPage(driver)
    main_page.click_resume_menu()

    resume_page = ResumePage(driver)
    resume_page.scroll_and_click_target_resume("신입 QA Engineer 정윤식")
