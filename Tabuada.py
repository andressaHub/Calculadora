print("=== Gerador de Tabuada ===")
numero = int(input("Digite um número para ver a tabuada: "))

# Incluido por Sérgioooo
for i in range(0, 11):
    print(f"{numero} x {i} = {numero * i}")

print("\n---")

print("=== Validador de Senha ===")
senha_correta = "qa123"
tentativas = 3

while tentativas > 0:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso liberado ✅")
        break
    else:
        tentativas -= 1
        print(f"Senha incorreta! Tentativas restantes: {tentativas}")

if tentativas == 0:
    print("Acesso bloqueado ❌")
