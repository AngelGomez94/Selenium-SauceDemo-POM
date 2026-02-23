import pytest
from pages.pagelogin import LoginPage
from data.data import USUARIOS_VALIDOS

@pytest.mark.parametrize("user, password", USUARIOS_VALIDOS)
def test_login_exitoso(driver,user,password):
    login = LoginPage(driver)
    login.abrir_url("https://www.saucedemo.com/")
    login.ingresar_credenciales(user, password)

    assert "/inventory.html" in driver.current_url, "❌ El login falló."

    url = login.logout()
    assert url == login.link_principal, F"No se pudo realizar el logout"

