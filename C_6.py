import cv2
import numpy as np

# Cargar las imágenes de los logos
image_chevrolet = cv2.imread('chevrolet.png', 0)
image_hyundai = cv2.imread('Hiunday.png', 0)

# Función para encontrar contornos en una imagen
def find_contours(image):
    # Aplicar umbralización adaptativa para binarizar la imagen
    thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Encontrar contornos en la imagen binarizada
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar contornos en la imagen original
    image_contours = cv2.drawContours(image, contours, -1, (0), 3)

    return image_contours, contours

# Encontrar contornos en las imágenes de los logos
image_chevrolet_contours, contours_chevrolet = find_contours(image_chevrolet)
image_hyundai_contours, contours_hyundai = find_contours(image_hyundai)

# Obtener las coordenadas X e Y de los contornos
for contour in contours_chevrolet:
    x, y, w, h = cv2.boundingRect(contour)
    print(f'Coordenadas X e Y del logo Chevrolet: ({x}, {y})')

for contour in contours_hyundai:
    x, y, w, h = cv2.boundingRect(contour)
    print(f'Coordenadas X e Y del logo Hyundai: ({x}, {y})')