import time
import pytest
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

# 경로 설정 및 환경 변수 로드
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
load_dotenv()

from tests.python.pages.saramin.login_page import LoginPage
from tests.python.pages.saramin.main_page import MainPage
from tests.python.pages.saramin.resume_page import ResumePage
from tests.python.pages.saramin.resume_detail_page import ResumeDetailPage
from tests.python.pages.saramin.resume_edit_page import ResumeEditPage

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

    resume_detail_page = ResumeDetailPage(driver)
    resume_detail_page.click_edit_resume_button()

    WebDriverWait(driver, 10).until(
        lambda d: "resume-manage/edit" in d.current_url
    )
    assert "resume-manage/edit" in driver.current_url, "이력서 수정 페이지로 이동하지 않았습니다."

    # 수정 폼 로딩 완료 대기
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea[name="mycareer_contents"]'))
    )

    resume_edit_page = ResumeEditPage(driver)
    resume_edit_page.click_mycareer_edit_button()  

    new_text = """
소프트웨어학과를 졸업한 신입 QA 엔지니어 정윤식입니다.  
Node.js 기반 서버 개발 경험을 바탕으로, 프론트엔드(React)와 백엔드(NestJS)를 연동하여 Rest API를 구축하고, Docker와 AWS EC2를 이용해 서비스를 직접 배포한 경험이 있습니다.

프로젝트 개발 과정에서 Postman, Pytest, Selenium 등을 활용해 테스트를 자동화하고, 단위 테스트와 E2E 테스트(Jest + Supertest)로 기능 검증을 수행하였습니다. 또한, 경계값 분석·등가분할 테스트 기법을 활용한 시나리오 설계와, 실제 사용자 시나리오 기반 UI 테스트 자동화를 통해 품질을 높이는 경험도 해보았습니다.

이 경험을 통해 깨달은 점은, "품질은 개발의 마지막 단계가 아니라, 기획과 설계 단계에서부터 함께 고려되어야 한다"는 것입니다. 사용자의 관점에서 문제를 바라보고, 예상 가능한 오류를 미리 차단하며, 개선점을 찾아내는 것이 QA의 핵심이라고 생각합니다.

기술적인 능력뿐 아니라 팀원들과 협업하여 테스트 프로세스를 정립하고, 지속적으로 품질을 개선하는 QA 엔지니어가 되겠습니다.
""".strip()

    resume_edit_page.update_mycareer_textarea(new_text)
    resume_edit_page.click_save_then_complete()
