import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

@pytest.fixture(scope="function")
def driver():
    # --- AQUÍ VA TODA TU CONFIGURACIÓN "MOLESTA" ---
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=SafeBrowsingPasswordCheck")
    
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    # Arrancamos el driver
    _driver = webdriver.Chrome(options=chrome_options)
    _driver.maximize_window()
    
    yield _driver # Esto le "presta" el driver al test
    
    # --- DESPUÉS DEL TEST ---
    time.sleep(5)
    _driver.quit() # Se cierra solito al terminar