Installing Connector/Python with pip
Using pip is the recommended way to install Connector/Python and it functions on all standard systems, including Windows, and installing the Python language also installs pip.


# Installation
pip install mysql-connector-python

# Upgrade
pip install mysql-connector-python --upgrade

# Optional, installs the X DevAPI interface
pip install mysqlx-connector-python


from sqlalchemy import create_engine
conexion = create_engine(f'mysql+mysqlconnector://root:Mysql-1904@localhost/olympics-dos') ###ojo hay que poner el nombre de la base de datos y es mejor si no tiene guiones
connection = conexion.raw_connection()
cursor = connection.cursor()
cursor.execute('DROP DATABASE `olympics-dos`;')  # ojo con los `` 
conexion.dispose()


# UTILIZO UNA FUNCÓN PARA QUE INDIQUE SI LOS VALORES PERMITEN TENER METRICAS: 

def display_summary_statistics(df, column):
    try:
        summary_statistics = df[column].describe().loc[['mean', 'std', 'min', 'max']]
        print(f"{column.capitalize()} Estadigrafos se muestrar ok.")
        return True
    except KeyError:
        print(f"Error: Column '{column}' does not exist in the DataFrame.")
        return False

# LLAMO A LA FUNCION PARA OBTENER LAS METRICAS DE AMBAS COLUMNAS
display_summary_statistics(df_transactions, 'amount')
display_summary_statistics(df_users, 'age')
