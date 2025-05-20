from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def enter_search_query(self, query):
        search_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"]'))
        )
        search_input.clear()
        search_input.send_keys(query)

    def click_search_button(self):
        button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.search-bar button.btn-primary'))
        )
        button.click()

    def get_search_results(self):
        return self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul.list-group li.list-group-item'))
        )
    
    def get_result_count(self) -> int:
        try:
            return len(self.get_search_results())
        except:
            return 0
        
    def clear_search_input(self):
        search_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"]'))
        )
        search_input.clear()

    def is_first_result_valid(self) -> bool:
        try:
            results = self.get_search_results()
            if not results:
                return False

            first = results[0]
            img = first.find_element(By.TAG_NAME, 'img')
            title = first.find_element(By.TAG_NAME, 'h5')
            price = first.find_element(By.TAG_NAME, 'p')

            return all([
                img.get_attribute('src'),
                title.text.strip(),
                price.text.strip()
            ])
        except Exception:
            return False
