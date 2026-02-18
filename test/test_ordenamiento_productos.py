import pytest
from pages.product_page import ProductPage
from data.data import USUARIOS_VALIDOS
@pytest.mark.parametrize("user,password",USUARIOS_VALIDOS)
def test_ordenamiento_productos(driver,user,password):
    filtros = ProductPage(driver)
    filtros.abrir_url("https://www.saucedemo.com/")
    filtros.ingresar_credenciales(user, password)
    prodructo_menor = filtros.filtro_menor_precio_a_mayor()
    assert prodructo_menor == "Sauce Labs Onesie", f"El articulo no es el de menor precio."
    #time.sleep(2)
    articuloz_a =filtros.filtro_alfabeticamente_z_a()
    #articuloz_a = filtros.obtener_item_z_a()
    assert articuloz_a == "Test.allTheThings() T-Shirt (Red)", f"No coincide el texto del primer articulo"
