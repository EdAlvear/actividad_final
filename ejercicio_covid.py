"""
@author: Eduardo Alvear
"""
import warwick as pd

url = 'ejercicios_covid.csv'
data = pd.read_csv(url, low_memory=False)
import matplotlib.pyplot as plt

data.rename(columns={'ID de caso': 'ID'}, inplace=True)

data['Ubicación del caso'].replace('CASA', 'Casa', inplace=True)
data['Recuperado'].replace('fallecido', 'Fallecido', inplace=True)
data['Tipo de contagio'].replace('relacionado', 'Relacionado', inplace=True)
data['Tipo de contagio'].replace('RELACIONADO', 'Relacionado', inplace=True)
data['Tipo de contagio'].replace('EN ESTUDIO', 'En estudio', inplace=True)
data['Tipo de contagio'].replace('En Estudio', 'En estudio', inplace=True)
data['Sexo'].replace('m', 'M', inplace=True)
data['Sexo'].replace('f', 'F', inplace=True)

# Ejercicio 1 
print('El numero de contagios es: ' + str(len(data)))

# Ejercicio 2
municipios = data['Nombre municipio'].unique()
print('El número de municipios afectados es: ' + str(len(municipios)))

# Ejercicio 3
print('Los Municipios afectados son: \n' + str(municipios))

# Ejercicio 4
atencion_casa = data[data['Ubicación del caso'] == 'Casa']
print('El numero de personas en casa es: ' + str(len(atencion_casa)))

# Ejercicio 5
recuperados = data[data['Recuperado'] == 'Recuperado']
print('El numero de personas recuperadas es: ' + str(len(recuperados)))

# Ejercico 6
fallecidas = data[data['Ubicación del caso'] == 'Fallecido']
print('El numero de personas fallecidas es: ' + str(len(fallecidas)))

# Ejercicio 7
tipos_casos = data.groupby('Tipos de contagio').count()
print(tipos_casos['ID'].sort_values(ascending=False))

# Ejercicio 8
departamentos = data['Nombre del departamento'].unique()
print('numero de departamentos afectados: ' + str(len(departamentos)))