# Função para contar cédulas
def contar_cedulas(cedulas, valor):
    cedulas.sort(reverse=True)
    resultado = []
    qnt_ceulas = {}

    for cedula in cedulas:
        qnt_ceulas[f"{cedula}"] = 0
        while valor >= cedula:
            valor -= cedula
            resultado.append(cedula)
            qnt_ceulas[f"{cedula}"] += 1

    if valor != 0:
        print(f"Não é possível fornecer o troco exato!\nFalta R${valor}")

    return f"{resultado}\n{qnt_ceulas}"

cedulas = [25, 10, 5, 1]
valor = 63

print("Cedulas usadas:", contar_cedulas(cedulas, valor))