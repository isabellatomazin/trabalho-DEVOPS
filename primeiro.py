import time

print("Bem vindo ao contador PLUS.")

#While criado para que o usuário fique preso até colocar um número inteiro menor que 20.
while True:
    num = input("Você quer que eu conte até que número?")
    if num.isdigit() and int(num) <= 20:
        num = int(num)
        break
    else:
        print("Coloca um numero")

#Estrutura de repetição que contará até o número solicitado.
i = 0
while i <= num:
    print(i)
    i += 1
    time.sleep(1)
 