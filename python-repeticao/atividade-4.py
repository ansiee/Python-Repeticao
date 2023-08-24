# 4- Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxa de crescimento de 1.5%. Facça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, manidas as taxas de crescimento.

A = 80.000
B = 200.000
ano = 0

while B > A:
    A += A * 0.03
    B += B * 0.015
    ano += 1
print(f"A população do pais ")