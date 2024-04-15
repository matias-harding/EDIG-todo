EDIG-Todo

En la raiz del proyecto correr:
docker-compose run --build

Luego en la carpeta /backend:

Asegurarse de tener instalado

python 3.12 o compatible
pip 23.2.1 o compatible

correr:
pip3 install -r requirements.txt

finalmente si la instalacion fue exitosa:
uvicorn app:app --reload

la aplicacion deberia ser visible en [http://localhost:3000](http://localhost:3000/)

![Edig-Todo](<Captura de Pantalla 2024-04-14 a la(s) 23.05.24.png>)