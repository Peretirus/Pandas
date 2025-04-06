import matplotlib.pyplot as plt

numero = int(input("Digite um número para ver a tabuada: "))
valores = []
resultados = []

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    valores.append(f"{numero}x{i}")
    resultados.append(resultado)

# Plotando a tabuada
plt.bar(valores, resultados, color="skyblue")
plt.title(f"Tabuada do {numero}")
plt.xlabel("Multiplicações")
plt.ylabel("Resultados")
plt.grid(axis="y")
plt.tight_layout()
plt.show()
