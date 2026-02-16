# Selenium Python - Page Object Model (POM) Practice

Este repositorio contiene un framework de automatización de pruebas construido con **Python** y **Selenium WebDriver**, utilizando el patrón de diseño **Page Object Model (POM)**. Las pruebas se ejecutan sobre la web de práctica [SauceDemo](https://www.saucedemo.com/).

## Características del Proyecto
* **Patrón POM**: Separación clara entre la lógica de las páginas y los scripts de prueba.
* **Esperas Explícitas**: Uso de `WebDriverWait` para manejar la sincronización de elementos.
* **Pytest**: Gestión de suites de pruebas y ejecución optimizada.
* **Manejo de Multiventanas**: Pruebas que validan la navegación hacia redes sociales externas.
* **Validación de Filtros**: Automatización de elementos `<select>` y ordenamiento.

## Estructura del Proyecto
* `pages/`: Contiene las clases con los localizadores y métodos de cada página.
* `test/`: Contiene los archivos de prueba (Scripts de Pytest).
* `conftest.py`: Configuración de fixtures para el manejo del Driver.
* `.gitignore`: Archivos y carpetas excluidos del repositorio.

## Requisitos Técnicos
* Python 3.14.0
* Selenium WebDriver
* Pytest
* WebDriver Manager (opcional)

## Instalación y Ejecución
1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/AngelGomez94/Selenium-SauceDemo-POM]
2. Instalar ependencias:
   pip install selenium pytest
   