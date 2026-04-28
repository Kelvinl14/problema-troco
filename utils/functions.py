from collections import defaultdict

# Função para contar cédulas
def contar_cedulas(cedulas:int, valor:int) -> dict[list, dict]:
    cedulas.sort(reverse=True)
    resultado = []
    #qnt_ceulas = {} # uso de counter
    counter_cedulas = defaultdict(int)

    for cedula in cedulas:
        #qnt_ceulas[f"{cedula}"] = 0 # uso de counter
        while valor >= cedula:
            valor -= cedula
            resultado.append(cedula)
            #qnt_ceulas[f"{cedula}"] += 1
            counter_cedulas[f"{cedula}"] += 1

    if valor != 0:
        print(f"Não é possível fornecer o troco exato!\nFalta R${valor}")

    # return f"{resultado}\n{qnt_ceulas}"
    # return f"{resultado}\n{counter_cedulas}"

    return {"resultado": resultado, "contagem": counter_cedulas}

if __name__ == '__main__':
    cedulas = [25, 10, 5, 1]
    valor = 63

    print("Cedulas usadas:", contar_cedulas(cedulas, valor))