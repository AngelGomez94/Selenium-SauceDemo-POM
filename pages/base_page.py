from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)
    
    def abrir_url(self, url):
        self.driver.get(url)
    def esperar_y_hacer_clicl(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()