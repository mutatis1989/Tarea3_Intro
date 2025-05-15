#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se
#cobran hasta finales de año, se te añaden al #balance final de tu cuenta de ahorros. Escribir
#un programa que comience leyendo la cantidad #de dinero depositada en la cuenta de ahorros,
#introducida por el usuario. Después el programa #debe calcular y mostrar por pantalla la cantidad
#de ahorros tras el primer, segundo y tercer años.#Redondear cada cantidad a dos decimales.
def main ():
    cantidad_inicial = float(input("Ingrese la cantidad de dinero que usted tiene depositada en su cuena de ahorros: "))
    tasa_interes = 0.04
    for año in range(1, 4):
        cantidad_inicial *= (1 + tasa_interes)
        print(f"Cantidad ahorrada tras el año {año}: {cantidad_inicial:.2f}")
main()