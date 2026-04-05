from playwright.sync_api import Page
from playwright.sync_api import expect
from helpers.data_helper import USUARIO_VALIDO, CONTRASENA_VALIDA
from helpers.login_helper import login
from helpers.urls_helper import URL_BASE, URL_INVENTARIO
from locators.inventary_locators import *
from locators.login_locators import *

"""
    3. Verifica que un usuario puede añadir productos al carrito correctamente.
"""


def test_agregar_productos_carrito(page: Page):

    # Navegar al login
    page.goto(URL_BASE)

    # Hacer login con credenciales válidas
    login(page, USUARIO_VALIDO, CONTRASENA_VALIDA)

    # Comprobar navegación al inventario
    expect(page).to_have_url(URL_INVENTARIO)

    # Comprobar estado del carrito sin productos añadidos
    expect(page.locator(CONTADOR_CARRITO)).to_be_hidden()

    # Añadir 2 elementos al carrito
    elementos_inventario = page.locator(
        ELEMENTOS_INVENTARIO).all()

    for i in range(2):
        elementos_inventario[i].locator(
            BOTON_AGREGAR_CARRITO_ELEMENTO_INVENTARIO).click()

    # Comprobar estado del carrito a 2 elementos añadidos
    expect(page.locator(CONTADOR_CARRITO)).to_have_text("2")
