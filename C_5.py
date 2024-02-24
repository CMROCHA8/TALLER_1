import matplotlib.pyplot as plt

# Coordenadas para las letras del nombre "Cesar"
coordenadas = {
    'C': [(1, 0), (0, 0), (0, 4), (1, 4)],
    'e': [(3, 0), (2, 0),(2,2), (3, 2), (2, 4),(3,4)],
    's': [(3, 3), (2, 4), (1, 4), (1, 3), (2, 2), (3, 2), (3, 1), (2, 1), (1, 0), (2, 0), (3, 1)],
    'a': [(4, 0), (4.5, 1.5), (4, 2), (4.5, 3), (4, 4), (3, 2)],
    'r': [(5, 3), (5, 4), (6, 4), (6, 3), (5.5, 2)]
}

# Dibujar el nombre "Cesar"
plt.figure(figsize=(8, 4))
for letra, puntos in coordenadas.items():
    x, y = zip(*puntos)
    plt.plot(x, y, marker='o', label=letra)

# Ajustes del gráfico
plt.title('Nombre: Cesar')
plt.axis('equal')
plt.grid(True)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()