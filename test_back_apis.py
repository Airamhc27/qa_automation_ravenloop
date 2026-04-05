import requests

from helpers.data_helper import API_KEY
from helpers.urls_helper import URL_LOGIN_API, URL_USERS_API

"""
    Verifica login correcto: devuelve 200 y token.
"""


def test_login_valido():

    # Petición post
    respuesta = requests.post(
        URL_LOGIN_API,
        headers={
            "x-api-key": API_KEY,
            "Content-Type": "application/json"
        },
        json={
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
    )

    # Comprobar status
    assert respuesta.status_code == 200

    # Guardar el cuerpo de la respuesta
    body = respuesta.json()

    # Verificar que existe el token en la respuesta
    assert "token" in body


"""
    Verifica login correcto: devuelve 400 y mensaje de error.
"""


def test_login_invalido():

    # Petición post
    respuesta = requests.post(
        URL_LOGIN_API,
        headers={
            "x-api-key": API_KEY,
            "Content-Type": "application/json"
        },
        json={
            "email": "demo@demo.com",
            "password": "demo"
        }
    )
    # Comprobar status
    assert respuesta.status_code == 400

    # Guardar el cuerpo de la respuesta
    body = respuesta.json()

    # Verificar que existe el mensaje de error en la respuesta
    assert "error" in body


"""
    Verifica lista de emails válidos.
"""


def test_lista_emails_validos():

    # Petición post
    respuesta = requests.get(
        URL_USERS_API,
        headers={
            "x-api-key": API_KEY,
            "Content-Type": "application/json"
        }
    )
    # Comprobar status
    assert respuesta.status_code == 200

    # Guardar el cuerpo de la respuesta
    body = respuesta.json()

    # Verificar que existe data con los emails en la respuesta
    assert "data" in body

    # Guardar la lista de usuarios
    usuarios = body["data"]

    # Recorrer cada usuario y verificar el email
    for usuario in usuarios:
        email = usuario["email"]
        assert "@" in email
        assert "." in email
