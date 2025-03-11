print("Um aluno se feriu? O que se deve fazer"?

# O usuário insere o Índice de Qualidade do Ar (AQI)
ferimento = int(input("Fale o ferimento do aluno"))

# Classificação da qualidade do ar
if ferimento <= "Leve":
    print("Higienizar o local com água e sabão." 
          "Aplicar curativo ou gelo, se necessário." 
          "Registrar o incidente em um relatório interno." 
          "Informar os pais/responsáveis")

elif ferimento <= "Moderado":
    print("Levar o aluno para a enfermaria ou setor de primeiros socorros."
    "Aplicar os primeiros socorros (gelo, compressão, imobilização, etc.)."
    "Registrar o incidente em um relatório detalhado."
    "Obrigatório avisar os pais/responsáveis e seguir orientação médica."
    "Se necessário, encaminhar para um hospital ou posto de saúde.")
elif aqi <= 150:
    print("Acionar imediatamente o SAMU (192) ou serviço de emergência."
    "Nunca mover o aluno (exceto em risco de vida, como incêndio)."
    "Aplicar os primeiros socorros se a equipe estiver treinada."
    "Informar a direção da escola."
    "Registrar o incidente oficialmente."
    "Notificar os pais/responsáveis imediatamente.")
