# Google Colab
# https://colab.research.google.com/drive/1xpUHOEliaaUtd1-atYSWl_uACfmLBr-m?usp=sharing

# Importar Biblioteca Pandas
import pandas as pd

# Importar a Base de Dados
df = pd.read_excel("https://joaoricardao.wordpress.com/wp-content/uploads/2024/11/grupos_pesquisa.xlsx")

'''
# Criar Base de Dados
nome = ["joao", "elda", "petrus", "pietra"]
idade = [48, 49, 20, 15]
df = pd.DataFrame({"NOME":nome, "IDADE":idade})
'''

# Exibir DataFrame
df

# Exibir Cabeçalho
df.head()

# Exibir 20 primeiros registros
df.head(20)

# Exibir os Valores do DataFrame
df.values

# Exibir as Colunas do DataFrame
df.columns

# Exibir DataFrame Ordenado
df_sorted

# Exibir DataFrame Ordenado pelos 20 primeiros Registros
df_sorted.head(20)

# Exibir DataFrame Ordenado pelos 20 últimos Registros
df_sorted.tail(20)

#Ver se é crescente ou decrescente
ascending = [True] #Crescente
ascending = [False] #Decrescente

# Calcular e imprimir a média
print(f"Média de {coluna}:", df[coluna].mean())

# Calcular e imprimir a mediana
print(f"Mediana de {coluna}:", df[coluna].median())
