import pandas as pd

df = pd.read_csv('data/mantenimiento.csv')

df.info()
print(df.isnull().sum())


#Eliminar las columnas 'ID' y 'Product ID' ya que no aportan información relevante
df_mantenimiento = df.drop(df.columns[[0, 1]], axis=1)


#Renombrar las columnas para facilitar su interpretación
df_mantenimiento.columns = [
    'Tipo', 'Temp_Aire', 'Temp_Proceso', 'Velocidad',

    'Torque', 'Desgaste', 'Fallo', 'Tipo_Fallo']

print(df_mantenimiento.head())

#MÉTRICAS DE CONSUMO DE ENERGÍA

# Estimar el consumo (kWh) usando Torque y Velocidad como indicadores
df_mantenimiento['Consumo_Estimado'] = (
        df_mantenimiento['Torque'] * df_mantenimiento['Velocidad']) / 1000


# Marcar las máquinas que superan el consumo medio
media_consumo = df_mantenimiento['Consumo_Estimado'].mean()

df_mantenimiento['Gasto_Excesivo'] = (df_mantenimiento['Consumo_Estimado'] > media_consumo)


print(f"\nMedia de consumo calculada: {media_consumo:.2f}")
print(df_mantenimiento[['Tipo', 'Consumo_Estimado', 'Gasto_Excesivo']].head())

#Guardar el dataset para el análisis posterior
df_mantenimiento.to_csv('data/mantenimiento_procesado.csv', index=False)
