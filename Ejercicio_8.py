#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
#en una lista y la muestre por pantalla. Utilice recursividad.
def main ():
    def mostrar_lista(lista, index=0):
        if index < len(lista):
            print(lista[index])
            mostrar_lista(lista, index + 1)

    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    print("Asignaturas del curso:")
    mostrar_lista(asignaturas)

main()