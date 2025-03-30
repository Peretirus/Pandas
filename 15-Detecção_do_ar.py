import pandas as pd
import matplotlib.pyplot as plt

# Dados reais do IQA em Natal
dias = ["Hoje", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]
iqa = [13, 11, 17, 21, 10, 20, 33]  # Índice de Qualidade do Ar

# Criar DataFrame
df = pd.DataFrame({"Dia": dias, "IQA": iqa})

# Criar gráfico de linha
plt.plot(df["Dia"], df["IQA"], marker="o", linestyle="-", color="b", label="IQA")
plt.axhline(y=50, color="g", linestyle="--", label="Bom")
plt.axhline(y=100, color="r", linestyle="--", label="Ruim")
plt.xlabel("Dia")
plt.ylabel("Índice de Qualidade do Ar (IQA)")
plt.title("Previsão do IQA em Natal - Próximos Dias")
plt.legend()
plt.show()

# Mostrar os dias com IQA acima de 50 (indicativo de alerta)
print("Dias com IQA acima de 50:", df[df["IQA"] > 50])
