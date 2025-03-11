print("Um aluno se feriu? O que se deve fazer?")

ferimento = input("Fale o ferimento do aluno ")

if ferimento == "Leve":
    print("Higienizar o local com água e sabão.\n\n" 
          "Aplicar curativo ou gelo, se necessário.\n\n" 
          "Registrar o incidente em um relatório interno.\n\n" 
          "Informar os pais/responsáveis")

elif ferimento == "Moderado":
    print("Levar o aluno para a enfermaria ou setor de primeiros socorros.\n\n"
    "Aplicar os primeiros socorros (gelo, compressão, imobilização, etc.).\n\n"
    "Registrar o incidente em um relatório detalhado.\n\n"
    "Obrigatório avisar os pais/responsáveis e seguir orientação médica.\n\n"
    "Se necessário, encaminhar para um hospital ou posto de saúde.")
elif ferimento == "Grave":
    print("Acionar imediatamente o SAMU (192) ou serviço de emergência.\n\n"
    "Nunca mover o aluno (exceto em risco de vida, como incêndio).\n\n"
    "Aplicar os primeiros socorros se a equipe estiver treinada.\n\n"
    "Informar a direção da escola.\n\n"
    "Registrar o incidente oficialmente.\n\n"
    "Notificar os pais/responsáveis imediatamente.")
