print("=== Calculadora de Despesas Mensais ===")


salario = float(input('Digite seu salário mensal: R$ '))
moradia = float(input('Gastos com moradia: R$ '))
alimentacao = float(input('Gastos com alimentação: R$ '))
transporte = float(input('Gastos com transporte: R$ '))

total_gastos = moradia + alimentacao + transporte
saldo = salario - total_gastos

print('\n==== RESUMO FINANCEIRO ====')
print(f'Salário: R$ {salario}')
print(f'Despesas: R$ {total_gastos}')
print(f'Saldo restante: R$ {saldo}')

if saldo > 0:
    print('Você tem dinheiro sobrando este mês!')
elif saldo == 0:
    print('Cuidado! Suas despesas estão exatamente iguais ao salário.')
else:
    print('Atenção você gastou mais do que ganha!')

