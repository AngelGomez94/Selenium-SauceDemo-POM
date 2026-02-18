import pytest
from pages.pagelogin import LoginPage


# Aquí definimos los datos: [("usuario", "contraseña"), ...]
datos_login = [
    ("standard_user", "secret_sauce"),            # Usuario OK
    ("locked_out_user", "secret_sauce"),          # Usuario bloqueado
    ("problem_user", "secret_sauce"),             # Usuario con problemas
    ("usuario_falso", "clave_falsa")              # Usuario inexistente
]

@pytest.mark.parametrize("user, password", datos_login)
def test_login_multiple(driver, user, password):
    login = LoginPage(driver)
    login.abrir_url("https://www.saucedemo.com/")
    
    print(f"\nProbando con el usuario: {user}")
    login.ingresar_credenciales(user, password)
    
    # Aquí podrías poner una lógica que valide según el tipo de usuario
    # Por ahora, solo queremos ver cómo Pytest corre 4 veces el mismo test