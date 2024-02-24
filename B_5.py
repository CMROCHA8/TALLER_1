def continuar():
    while True:
        respuesta = input("¿Desea continuar? (Si/No): ")
        if respuesta.lower() == 'no':
            print("¡Hasta luego!")
            break
        elif respuesta.lower() == 'si':
            continue
        else:
            print("Por favor, responda con Si o No.")

if __name__ == "_main_":
    continuar()