from datetime import datetime

# Lista de produtos com validade pré-definida
estoque = {
    "Leite": "2025-01-10",
    "Ovos": "2024-12-20",
    "Queijo": "2024-11-15",
    "Presunto": "2024-11-10",
    "Iogurte": "2024-10-30",
    "Maçã": "2024-09-25",
    "Banana": "2024-09-20",
    "Tomate": "2024-09-15",
    "Carne": "2024-08-05",
    "Peixe": "2024-08-01"
}

# Exibir a lista de produtos disponíveis
print("PRODUTOS DISPONÍVEIS ")
for produto, validade in estoque.items():
    print(f"- {produto} (Vence em {validade})")

# Usuário escolhe um produto
produto_escolhido = input("\nDigite o nome do produto que deseja atualizar: ").strip()

# Verifica se o produto está no estoque
if produto_escolhido in estoque:
    # Usuário insere a nova validade
    while True:
        nova_validade = input(f"Digite a nova validade do produto '{produto_escolhido}' (YYYY-MM-DD): ")
        try:
            validade_data = datetime.strptime(nova_validade, "%Y-%m-%d").date()
            estoque[produto_escolhido] = nova_validade  # Atualiza a validade
            break
        except ValueError:
            print(" Formato inválido! Digite no formato correto (YYYY-MM-DD).")
    
    # Verifica se o produto está vencido
    hoje = datetime.today().date()
    validade_atualizada = datetime.strptime(estoque[produto_escolhido], "%Y-%m-%d").date()
    
    print("\nSTATUS DO PRODUTO 📢")
    if validade_atualizada < hoje:
        print(f"{produto_escolhido.upper()} ESTÁ VENCIDO! (Venceu em {validade_atualizada})")
    else:
        print(f"{produto_escolhido} está bom para consumo até {validade_atualizada}.")
else:
    print("Produto não encontrado no estoque.")
