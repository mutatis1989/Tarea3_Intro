#Escribir un programa que pregunte el nombre
#del usuario en la consola y después de que el
#usuario lo introduzca muestre por pantalla
#<NOMBRE> tiene <n> letras, donde <NOMBRE> es
#el nombre de usuario en mayúsculas y <n> es el
#número de letras que tienen el nombre.

def main():
    nombre = input("Ingrese su nombre: ")
    nombre_mayusculas = nombre.upper()
    longitud_nombre = len(nombre)
    print(f"{nombre_mayusculas} tiene {longitud_nombre} letras.")
main()