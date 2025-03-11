# Importa matplotlib.pyplot como plt
import matplotlib.pyplot as plt

# Lista de anos e população (exemplo)
year = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020] # Ano
pop = [2.5, 3.0, 3.7, 4.4, 5.3, 6.1, 6.9, 7.8]  # População em bilhões

# Imprime o último item de year e pop
print(year[-1])  # Último ano da lista
print(pop[-1])   # Última população da lista

# Faz um gráfico de linha: year no eixo x, pop no eixo y
plt.plot(year, pop)

# Adiciona rótulos aos eixos e título
plt.xlabel("Ano")
plt.ylabel("População (bilhões)")
plt.title("Crescimento da População Mundial")

# Exibe o gráfico com plt.show()
plt.show()
