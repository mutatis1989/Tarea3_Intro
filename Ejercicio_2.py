#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de
#masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es
# <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
def main():
    peso = float(input("Anote su peso en kg:"))
    estatura = float(input("Anote su altura en metros: "))

    imc = peso / (estatura ** 2)

    imc_redondeado = round(imc, 2)

    print(f"Su IMC es {imc_redondeado}")
main()