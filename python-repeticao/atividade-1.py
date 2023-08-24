# Façc um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuario informe um valor válido.

i = float(input("Insira uma nota entre 0 e 10: "))

while i < (0) or i > (10):
    print(f"Sua nota é inválida, insira novamente!")

    i = float(input("Insira uma nota entre 0 e 10: "))
    
print(f"Fim do pograma!")

