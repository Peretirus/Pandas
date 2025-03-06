
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

# Exibir DataFrame Ordenado pelos 30 primeiros Registros
df.sort_values(by="UF_GRUPO_PESQUISA",ascending=False).head(30)

# Exibir DataFrame Ordenado pelos 30 últimos Registros
df.sort_values(by="UF_GRUPO_PESQUISA",ascending=False).tail(30)

# Calcular e imprimir a média
df["ANO_FORMACAO"].mean()

# Calcular e imprimir a mediana
df["ANO_FORMACAO"].median()

# Calcular a soma acumulada e adicionar como uma nova coluna
df['cum_sum'] = df['QTD_ESTUDANTES_GRUPO'].cumsum()

# Calcular o máximo acumulado e adicionar como uma nova coluna
df['cum_max'] = df['QTD_ESTUDANTES_GRUPO'].cummax()

# Imprimir as primeiras linhas para visualizar
print(df[['QTD_ESTUDANTES_GRUPO', 'cum_sum', 'cum_max']].head())
