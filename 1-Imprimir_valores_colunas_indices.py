import pandas as pd  # Importação única do pandas

# Criando corretamente um DataFrame
homelessness = pd.DataFrame({
    "region": ["East South Central", "Pacific", "Mountain", "West South Central", "Pacific"],
    "state": ["Alabama", "Alaska", "Arizona", "Arkansas", "California"],
    "individuals": [2570.0, 1434.0, 7259.0, 2280.0, 109008.0],
    "family_members": [864.0, 582.0, 2606.0, 432.0, 20964.0],
    "population": [4887681, 735139, 7158024, 3009733, 39461588]
})

# Imprime os valores do DataFrame
print(homelessness.values)

# Imprime os nomes das colunas do DataFrame
print(homelessness.columns)

# Imprime o índice das linhas do DataFrame
print(homelessness.index)
