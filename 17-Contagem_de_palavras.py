import string

# Texto para análise
texto = input("Digite um texto para análise de palavras: ")

# Convertendo o texto para minúsculas
texto = texto.lower()

# Removendo pontuações
for pontuacao in string.punctuation:
    texto = texto.replace(pontuacao, "")

# Separando em palavras
palavras = texto.split()

# Contando as ocorrências de cada palavra
contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

# Exibindo o resultado
print("\nContagem de palavras:")
for palavra, contagem in contagem_palavras.items():
    print(f"{palavra}: {contagem}")
