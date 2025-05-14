import sys
import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# 경로 설정
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from tests.python.pages.home_page import HomePage

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)

    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://localhost:3000")
    yield driver  # 테스트 함수에게 driver 인스턴스를 넘김
    time.sleep(2)
    driver.quit()

def test_laptop_search(driver):
    home_page = HomePage(driver)
    time.sleep(2)  # 초기 로딩 대기
    home_page.enter_search_query("laptop")
    time.sleep(1)
    home_page.click_search_button()
    time.sleep(3)  # 렌더링 대기

    assert home_page.is_first_result_valid()
