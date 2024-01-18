# libros_peliculas
Desarrollo de 2 micro servicios que brindan información de libros y películas cada que se consultan, enmascaradas las URLs con Nginx y alojadas en un contenedor Docker. 

# Ejecución del contenedor
## Para ejecutar el proyecto se ejecuta el siguiente comando dentro del repositorio descargado:
  ```
    docker-compose up --build
  ```
## Una vez ejecutado este, él se auto configura y despliega para consumir las URLs:
  http://localhost/books
  
  http://localhost/movies
## Las cuales enmascaran las originales de Flask que incluyen puerto y el nombre es más largo. Estas devuelven información de libros y películas respectivamente.

