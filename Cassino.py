import numpy as np

dinheiro = 50
dado = np.random.randint(1, 7)  # Simulando o dado

if dado == 1:
    dinheiro -= np.random.randint(1, 4)
elif dado == 2 or dado == 3:
    dinheiro += np.random.randint(1, 4)
elif dado == 4 or dado == 5:
    dinheiro += np.random.randint(2, 6)
else:  # Caso o dado seja 6
    ganho = np.random.randint(5, 11)  # Número entre 5 e 10
    print(f"Ganhou R${ganho}")  # Exibir o valor ganho
    dinheiro += ganho  # Adicionar ao saldo

print(f"Dado: {dado}, Saldo atual: R${dinheiro}")
