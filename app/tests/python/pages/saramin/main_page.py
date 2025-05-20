import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click_resume_menu(self):
        time.sleep(1.5)  # DOM 렌더링 대기
        resume_menu = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "이력서/자소서")]'))
        )
        resume_menu.click()
