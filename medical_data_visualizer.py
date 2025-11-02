import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Pagina del desafio https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer

# 1. Lee los datos desde el archivo CSV y guardalos en un DataFrame llamado df.
df = None

# 2. Agrega una nueva columna llamada 'overweight'
# - Calcula el IMC (BMI) = peso (en kg) / (altura en metros)^2.
# - Si el valor es > 25, asigna 1 (sobrepeso); de lo contrario, 0.
# Pista: Considera las unidades de los datos.
df['overweight'] = None

# 3. Normaliza los datos para que 0 siempre signifique “bueno” y 1 signifique “malo”.


# 4. Para definir la siguiente funcion completa los pasos del 5 al 9.
def draw_cat_plot():
    # 5. Crea un DataFrame df_cat usando pd.melt().
    # Incluye como variables de valor ('value_vars') las columnas: ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    # y usa 'cardio' como variable del tipo identificador ('id_vars').
    df_cat = None


    # 6. Agrupalos datos de df_cat.
    # Agrupa por ['cardio', 'variable', 'value'] y cuenta las ocurrencias hay en cada grupo resultante.
    # Luego, renombra la columna de conteo a 'total' para que el gráfico funcione correctamente.
    # El resultado debe ser un DataFrame que contenga columnas: ['cardio', 'variable', 'value', 'total'].
    df_cat = None
    

    # 7. Crea el gráfico categórico con seaborn.
    # Usa sns.catplot() para mostrar los conteos de cada categoría (variable) divididos por 'cardio'.


    # 8. Guarda el resultado del gráfico en la variable 'fig'.
    fig = None


    # 9. Guarda la figura con tu nombre y catplot al final. (Ejemplo: Elena_Nito_catplot.png)
    fig.savefig('catplot.png')
    return fig


# 10. Para definir la siguiente funcion sigue los pasos del 11 al 16.
def draw_heat_map():
    # 11. Limpia el dataset (df_heat) aplicando filtros para eliminar datos incorrectos.
    # Mantén los registros donde:
    #  - ap_lo <= ap_hi  (la presión diastólica no puede ser mayor que la sistólica)
    #  - altura entre los percentiles 2.5 y 97.5
    #  - peso entre los percentiles 2.5 y 97.5
    df_heat = None

    # 12. Obten las correlaciones numéricas entre todas las variables.
    corr = None

    # 13. Pista: Usa np.triu(np.ones_like(corr, dtype=bool)).
    mask = None



    # 14. Crea una figura y un eje con plt.subplots(figsize=(x, y)).
    # Por ejemplo: fig, ax = plt.subplots(figsize=(12, 10))
    fig, ax = None

    # 15. Dibujar el mapa de calor con sns.heatmap().
    # - Usa la matriz de correlación 'corr'
    # - Aplica la máscara 'mask'
    # - Añade anotaciones

    # 16. Guarda la figura con tu nombre y heatmap al final. (Ejemplo: Elena_Nito_heatmap.png)
    fig.savefig('heatmap.png')
    return fig
