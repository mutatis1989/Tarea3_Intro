#Los teléfonos de una empresa tienen el siguiente
#formato prefijo-número-extension donde el
#prefijo es el código del país +34, y la extensión
#tiene dos dígitos (por ejemplo +34-913724710-
#56). Escribir un programa que pregunte por un
#número de teléfono con este formato y muestre
#por pantalla el número de teléfono sin el prefijo
#y la extensión.
def main ():
    codigo_pais = input ("Ingrese su código de país: +")
    telefono = input ("Ingrese su número de teléfono: ")
    extension = input ("Ingrese su extensión: ")
    print ("Su número de teléfono es: ", telefono)
    print ("Recuerde que su extensión es: ", extension)
    print ("Recuerde que su código de país es: ", codigo_pais)
    print ("+ " + codigo_pais +  telefono + "Ext. " + extension)
main ()
