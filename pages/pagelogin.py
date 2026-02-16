from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Estos son los campos del formulario (Selectores)
    txt_usuario = (By.ID, "user-name")
    txt_pasword = (By.ID, "password")
    btn_login = (By.ID, "login-button")
    lbl_blocked_user = (By.CLASS_NAME,"error-message-container")
    ERR_LOCKED_USER = "Mi nombre es angel"

    def __init__(self, driver):
        super().__init__(driver) # Le dice a la mamá BasePage: "Toma el driver"

    def ingresar_credenciales(self, usuario, pasword):
        # 1. Esperamos a que el campo de usuario sea visible usando el wait de la mamá
        # El * abre la "caja" (tupla) de txt_usuario
        self.wait.until(EC.visibility_of_element_located(self.txt_usuario)).send_keys(usuario)
        
        # 2. Llenamos el resto y damos click
        self.driver.find_element(*self.txt_pasword).send_keys(pasword)
        self.driver.find_element(*self.btn_login).click()
    def obtener_mensaje_blocked_user(self):
        return self.wait.until(EC.visibility_of_element_located(self.lbl_blocked_user)).text