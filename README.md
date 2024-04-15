# EDIG-Todo

## Instrucciones de Instalación

### Pre-requisitos

Antes de comenzar, asegurarse de tener instalado lo siguiente en el sistema:

- **Python 3.12** o una versión compatible.
- **pip 23.2.1** o una versión compatible.

### Configuración del Proyecto

1. **Construcción y ejecución del contenedor Docker**

   En la raíz del proyecto ejecuta lo siguiente para el front y DB Dockerizado:

   ```
   docker-compose run --build
   ```

2. **Instalación de dependencias**

   Desde la raiz del proyecto `cd backend` y ejecutar:

   ```
   pip3 install -r requirements.txt
   ```

### Ejecución de la Aplicación

Si la instalación fue exitosa, inicia el servidor de desarrollo con:

```
uvicorn app:app --reload
```

La aplicación debería estar ya disponible en [http://localhost:3000](http://localhost:3000).

### Problemas Comunes

Si encuentras errores durante la instalación de las dependencias, asegúrate de que tu pip esté actualizado y que Python 3.12 esté configurado como tu versión predeterminada de Python.

---

<img width="734" alt="Captura de Pantalla 2024-04-14 a la(s) 23 05 24" src="https://github.com/matias-harding/EDIG-todo/assets/2810449/aea2a22b-367a-46f2-8c93-e5827309b341">
