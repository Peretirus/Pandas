import pandas as pd

# Criando um dataset de notas de estudantes
alunos = ["Ana", "João", "Maria", "Carlos", "Lucas"]
notas = [75, 40, 85, 55, 90]

df = pd.DataFrame({"Aluno": alunos, "Nota": notas})

# Classificação como "Aprovado" ou "Reprovado" baseada na nota
df["Status"] = ["Aprovado" if nota >= 60 else "Reprovado" for nota in df["Nota"]]

print(df)
