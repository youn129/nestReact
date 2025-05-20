import sys
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
import os

load_dotenv()

LOCAL = os.getenv("LOCAL")

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
    driver.get(LOCAL)
    yield driver  # 테스트 함수에게 driver 인스턴스를 넘김
    time.sleep(2)
    driver.quit()

def scroll_to_bottom(driver, delay=0.8, max_tries=5):
    last_height = driver.execute_script("return document.body.scrollHeight")
    tries = 0

    while tries < max_tries:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)  

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            tries += 1  
        else:
            tries = 0  
        last_height = new_height

# 등가 분할, 경계값 분석 기반 테스트
@pytest.mark.parametrize("query, expected_min", [
    ("a", 1),       # 경계값 분석 - 최소 입력
    ("laptop", 1),  # 정상 입력
    ("", 0),        # 빈 문자열 - 비정상 입력
])

def test_search_query_variants(driver, query, expected_min):
    home_page = HomePage(driver)
    time.sleep(1)
    home_page.enter_search_query(query)
    time.sleep(0.5)
    home_page.click_search_button()
    scroll_to_bottom(driver)
    time.sleep(1)

    result_count = home_page.get_result_count()
    assert result_count >= expected_min

def test_multi_step_query(driver):
    home_page = HomePage(driver)

    for keyword in ["iphone", "laptop", "laptop, Ram"]:
        home_page.clear_search_input()
        time.sleep(0.3)
        home_page.enter_search_query(keyword)
        time.sleep(0.2)
        home_page.click_search_button()
        time.sleep(1.5)
        scroll_to_bottom(driver)
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(0.5)  
        assert home_page.get_result_count() >= 1