# 🧪 Proyecto de Automatización de Tests (Frontend + API)

## 📌 Descripción

Este proyecto contiene la automatización de pruebas de:

- **Frontend** usando Playwright
- **Backend/API** usando requests sobre la API pública de ReqRes

Se validan flujos de login, carrito/checkout y endpoints de API.

---

## ⚙️ Tecnologías utilizadas

- Python
- Pytest
- Playwright
- Requests
- Allure Report

---

## ▶️ Cómo ejecutar los tests

### 1. Crear y activar entorno virtual:

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Mac / Linux
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 3. Instalar Playwright (solo la primera vez)

```bash
playwright install
```

---

## 🧪 Ejecutar tests

### ▶️ Ejecutar todos los tests

```bash
pytest
```

### ▶️ Ejecutar tests paso a paso (modo debug Playwright)

```bash
set PWDEBUG=1
pytest
```

Esto abre el navegador y permite ver la ejecución paso a paso.

---

## 📊 Reporting con Allure

### 1. Ejecutar tests generando resultados

```bash
pytest --alluredir=allure-results
```

---

### 2. Visualizar reporte

```bash
allure serve allure-results
```

👉 Se abrirá automáticamente en el navegador con un reporte visual completo.

---

## 🧪 Casos automatizados

### 🔹 Frontend (Playwright)

- Login válido
- Login inválido
- Añadir productos al carrito
- Flujo de checkout

---

### 🔹 Backend (API - ReqRes)

- POST /api/login → login correcto (200 + token)
- POST /api/login → login incorrecto (400 + mensaje de error)
- GET /api/users?page=2 → validación de emails

---

## 🧠 Decisiones tomadas

- Uso de **pytest** como framework principal por su simplicidad.
- Uso directo de funciones y helpers para mantener el código más sencillo.
- Separación entre tests de frontend y backend.
- Uso de constantes (helpers) para URLs, datos y funciones.

---

## 🚀 Qué mejoraría con más tiempo

- Implementar **Page Object Model** para mejorar la escalabilidad
- Añadir capturas de pantalla en fallos (Allure + Playwright)
- Uso de variables de entorno para credenciales

---

## 📂 Estructura del proyecto

```
test_front_login.py
test_front_checkout.py
test_back_apis.py

helpers/
├── login_helper.py
├── urls_helper.py
├── data_helper.py
├── texts_helper.py

locators/
├── login_locators.py
├── inventary_locators.py
```

---
