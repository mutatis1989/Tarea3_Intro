#Escribir un programa que almacene las
#asignaturas de un curso (por ejemplo
#Matemáticas, Física, Química, Historia y Lengua)
#en una lista, pregunte al usuario la nota que ha
#sacado en cada asignatura, y después las
#muestre por pantalla con el mensaje En
#<asignatura> has sacado <nota> donde
#<asignatura> es cada una des las asignaturas de
#la lista y <nota> cada una de las
#correspondientes notas introducidas por el
#usuario.Utilice recursividad.
def main ():
    def pedir_notas(materias, notas=[], index=0):
        if index < len(materias):
            nota = input(f"Ingrese la nota para {materias[index]}: ")
            notas.append(nota)
            return pedir_notas(materias, notas, index + 1)
        return notas

    def mostrar_notas(materias, notas, index=0):
         if index < len(materias):
            print(f"Su nota en  {materias[index]} es esta: {notas[index]}")
            mostrar_notas(materias, notas, index + 1)

    materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    notas = pedir_notas(materias)
    print("\nResumen de notas:")
    mostrar_notas(materias, notas)

main()
