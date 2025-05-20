from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ResumePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def scroll_and_click_target_resume(self, target_text: str):
        scroll_attempts = 0
        found = False

        while scroll_attempts < 5:
            links = self.driver.find_elements(By.CSS_SELECTOR, 'a.tit.btn_action span')
            for span in links:
                if target_text in span.text:
                    actions = ActionChains(self.driver)
                    actions.move_to_element(span).perform()
                    time.sleep(2)
                    span.click()
                    found = True
                    break

            if found:
                break

            for _ in range(5):
                self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
                time.sleep(1.2)

            scroll_attempts += 1

        assert found, f'"{target_text}" 이력서를 찾지 못했습니다.'
