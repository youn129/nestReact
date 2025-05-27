from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class ResumeDetailPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click_edit_resume_button(self):
        # 버튼 요소 로딩 대기
        edit_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.BtnType.BtnTypeRd.SizeML'))
        )

        # 화면에 보이도록 스크롤 및 hover
        actions = ActionChains(self.driver)
        actions.move_to_element(edit_button).perform()
        time.sleep(1.5)

        # 클릭 가능한 상태 확인 후 클릭
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.BtnType.BtnTypeRd.SizeML'))
        )
        edit_button.click()