from pages.pagelogin import LoginPage

def test_login_blocked_user(driver):
 login = LoginPage(driver)
 login.abrir_url("https://www.saucedemo.com/")
 login.ingresar_credenciales("locked_out_user","secret_sauce")
 mensaje_blocked_user = login.obtener_mensaje_blocked_user()
 assert mensaje_blocked_user == login.ERR_LOCKED_USER,f"Epic sadface: Sorry, this user has been locked out."