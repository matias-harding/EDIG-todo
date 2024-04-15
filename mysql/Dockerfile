FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=3dig_t0D0
ENV MYSQL_USER=edig
ENV MYSQL_PASSWORD=3dig_t0D0
ENV MYSQL_DATABASE=EDIG_TODO

COPY ./schema.sql /docker-entrypoint-initdb.d/schema.sql

EXPOSE 3306
