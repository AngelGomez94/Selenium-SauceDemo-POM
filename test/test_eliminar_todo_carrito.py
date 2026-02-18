import pytest
from pages.product_page import ProductPage
from data.data import USUARIOS_VALIDOS

@pytest.mark.parametrize("user,password",USUARIOS_VALIDOS)
def test_eliminar_todo_del_carrito(driver,user,password):
    productos = ProductPage(driver)
    productos.abrir_url("https://www.saucedemo.com/")
    productos.ingresar_credenciales(user,password)
    productos.agregar_productos_carrito()
    productos.ir_al_carrito()
    productos.eliminar_todo_del_carrito()
    cantidad_items= productos.validar_cero_articulos_carrito()
    assert cantidad_items == 0, f"❌ Error: El carrito aún tiene {cantidad_items} productos."
    productos.continue_shoping()


