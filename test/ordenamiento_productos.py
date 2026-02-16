from pages.product_page import ProductPage
import time

def test_ordenamiento_productos(driver):
    filtros = ProductPage(driver)
    filtros.abrir_url("https://www.saucedemo.com/")
    filtros.ingresar_credenciales("standard_user", "secret_sauce")
    filtros.filtro_menor_precio_a_mayor()
    time.sleep(2)
    filtros.filtro_alfabeticamente_z_a()
    articuloz_a = filtros.obtener_item_z_a()
    assert articuloz_a == "Test.allTheThings() T-Shirt (Red)", f"No coincide el texto del primer articulo"
