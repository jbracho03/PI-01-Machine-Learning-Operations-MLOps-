# PI-01-Machine-Learning-Operations-MLOps-
Proyecto Individual 1 

:yellow_circle: **MENU:** :black_circle:
* **objetivo.md** - _Explicacion del proyecto._
* **MLOpsReviews** - _las bases de datos que recibí para trabajar._
* **Datos_PI_2.csv** - _carpeta necesaria para el funcionamiento de la api._
* **Desarrollo de la API.ipynb** - _notebook con pruebas de las queries._
* **Transformacion de datos PI01.ipynb** - _paso a paso del ETL._
* **main.py** - _el código de la API._
* **requirements.txt** - _dependencias necesarias para que funcione._
* **EDA.ipynb** - _transformacion de datos._
* **recomendacion.ipynb** - _sistema de recomendacion de peliculas segun usuario._

:yellow_circle: **Las funciones que componen la API son:** :black_circle:

:white_medium_small_square: Pelicula con mayor duracion cpor Año, Plataforma y Tipo de duracion. <br>
:white_medium_small_square: Cantidad de peliculas por plataforma con un puntaje mayor a XX en determinado año. <br>
:white_medium_small_square: Cantidad de peliculas por plataforma.. <br>
:white_medium_small_square: Actor que mas se repite segun plataforma y año. <br>

:yellow_circle: **Link para instalar la API:** :black_circle:
:white_medium_small_square: https://deta.space/discovery/r/qr4rgck6e8wkdetc <br>

:yellow_circle: **Cómo escribir cada función en el navegador:** :black_circle: 

:white_medium_small_square: https://detaspacepi01-1-d0046100.deta.app/max_duration/{year}/{platform}/{duration_type}<br>
:white_medium_small_square: https://detaspacepi01-1-d0046100.deta.app/get_score_count/{platform}/{score}/{year} <br>
:white_medium_small_square: https://detaspacepi01-1-d0046100.deta.app/get_count_platform/{platform} <br>
:white_medium_small_square: https://detaspacepi01-1-d0046100.deta.app/get_actor/{platform}/{year} <br>

:yellow_circle: **Queries de ejemplo para probar la api** :black_circle: 

:white_medium_small_square: https://detaspacepi01-1-d0046100.deta.app/max_duration/2012/n/min <br>
:white_medium_small_square: https://detaspacepi01-1-d0046100.deta.app/get_score_count/n/4.0/2011 <br>
:white_medium_small_square: https://detaspacepi01-1-d0046100.deta.app/get_count_platform/amazon <br>
:white_medium_small_square: https://detaspacepi01-1-d0046100.deta.app/get_actor/disney/2010 <br>

:warning: **Sintaxis a tener en cuenta al escribir una consulta:** :warning:<br>
:white_medium_small_square: Todo debe estar escrito en minúsculas.  <br>
:white_medium_small_square: Las plataformas que admite son: Amazon, Disney, Hulu y Netflix. <br>
:white_medium_small_square: En la primera y segunda consulta al insertar platform, solo aceptara: 
            'n': 'netflix',
            'h': 'hulu',
            'd': 'disney+',
            'as': 'amazon'  <br>
:white_medium_small_square: Al escribir el sore solo aceptara si se escribe de esta manera = 4.0.<br>            
:white_medium_small_square: En caso de la query no arroje resultados, un mensaje explicativo se imprimirá en pantalla.<br>
:white_medium_small_square: En caso de que se ingrese una plataforma inválida, un mensaje explicativo se imprimirá en pantalla. <br>

:yellow_circle: **Funciones extra** :black_circle: <br>
:white_medium_small_square: Función _Presentación_: `/` <br>
Invocando el link vacío, muestra un mensaje de Bienvenida y a quien pertenece la api.<br>
:white_medium_small_square: Función _Contacto_: `/contacto`<br>
Muestra mi correo electronico y linkedin, en caso de necesidad de querer contactarme. <br>
:white_medium_small_square: Función _docs_: `/docs` <br>
Muestra el menú principal de la api, donde también se puede testear las consultas.<br>


