from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select



class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)
    
    def abrir_url(self, url):
        self.driver.get(url)
    
    def esperar_y_hacer_click(self, locator):
      self.wait.until(EC.element_to_be_clickable(locator)).click()
    
    def escribir(self,locator,texto):
        elemento = self.wait.until(EC.visibility_of_element_located(locator))
        elemento.clear()
        elemento.send_keys(texto)
    def obtener_texto(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
    def filtros(self,locator,text_in_filter):
         filtro = self.wait.until(EC.visibility_of_element_located(locator))
         Select(filtro).select_by_visible_text(text_in_filter)
    def wait_url(self,url):
         self.wait.until(EC.url_contains(url))

   