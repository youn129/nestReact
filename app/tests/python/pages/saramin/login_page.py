import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click_login_button(self):
        login_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.btn_sign.signin'))
        )
        time.sleep(1)
        login_btn.click()

    def click_kakao_login_button(self):
        kakao_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.login_kakao a'))
        )
        time.sleep(1.5)
        kakao_btn.click()

    def switch_to_kakao_popup(self):
        main_window = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != main_window:
                self.driver.switch_to.window(handle)
                break
        time.sleep(2)

    def enter_kakao_credentials(self, username, password):
        # 아이디 입력 필드 로딩 대기 후 입력
        id_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "loginId--1"))
        )
        time.sleep(1)
        id_field.clear()
        id_field.send_keys(username)

        # 비밀번호 입력 필드 로딩 대기 후 입력
        pw_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "password--2"))
        )
        time.sleep(1)
        pw_field.clear()
        pw_field.send_keys(password)

        # 로그인 버튼 클릭 전 대기
        time.sleep(1)
        login_btn = self.driver.find_element(By.CSS_SELECTOR, "button.btn_g.highlight.submit")
        login_btn.click()
        time.sleep(5)  # 로그인 후 리디렉션 여유
