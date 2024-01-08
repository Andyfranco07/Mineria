
import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('C:/Users/andyuwu/Documents/5pruebas/archivos_uwu/3.csv')


# Obtener la letra inicial de la primera columna
df['primera_letra'] = df['MOVIES'].str[0]

# Crear los subdatasets
subdataset_1 = df[df['primera_letra'].between('A', 'G', inclusive='both')]
subdataset_2 = df[df['primera_letra'].between('H', 'N', inclusive='both')]
subdataset_3 = df[df['primera_letra'].between('Ñ', 'Z', inclusive='both')]

# Guardar los subdatasets en archivos CSV separados
subdataset_1.to_csv('subdataset_1.csv', index=False)
subdataset_2.to_csv('subdataset_2.csv', index=False)
subdataset_3.to_csv('subdataset_3.csv', index=False)
