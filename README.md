# UnemploymentBCN

Proyecto de mitad de Bootcamp (Big Data y Machine Learning) en Core Code School donde aplico parte de lo estudiado en él.

Podemos ver conocimientos adquiridos en python, el uso de diferentes librerias y herramientas:
- fastapi, streamlit, pandas, plotly, mongoDB, Docker, Heroku.

Creación, diseño, definición de endponints y parametros y lo necesario para hacer la API concectada a la bbdd creada en MongoDB.

La bbdd proviene de **[Barcelona data sets](https://www.kaggle.com/xvivancos/barcelona-data-sets)** dónde tenemos información acerca de la Administración, el entorno urbano, la población, su territorio y la economia y sus negocios. 

Para finalizar, la creación de un dashboard de visualización de datos en Streamlit, que consume los datos de la API creada.

## API

**[Api Proyecto Heroku](https://api-test-bcn.herokuapp.com/)**

### Endpoints
Información acerca de la poblacion en Barcelona.

- **/Population/Year**
Devuelve los diferentes años dentro la bbdd.

- **/Population/Gender**
Devuelve los diferentes géneros dentro la bbdd.

- **/Population/DataGender/{year}/{gender}**
Devuelve la población por rango de edades en un año y género determinado.

- **/Population/Neighborhood/{year}**
Devuelve la población total por barrios en un año determinado.

Información acerca del desempleo en Barcelona.

- **/Unemployment/Year**
Devuelve los diferentes años dentro la bbdd.

- **/Unemployment/Month**
Devuelve los diferentes meses del año dentro la bbdd.

- **/Unemployment/Demand/{year}/{month}**
Devuelve la población demandante y desempleado en un año y mes concreto.

- **/Unemployment/DataGender/{year}/{month}**
Devuelve la población desempleada por género en un año y mes determinado.

- **/Unemployment/Neighborhood/{year}/{month}**
Devuelve la población desempleada por barrios en un año y mes determinado.


## Dashboard Streamlit

A falta de colgar el dashboard en Heroku, Streamlit nos muestra los datos, que consume de la API creada, en dos paginas con diferentes visualizaciones.

- **[Población Barcelona](https://raw.githubusercontent.com/VictorBlay/UnemploymentBCN-CoreCodeSchool/main/data/Images/Population.png)**

- **[Desemploeo Barcelona](https://raw.githubusercontent.com/VictorBlay/UnemploymentBCN-CoreCodeSchool/main/data/Images/Unemployment.png)**


## Autor

**- [Victor Blay Garcia](https://github.com/VictorBlay)**

## Agradecimientos

Profesores de Bootcamp:

**- [Álvaro Lucas](https://github.com/Alvaro-Lucas)**

**- [Core Code School](https://github.com/core-school/bdmlpt0122)**







