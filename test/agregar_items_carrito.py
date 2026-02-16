from pages.product_page import ProductPage

def test_agregar_items_carrito(driver):
    productos = ProductPage(driver)
    productos.abrir_url("https://www.saucedemo.com/")
    productos.ingresar_credenciales("standard_user", "secret_sauce")
    productos.agregar_productos_carrito() 
    productos.ir_al_carrito()
    productos.ir_a_checkout()
    productos.fill_checkout("Andres Angel","Gomez Morales","55886")
    productos.checkout_step_two()
    mensaje = productos.checkout_message()
    assert mensaje  in  "Thank you for your order!", f"Error, no se encontro el label de compra corrcta"
    productos.back_home()
    url_inicio  = productos.main_page()
    assert url_inicio in "https://www.saucedemo.com/inventory.html", f"Error: Se esperaba la página final pero estamos en {url_inicio}"