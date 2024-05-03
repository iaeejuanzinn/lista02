conta = int(input('digite o numero da sua conta: '))
saldo = float(input('digite seu saldo: '))
debito = float(input('digite o debito: '))
credito = float(input('digite o credito: '))
saldo_atual = saldo - (debito + credito)
if saldo_atual >= 0:
    print(saldo_atual,('saldo positivo'))
else:
    print(saldo_atual,('saldo negativo'))