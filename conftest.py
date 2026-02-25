import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest_html
import time
from pytest_html import extras

@pytest.fixture(scope="function")
def driver():
    # --- CONFIGURACIÓN DE CHROME ---
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
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    
    yield driver # Le presta el driver al test
    
    # --- DESPUÉS DEL TEST ---
    time.sleep(2) # Bajé un poco el sleep para no esperar tanto
    driver.quit()

# --- HOOK PARA CAPTURAS DE PANTALLA EN CASO DE FALLO ---
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        # Buscamos el driver dentro de la fixture
        driver = item.funcargs.get("driver")
        if driver:
            # Tomamos la captura en base64 para que el reporte sea un solo archivo
            screenshot = driver.get_screenshot_as_base64()
            html = f'<div><img src="data:image/png;base64,{screenshot}" alt="screenshot" style="width:600px;height:350px;" ' \
                   'onclick="window.open(this.src)" align="right"/></div>'
            extra.append(extras.html(html))
    
    report.extra = extra