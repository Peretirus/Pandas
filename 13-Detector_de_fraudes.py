import pandas as pd
import numpy as np

# Criando um dataset fictício de transações bancárias
data = {
    "ID": np.arange(1, 11),
    "Valor (R$)": [50, 200, 1500, 30, 5000, 70, 12000, 300, 450, 8000],
    "Tipo": ["Compra", "Compra", "Transferência", "Saque", "Transferência", 
             "Saque", "Transferência", "Compra", "Compra", "Transferência"]
}

df = pd.DataFrame(data)

# Definir um limite para transações suspeitas (> R$ 5000)
limite_suspeito = 5000

# Identificar transações suspeitas
df["Suspeita"] = df["Valor (R$)"].apply(lambda x: "SIM" if x > limite_suspeito else "NÃO")

print(df)
