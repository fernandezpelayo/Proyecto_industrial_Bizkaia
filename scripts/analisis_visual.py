import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=BASE_DIR / ".env")
PASSWORD = os.getenv('DB_PASSWORD')

DB_URL = f'mysql+pymysql://root:{PASSWORD}@localhost:3306/mantenimiento_industrial'
engine = create_engine(DB_URL)
df = pd.read_sql("SELECT * FROM monitoreo_maquinas", con=engine)

# Traducción de categorías
traduccion_fallos = {
    'Power Failure': 'Fallo de Potencia',
    'Tool Wear Failure': 'Desgaste de Herramienta',
    'Overstrain Failure': 'Sobreesfuerzo',
    'Random Failures': 'Fallos Aleatorios',
    'Heat Dissipation Failure': 'Disipación de Calor',
    'No Failure': 'Sin Fallo'
}

df_fallos = df[df['Fallo'] == 1].copy()
df_fallos['Tipo_Fallo'] = df_fallos['Tipo_Fallo'].map(traduccion_fallos)

# Gráfica: Frecuencia de fallos
plt.figure(figsize=(12, 8))
ax = sns.countplot(data=df_fallos, x='Tipo_Fallo', hue='Tipo')

for p in ax.patches:
    if p.get_height() > 0:
        ax.annotate(f'{int(p.get_height())}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='center', 
                    xytext=(0, 9), 
                    textcoords='offset points')

plt.title('Análisis de Fallos: Frecuencia por Causa y Tipo de Máquina', fontsize=15)
plt.xticks(rotation=30, ha='right') 
plt.tight_layout()
plt.show()

# Gráfica: Matriz de correlación
plt.figure(figsize=(12, 10))
cols_analisis = [
    'Temp_Aire', 'Temp_Proceso', 'Velocidad', 
    'Torque', 'Desgaste', 'Consumo_Estimado', 'Fallo'
]

sns.heatmap(
    df[cols_analisis].corr(), 
    annot=True, 
    cmap='coolwarm', 
    fmt=".2f", 
    linewidths=0.5, 
    vmin=-1, vmax=1
)

plt.title('Matriz de Correlación: Sensores vs Fallos', fontsize=16)
plt.tight_layout()
plt.show()