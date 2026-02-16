from pages.pagelogin import LoginPage
from pages.product_page import ProductPage

def test_abrir_twitter(driver):
    login = LoginPage(driver)
    products = ProductPage(driver)
    login.abrir_url("https://www.saucedemo.com/")
    login.ingresar_credenciales("standard_user","secret_sauce")
    abrir_twitter = products.footer_twitter()
    assert abrir_twitter == "https://x.com/saucelabs", f"La url no es la de saucelabs en twitter..la url que se esta abriendo es: {abrir_twitter}"