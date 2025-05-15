#Escribir un programa que pregunte al usuario los
#números ganadores de la lotería primitiva, los
#almacene en una lista y los muestre por pantalla
#ordenados de menor a mayor.
#Utilice
#recursividad.
def pedir_numeros(cantidad, numeros=[]):
    if len(numeros) < cantidad:
        numero = int(input("Ingrese un número ganador: "))
        numeros.append(numero)
        return pedir_numeros(cantidad, numeros)
    return numeros

def main():
    cantidad = 3
    numeros = pedir_numeros(cantidad)
    numeros.sort()
    print("Números ganadores ordenados:")
    print(numeros)

main()
