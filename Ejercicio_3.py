#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre
#<m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y
# <r> son el cociente y el resto de la división entera respectivamente.
def main():
    n = int(input("Introduzca un número (n): "))
    m = int(input("Introduzca un número (m): "))
    c = n // m
    r = n % m
    print(f"La división {n} entre {m} da un cociente {c} y un residuo {r}")
main()