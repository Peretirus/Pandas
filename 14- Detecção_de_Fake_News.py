import pandas as pd

# Lista de palavras suspeitas
palavras_suspeitas = ["urgente", "chocante", "desesperador", "fake", "mentira"]

# Criar um dataset de notícias
noticias = {
    "ID": [1, 2, 3, 4, 5],
    "Texto": [
        "URGENTE! Novo imposto será cobrado de todos amanhã.",
        "Estudos mostram que exercício melhora a saúde.",
        "Chocante! Governo planeja algo terrível para o futuro.",
        "Cientistas descobrem nova vacina para doença rara.",
        "Mentira desmascarada! Veja o que políticos estão escondendo."
    ]
}

df = pd.DataFrame(noticias)

# Função para identificar fake news
def identificar_fake_news(texto):
    for palavra in palavras_suspeitas:
        if palavra.lower() in texto.lower():
            return "SIM"
    return "NÃO"

# Aplicar a função na coluna "Texto"
df["Fake News"] = df["Texto"].apply(identificar_fake_news)

print(df)
