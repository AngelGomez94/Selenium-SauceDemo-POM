from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):
    # Estos son los campos del formulario (Selectores)
    txt_usuario = (By.ID, "user-name")
    txt_pasword = (By.ID, "password")
    btn_login = (By.ID, "login-button")
    lbl_blocked_user = (By.CLASS_NAME,"error-message-container")
    ERR_LOCKED_USER = "Epic sadface: Sorry, this user has been locked out."
    menu_desplegable = (By.ID, "react-burger-menu-btn")
    btn_logout = (By.ID,"logout_sidebar_link")
    link_principal = "https://www.saucedemo.com/"

    def __init__(self, driver):
        super().__init__(driver) # Le dice a la mamá BasePage: "Toma el driver"

    def ingresar_credenciales(self, usuario, pasword):
        # 1. Esperamos a que el campo de usuario sea visible usando el wait de la mamá
        self.escribir(self.txt_usuario,usuario)
        self.escribir(self.txt_pasword,pasword)
        self.esperar_y_hacer_click(self.btn_login)
    def obtener_mensaje_blocked_user(self):
        self.obtener_texto(self.lbl_blocked_user)
    
    def logout(self):
        self.esperar_y_hacer_click(self.menu_desplegable)
        self.esperar_y_hacer_click(self.btn_logout)
        
        return self.driver.current_url
