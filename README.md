# API de Gestión de Productos (FastAPI)

Este proyecto es una API RESTful desarrollada con [FastAPI](https://fastapi.tiangolo.com/) para la gestión de productos. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una base de datos.

## Requisitos

*   Python 3.10 o superior
*   Pip (gestor de paquetes de Python)

## Instalación

1.  **Clonar el repositorio** (o descargar los archivos):
    ```bash
    cd FAPI_practica
    ```

2.  **Crear un entorno virtual** (recomendado para aislar dependencias):
    ```bash
    python -m venv venv
    ```

3.  **Activar el entorno virtual**:
    *   En Windows:
        ```bash
        venv\Scripts\activate
        ```
    *   En macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4.  **Instalar dependencias**:
    Ejecuta el siguiente comando para instalar las librerías necesarias (`fastapi`, `uvicorn`, `sqlalchemy`):
    ```bash
    pip install fastapi uvicorn sqlalchemy
    ```

## Ejecución

Para iniciar el servidor de desarrollo con recarga automática, ejecuta:

```bash
uvicorn main:app --reload
```

El servidor se iniciará en `http://127.0.0.1:8000`.

## Uso y Documentación

Una vez que el servidor esté corriendo, puedes acceder a la documentación interactiva generada automáticamente para probar los endpoints:

*   **Swagger UI:** http://127.0.0.1:8000/docs - Interfaz gráfica para probar la API.
*   **ReDoc:** http://127.0.0.1:8000/redoc - Documentación alternativa.

Los endpoints disponibles son:
*   `GET /productos`: Listar productos.
*   `POST /productos`: Crear producto.
*   `GET /productos/{id}`: Obtener detalle.
*   `PUT /productos/{id}`: Actualizar.
*   `DELETE /productos/{id}`: Eliminar.