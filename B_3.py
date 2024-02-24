import math

def volumen_prisma(base, altura):
    return base * altura

def volumen_piramide(base, altura):
    return (1/3) * base * altura

def volumen_cono_truncado(radio_mayor, radio_menor, altura):
    return (math.pi * altura / 3) * (radio_mayor*2 + radio_mayor * radio_menor + radio_menor*2)

def volumen_cilindro(radio, altura):
    return math.pi * radio**2 * altura

def main():
    print("Calculo para volumenes")
    print("1. Prisma")
    print("2. Pirámide")
    print("3. Cono Truncado")
    print("4. Cilindro")

    opcion = int(input("Seleccione para calcular su volumen: "))

    if opcion == 1:
        base = float(input("Ingrese la base del prisma: "))
        altura = float(input("Ingrese la altura del prisma: "))
        volumen = volumen_prisma(base, altura)
        print("El volumen del prisma es:", volumen)

    elif opcion == 2:
        base = float(input("Ingrese la base de la pirámide: "))
        altura = float(input("Ingrese la altura de la pirámide: "))
        volumen = volumen_piramide(base, altura)
        print("El volumen de la pirámide es:", volumen)

    elif opcion == 3:
        radio_mayor = float(input("Ingrese el radio mayor del cono truncado: "))
        radio_menor = float(input("Ingrese el radio menor del cono truncado: "))
        altura = float(input("Ingrese la altura del cono truncado: "))
        volumen = volumen_cono_truncado(radio_mayor, radio_menor, altura)
        print("El volumen del cono truncado es:", volumen)

    elif opcion == 4:
        radio = float(input("Ingrese el radio del cilindro: "))
        altura = float(input("Ingrese la altura del cilindro: "))
        volumen = volumen_cilindro(radio, altura)
        print("El volumen del cilindro es:", volumen)

    else:
        print("Opción no válida. Por favor seleccione una opción del 1 al 4.")

if __name__ == "_main_":
    main()