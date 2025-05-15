#Escriba un algoritmo que realice operaciones aritméticas (suma, resta,multiplicación y división).
def main ():
    print("Esta es una calculadora básica para la clase de Intro.")
a = int(input("Anote un número entero:"))
b = int(input("Anote otro número entero:"))
print("La suma de estos dos números es:", a + b)
print("La resta de estos dos números es:", a - b)
print("La multiplicación de estos dos números es:", a * b)
if b != 0:
    print("División",a/b)
else:
    print("No se puede dividir entre cero.")
main()