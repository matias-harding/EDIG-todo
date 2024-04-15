# EDIG-Todo

## Instrucciones de Instalación

### Pre-requisitos

**Docker** instalado en el sistema. Aqui un link a la [página oficial de Docker](https://www.docker.com/get-started).

### Configuración del Proyecto

1. **Construcción y ejecución del contenedor Docker**

   Desde la raíz del proyecto ejecuta:

   ```
   docker-compose --build
   ```

### Acceso a la Aplicación

Una vez las imagenes esten construidas y los contenedores levantados la aplicacion estra disponible en [http://localhost:3000](http://localhost:3000).

### Error de conección

  Si llegara a ocurrir un error de conección una vez los contenedores esten arriba, intente lo bajarlos y volverlos a correr:

   ```
   docker-compose down
   docker-compose up --build
   ```

  Si el error persiste considera hacer una instalacion local:

  - Frontend (./frontend)

   ```
   npm install
   ```

   y luego

   ```
    npm run dev
   ```

  - Backend (./backend)

  ```
   pip3 install -r requirements.txt
  ```

  y luego

  ```
   uvicorn main:app --reload
  ```

  **NOTA:** en el archivo ./backend/database.py se requiere comentar el hostname y port para Docker y descomentar el hostname y port para Local.

  - DB (./mysql)

  ```
   docker build -t edig-todo-mysql .
  ```

  y una vez construido

  ```
   docker run --name edig-mysql -e MYSQL_USER=edig MYSQL_PASSWORD=3dig_t0D0 -e MYSQL_DATABASE=EDIG_TODO -p 3307:3306 -d edig-todo-mysql
  ```


### Recuerda que

- **Docker debe estar corriendo**
- **El puerto 3000 debe estar disponible**

---

<img width="734" alt="Captura de Pantalla 2024-04-14 a la(s) 23 05 24" src="https://github.com/matias-harding/EDIG-todo/assets/2810449/aea2a22b-367a-46f2-8c93-e5827309b341">
