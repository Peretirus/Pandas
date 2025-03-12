# Lista de doações feitas por várias pessoas (em reais)
doacoes = [150.0, 50.5, 200.0, 75.25, 120.0]

# Usando enumerate para exibir as doações
for index, doacao in enumerate(doacoes):
    print("Pessoa " + str(index) + " doou: R$" + str(doacao))
