import pandas as pd

df = pd.read_csv('mantenimiento.csv')

print(df.head())
df.info()
print(df.isnull().sum())


#Eliminar las columnas 'ID' y 'Product ID' ya que no aportan información relevante
df_mantenimiento = df.drop(df.columns[[0, 1]], axis=1)


#Renombrar las columnas para facilitar su interpretación
df_mantenimiento.columns = [
    'Tipo', 'Temp_Aire', 'Temp_Proceso', 'Velocidad',

    'Torque', 'Desgaste', 'Fallo', 'Tipo_Fallo']

print(df_mantenimiento.head())