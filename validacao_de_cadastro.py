print("Bem-vindo ao sistema de cadastro!")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
senha = input("Crie uma senha (mínimo 6 caracteres): ")

if idade < 18:
    print(f"Desculpe {nome}, você precisa ter 18 anos ou mais para se cadastrar ❌")
elif len(senha) < 6:
    print(f"Senha muito curta, {nome}! Mínimo 6 caracteres ❌")
else:
    print(f"Cadastro realizado com sucesso! Bem-vindo {nome} ✅")
