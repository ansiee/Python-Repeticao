# 3- Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuáro deve informar de qual numero ele deseja ver a tabuada.

numero = int(input("Insira um número de 1 a 10 para ver sua tabuada: "))

for i in range (11):
    resultado = numero * i
    print(f"{i}x{numero}={resultado}")
