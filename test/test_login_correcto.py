from pages.pagelogin import LoginPage

def test_login_exitoso(driver):
    login = LoginPage(driver)
    login.abrir_url("https://www.saucedemo.com/")
    login.ingresar_credenciales("standard_user", "secret_sauce")

    assert "/inventory.html" in driver.current_url, "❌ El login falló, la URL no es la esperada."
    print("✅ CP001: Login exitoso y verificado.")


