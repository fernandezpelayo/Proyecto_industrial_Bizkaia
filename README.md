# Análisis de Mantenimiento y Eficiencia Energética

Este proyecto analiza un dataset de mantenimiento industrial para identificar patrones de fallo y optimizar el consumo eléctrico de la maquinaria.

## Fase 1: Preparación y limpieza de datos (Python)

En esta primera etapa, he procesado los datos brutos utilizando Python y la librería Pandas para asegurar su calidad y extraer métricas de valor:

* **Limpieza y normalización:** He eliminado las columnas de identificación que no aportaban valor estadístico y he renombrado las variables para facilitar su manipulación.

* **Ingeniería de variables:** He calculado una estimación de consumo energético (kWh) combinando los datos de Torque y Velocidad.

* **Detección de ineficiencias:** He creado una lógica para identificar automáticamente las máquinas que operan con un gasto superior a la media de la planta.

## Próximas fases del proyecto
* Fase 2: Análisis avanzado mediante consultas SQL.
* Fase 3: Creación de un panel de control en Power BI.