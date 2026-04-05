from playwright.sync_api import Page

from helpers.data_helper import CONTRASENA_VALIDA, USUARIO_VALIDO
from locators.login_locators import *


def login(page, usuario, contrasena):
    page.locator(CAMPO_USUARIO_LOGIN).fill(usuario)
    page.locator(CAMPO_CONTRASENA_LOGIN).fill(contrasena)
    page.locator(BOTON_LOGIN).click()
