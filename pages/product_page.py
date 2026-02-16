from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select
import time
class ProductPage(BasePage):
    
    txt_usuario = (By.ID, "user-name")
    txt_pasword = (By.ID, "password")
    btn_login = (By.ID, "login-button")
    btns_add_cart = (By.CLASS_NAME,"btn_primary")
    cantidad_productos_carrito = (By.CLASS_NAME,"shopping_cart_link")
    checkout = (By.ID,"checkout")
    txt_firtsname = (By.ID,"first-name")
    txt_last_name = (By.ID,"last-name")
    txt_zip = (By.ID,"postal-code")
    btn_continue = (By.ID, "continue")
    btn_finish = (By.ID,"finish")
    lbl_text = (By.CLASS_NAME,"complete-header")
    btn_back_home = (By.ID,"back-to-products")
    btn_remove = (By.XPATH,"//button[text()='Remove']")
    items_carrito = (By.CLASS_NAME ,"cart_item")
    btn_continue_shopping = (By.ID,"continue-shopping")
    filters_product = (By.CLASS_NAME,"product_sort_container")
    producto_z_a = (By.CSS_SELECTOR,".inventory_list .inventory_item:nth-child(1) .inventory_item_name") #first-child asegura que es el primer item de la clase
    twitter = (By.CLASS_NAME,"social_twitter")

    def __init__(self, driver):
        super().__init__(driver)

    def ingresar_credenciales(self,usuario,password):
        self.wait.until(EC.element_to_be_clickable(self.txt_usuario)).send_keys(usuario)

        self.driver.find_element(*self.txt_pasword).send_keys(password)
        self.driver.find_element(*self.btn_login).click()   
    def agregar_productos_carrito(self):
        clicks = self.wait.until(EC.visibility_of_all_elements_located(self.btns_add_cart))
        for i in clicks:
            i.click()
    def ir_al_carrito(self):
        click_carrito =self.wait.until(EC.element_to_be_clickable(self.cantidad_productos_carrito))
        click_carrito.click()
    def ir_a_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.checkout)).click()
    def fill_checkout(self,nombres,apellidos,cp):
        self.wait.until(EC.url_contains("checkout-step-one.html"))
        self.driver.find_element(*self.txt_firtsname).send_keys(nombres)
        self.driver.find_element(*self.txt_last_name).send_keys(apellidos)
        self.driver.find_element(*self.txt_zip).send_keys(cp)
        self.driver.find_element(*self.btn_continue).click()
    def checkout_step_two(self):
        self.wait.until(EC.url_contains("checkout-step-two.html"))
        self.driver.find_element(*self.btn_finish).click()
    def checkout_message(self):
        self.wait.until(EC.url_contains("checkout-complete.html"))
        return self.driver.find_element(*self.lbl_text).text
    def back_home(self):
        self.wait.until(EC.element_to_be_clickable(self.btn_back_home)).click()
    def main_page(self):
        return self.driver.current_url
    
    def eliminar_todo_del_carrito(self):
        remove = self.wait.until(EC.visibility_of_any_elements_located(self.btn_remove))
        for i in remove:
            i.click()
    def validar_cero_articulos_carrito(self):
        
        validar_items_borrados = self.driver.find_elements(*self.items_carrito)
        return len(validar_items_borrados)
    
    def continue_shoping(self):
        self.wait.until(EC.element_to_be_clickable(self.btn_continue_shopping)).click()
    
    def filtro_menor_precio_a_mayor(self):
        self.wait.until(EC.url_contains("inventory.html"))
        filtro_menor_mayor = Select(self.driver.find_element(*self.filters_product))
        filtro_menor_mayor.select_by_visible_text(("Price (low to high)"))

    def filtro_alfabeticamente_z_a(self):
        self.wait.until(EC.url_contains("inventory.html"))
        filtro_z_a = Select(self.driver.find_element(*self.filters_product))
        filtro_z_a.select_by_visible_text(("Name (Z to A)"))
    def obtener_item_z_a(self):
        return self.wait.until(EC.element_to_be_clickable(self.producto_z_a)).text
    
    def footer_twitter(self):
        self.wait.until(EC.url_contains("inventory.html"))
        ventana_principal= self.driver.current_window_handle
        self.driver.find_element(*self.twitter).click()
        self.wait.until(EC.number_of_windows_to_be(2))        
        self.driver.switch_to.window(self.driver.window_handles[1])
        nueva_url= self.driver.current_url
        self.driver.close()
        self.driver.switch_to.window(ventana_principal)
        return nueva_url
        


