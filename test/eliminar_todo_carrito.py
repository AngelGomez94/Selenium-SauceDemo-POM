from pages.product_page import ProductPage

def test_eliminar_todo_del_carrito(driver):
    productos = ProductPage(driver)
    productos.abrir_url("https://www.saucedemo.com/")
    productos.ingresar_credenciales("standard_user", "secret_sauce")
    productos.agregar_productos_carrito()
    productos.ir_al_carrito()
    productos.eliminar_todo_del_carrito()
    cantidad_items= productos.validar_cero_articulos_carrito()
    assert cantidad_items == 0, f"❌ Error: El carrito aún tiene {cantidad_items} productos."
    productos.continue_shoping()


