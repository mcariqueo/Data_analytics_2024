
# SPRINT 6

En el nivell 1, s'espera que generis visualitzacions que facilitin la comprensió del patró de vendes per país. 

## Nivell 1 -  Exercici 1

L'empresa necessita avaluar el rendiment de les vendes a nivell internacional. Com a part d'aquest procés, et demanen que triïs un gràfic en el qual es detalli la mitjana de vendes desglossades per país i any en una mateixa presentació visual. És necessari assenyalar les mitjanes que són menors a 200 euros anuals.

1. Creo una tabla que tenga:
    1. promedio de ventas, pais, año.
   ![b](files_6/611b.png)
    2. Con la visualización anterior elijo el grafico de barras agrupadas que me permite ver de manera ordenadad cada año. 
    ![a](files_6/611a.png)
    3. Agrego una linea constante que indique el KPI = 200 €:
    ![c](files_6/611c.png)
    4. Finalmente agrego al costado una segmentacion de datos con año y country, de manera que sirva para poder analizar dinamicamente la visualización.
    ![d](files_6/611d.png)
   
2. Finalmente el dashboard es el siguiente:
![e](files_6/611e.png)

## Nivell 1 - Exercici 2

L'empresa està interessada a obtenir una visió general de les transaccions realitzades per cada país. La teva tasca és crear una visualització que identifiqui el percentatge de les vendes per país.

1. En primer lugar, realizo una tabla que indique: country y suma amount
2. Filtro el grafico a traves de declined = 0:
   ![612a](files_6/612a.png)

3. Indico a la visualización que indique categoria (country) y porcentaje del total:
   ![612b](files_6/612b.png)

4. Elimino la interaccion entre el ejercicio 1 y 2, para no alterar la visualización.  

El resultado final es:

 ![612c](files_6/612c.png)

## Nivell 1 - Exercici 3

Dissenya un indicador visual en Power BI per a analitzar la diferència de vendes entre els anys 2022 i 2021 en cada país. L'empresa està interessada a comprendre com han variat les vendes en diferents països durant aquest període i desitja identificar qualsevol disminució o augment significatiu en les vendes.


1. Creo dos medidas dax para tener el promedio de venta. Esto me permite tener un valor que represente mejor las diferencias, ya que el 2021 contiene mas datos que el 2022.
   ![613a](files_6/613a.png)
   ![613b](files_6/613b.png)

2. A continuación, creo una medida DAX para obtener el porcentaje de diferencia entre la media del 2021 y 2022, siendo negativo una disminución y positivo un aumento del promedio de ventas:
   ![613c](files_6/613c.png)



## Nivell 1 - Exercici 4

Crea una visualització en la qual es pugui comptabilitzar el nombre de transaccions rebutjades en cada país per a mesurar l'eficàcia de les operacions. Recorda que l'empresa espera tenir menys de 5 transaccions rebutjades per país.

## Nivell 1 - Exercici 5

L'empresa busca comprendre la distribució geogràfica de les vendes per a identificar patrons i oportunitats específiques en cada regió. Selecciona la millor visualització per a mostrar aquesta informació.

## Nivell 1 - Exercici 6

El teu cap t'ha demanat preparar una presentació per al teu equip en la qual es detallin la informació de tots els gràfics visualitzats fins ara. Per a complir amb aquesta sol·licitud, has de proporcionar una interpretació de les visualitzacions obtingudes. La presentació pot realitzar-se amb la informació general o seleccionant un element en particular, com per exemple, els resultats d'Espanya.

## Nivell 2

En el nivell 2, aprofundirem en les transaccions de les empreses, tenint en compte el factor temporal. 

Exercici 1
La teva tasca consisteix a implementar un filtre interactiu que permeti seleccionar les vendes per a cada any.

Exercici 2
La gerència està interessada a analitzar més a fons les vendes en relació amb el mes. Per tant, et demanen que facis els ajustos necessaris per a mostrar la informació d'aquesta manera.

Exercici 3
Visualitza el total de vendes i la quantitat de transaccions realitzades. Si és necessari, pots crear dues visualitzacions separades.

Exercici 4
Crea una visualització que permeti observar de manera efectiva i clara la quantitat de les vendes realitzades i la quantitat de transaccions rebutjades. 

Exercici 5
Selecciona una visualització en la qual es reflecteixi els estadístics descriptius de les empreses que van realitzar transaccions. Recorda mostrar el total de cada estadístic.


Nivell 3
Exercici 1

Finalment, en el nivell 3, es crearan visualitzacions per a analitzar el patró de transaccions per usuari i producte.


En la teva empresa, volen aprofundir en l'anàlisi de les característiques dels usuaris que participen en les transaccions, així com en els productes venuts. T'han demanat que creïs visualitzacions rellevants per a millorar estratègicament les campanyes publicitàries i augmentar les vendes. Les visualitzacions que has d'incloure són les següents:
Informació personal dels usuaris/es.
•	Quantitat de transaccions realitzades i rebutjades. L'empresa espera que cada usuari/ària tingui almenys 10 transaccions per any, i que tinguin menys de 2 transaccions rebutjades per any.
•	Identificació del producte més barat i més car comprat per cada usuari/ària, juntament amb el seu preu.
•	Distribució geogràfica dels usuaris/es.
•	Mitjana de vendes realitzada.
•	L'usuari/ària ha de tenir l'opció de seleccionar si desitja mirar la informació d'un any únicament.
Després de crear els gràfics, has de presentar la informació de l'usuari/ària amb l'ID 96 amb una breu descripció de les dades a través d'una presentació de diapositives. Assegura't d'optimitzar la llegibilitat i comprensió de les visualitzacions mitjançant ajustos adequats.
