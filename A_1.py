import numpy as np

# Función para realizar la suma de dos vectores
def suma_vectores(vec1, vec2):
    return vec1 + vec2

# Función para realizar la resta de dos vectores
def resta_vectores(vec1, vec2):
    return vec1 - vec2

# Función para realizar el producto punto entre dos vectores
def producto_punto(vec1, vec2):
    return np.dot(vec1, vec2)

# Función para realizar el producto cruz entre dos vectores
def producto_cruz(vec1, vec2):
    return np.cross(vec1, vec2)

# Función para realizar la división de dos vectores
def division_vectores(vec1, vec2):
    # Suponiendo que quieres dividir elemento por elemento
    return vec1 / vec2

# Vectores de ejemplo
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

# Suma de vectores
print("Suma:", suma_vectores(vector1, vector2))

# Resta de vectores
print("Resta:", resta_vectores(vector1, vector2))

# Producto punto
print("Producto Punto:", producto_punto(vector1, vector2))

# Producto cruz
print("Producto Cruz:", producto_cruz(vector1, vector2))

# División de vectores
print("División:", division_vectores(vector1, vector2))


