import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# Datos de entrenamiento
X = np.array([[2.5], [1.5], [3.5], [3.8], [2.9], [5], [4.5], [5.5], [6.2], [6.8]])
y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

# Ajuste del modelo de regresión logística
model = LogisticRegression(C=1.0, solver='lbfgs')
model.fit(X, y)

# Generar puntos para la gráfica
x = np.linspace(0, 8, 100).reshape(-1, 1)
y_proba = model.predict_proba(x)[:, 1]

# Graficar los datos de entrenamiento y la función sigmoide
plt.figure(figsize=(8, 6))
plt.scatter(X, y, c=y, cmap=plt.cm.Paired, edgecolors='k')
plt.plot(x, y_proba, color='red', label='Función Sigmoide')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Regresión Logística')
plt.legend()
plt.grid(True)
plt.show()
