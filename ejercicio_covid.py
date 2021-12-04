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
departamentos = data['Número de departamentos afectados: '].unique()
print('numero de departamentos afectados: ' + str(len(departamentos)))

# Ejercicio 9
print('Los departamentos afectados son: \n' + str(departamentos))

# Ejercicio 10
tipos_casos = data.groupby('Ubicación del caso').count()
print(tipos_casos['ID'].sort_values(ascending=False))

# Ejercicio 11
dep_conta = data.groupby('Departamentos con mas casos de contagiados: ').count()
top_10_dep = dep_conta['ID'].sort_values(ascending=False).head(10)
print(top_10_dep)

# Ejercicio 12
dep_falle = fallecidas.groupby('Departamentos con mas casos de fallecidos: ').count()
print(dep_falle['ID'].sort_values(ascending=False).head(10))

# Ejercicio 13
dep_recu = recuperados.groupby('Departamentos con mas casos de recuperados: ').count()
print(dep_recu['ID'].sort_values(ascending=False).head(10))

# Ejercicio 14
mun_conta = data.groupby('Municipios con mas casos de contagiados: ').count()
top_10_mun = mun_conta['ID'].sort_values(ascending=False).head(10)
print(top_10_mun)

# Ejercicio 15
mun_falle = fallecidas.groupby('Municipios con mas casos de fallecidos: ').count()
print(mun_falle['ID'].sort_values(ascending=False).head(10))

# Ejercicio 16
mun_recu = recuperados.groupby('Municipios con mas casos de recuperados: ').count()
print(mun_recu['ID'].sort_values(ascending=False).head(10))

# Ejercicio 17
print(dep_conta)
