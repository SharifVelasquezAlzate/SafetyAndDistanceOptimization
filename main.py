import pandas as pd

# Leemos el archivo "data.csv" que contiene los datos de acoso en Medellín
df = pd.read_csv('data.csv', sep=';')
# Como el archivo se encuentra separado por ";" y no ",", establecemos
# sep=";".

# Ahora imprimimos el dataframe obtenido
print(df.to_string())
