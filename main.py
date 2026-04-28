from utils.functions import contar_cedulas

def main():
    cedulas = [25, 10, 5, 1]
    valor = 63

    print("Cedulas usadas:", contar_cedulas(cedulas, valor))

main()