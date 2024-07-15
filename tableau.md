Modelo de datos en Tableau

específicamente la diferencia entre la capa lógica y la capa física de las tablas. Aquí tienes una explicación más detallada:

Capa Lógica (Logical Layer)
La capa lógica es donde defines las relaciones entre las tablas lógicas. En el diagrama, se muestra una relación entre la "Logical Table A" y la "Logical Table B". Estas tablas lógicas representan las entidades que deseas analizar en Tableau y son las que se utilizan para construir las visualizaciones.

Capa Física (Physical Layer)
La capa física se refiere a las tablas reales de la base de datos que componen las tablas lógicas. En el diagrama:

Logical Table A está compuesta por cuatro tablas físicas (Physical Table A, B, C y D). Estas tablas físicas pueden estar unidas mediante uniones (joins) o combinaciones (blends).
Logical Table B está compuesta por una sola tabla física (Physical Table B).
Relación entre Capas
La relación entre la "Logical Table A" y la "Logical Table B" en la capa lógica se representa mediante una línea de relación en el diagrama.
Las tablas físicas subyacentes en la capa física se combinan para formar las tablas lógicas en la capa lógica.
Propósito
Este modelo permite a los usuarios de Tableau crear relaciones entre datos de una manera lógica y abstracta, facilitando la construcción de visualizaciones complejas sin preocuparse demasiado por los detalles de la estructura física de los datos.

¿Te gustaría más información sobre cómo implementar o trabajar con estos modelos en Tableau?






