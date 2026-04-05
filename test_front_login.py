from playwright.sync_api import Page
from playwright.sync_api import expect
from helpers.login_helper import login
from helpers.texts_helper import TEXTO_MENSAJE_ERROR_LOGIN
from helpers.data_helper import USUARIO_VALIDO, USUARIO_INVALIDO, CONTRASENA_VALIDA, CONTRASENA_INVALIDA
from helpers.urls_helper import URL_BASE, URL_INVENTARIO
from locators.inventary_locators import *
from locators.login_locators import *

"""
    1. Verifica que un usuario puede iniciar sesión con credenciales válidas.
"""


def test_login_valido(page: Page):

    # Navegar al login
    page.goto(URL_BASE)

    # Aserciones de elementos básicos del login
    expect(page.locator(CAMPO_USUARIO_LOGIN)).to_be_visible()
    expect(page.locator(CAMPO_CONTRASENA_LOGIN)).to_be_visible()
    expect(page.locator(BOTON_LOGIN)).to_be_visible()
    expect(page.locator(BOTON_LOGIN)).to_be_enabled()

    # Hacer login con credenciales válidas
    login(page, USUARIO_VALIDO, CONTRASENA_VALIDA)

    # Comprobar navegación al inventario
    expect(page).to_have_url(URL_INVENTARIO)

    # Comprobar elementos del inventario
    elementos_inventario = page.locator(
        ELEMENTOS_INVENTARIO).all()

    for ELEMENTO_INVENTARIO in elementos_inventario:
        # Comprobar elemento, imagen, título, descripción, precio y botón de añadir al carrito sean visibles
        expect(ELEMENTO_INVENTARIO).to_be_visible()
        expect(ELEMENTO_INVENTARIO.locator(
            IMAGEN_ELEMENTO_INVENTARIO)).to_be_visible()
        expect(ELEMENTO_INVENTARIO.locator(
            TITULO_ELEMENTO_INVENTARIO)).to_be_visible()
        expect(ELEMENTO_INVENTARIO.locator(
            DESCRIPCION_ELEMENTO_INVENTARIO)).to_be_visible()
        expect(ELEMENTO_INVENTARIO.locator(
            PRECIO_ELEMENTO_INVENTARIO)).to_be_visible()
        expect(ELEMENTO_INVENTARIO.locator(
            BOTON_AGREGAR_CARRITO_ELEMENTO_INVENTARIO)).to_be_visible()


"""
    2. Verifica que el sistema muestra un mensaje de error al intentar iniciar sesión
    con credenciales inválidas.
"""


def test_login_invalido(page: Page):

    # Navegar al login
    page.goto(URL_BASE)

    # Hacer login con credenciales inválidas
    login(page, USUARIO_INVALIDO, CONTRASENA_INVALIDA)

    # Aserciones del mensaje de error
    expect(page.locator(MENSAJE_ERROR_LOGIN)).to_be_visible()
    expect(page.locator(MENSAJE_ERROR_LOGIN)).to_contain_text(
        TEXTO_MENSAJE_ERROR_LOGIN)
