import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('3.csv')

# Eliminar la columna deseada
df = df.drop('STARS', axis=1)

# Guardar los cambios en un nuevo archivo CSV o sobrescribir el archivo original
df.to_csv('archivo_actualizado.csv', index=False)
