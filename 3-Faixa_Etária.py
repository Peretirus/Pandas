# Solicita a idade do usuário
idade = int(input("Digite sua idade: "))

# Verifica a categoria da idade
if idade < 18:
    print("Você é menor de idade.")
elif idade <= 60:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")
