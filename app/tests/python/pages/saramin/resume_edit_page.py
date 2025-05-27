from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class ResumeEditPage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click_mycareer_edit_button(self):
        edit_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.evtEditItem'))
        )
        ActionChains(self.driver).move_to_element(edit_btn).perform()
        time.sleep(1)
        edit_btn.click()

    def update_mycareer_textarea(self, new_text: str):
        textarea = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea[name="mycareer_contents"]'))
        )
        textarea.clear()
        time.sleep(0.5)
        
        for char in new_text:
            textarea.send_keys(char)
            time.sleep(0.02)

    def click_save_then_complete(self):
        # 저장 버튼 보이게 스크롤
        save_btn = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button.evtLayerSave'))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", save_btn)
        time.sleep(1.5)

       
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.evtLayerSave')))
        save_btn.click()

        time.sleep(3)

        complete_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.evtResumeSave'))
        )
        complete_btn.click()
