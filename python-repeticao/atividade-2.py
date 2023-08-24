# 2- Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
        # obs: Podemos sobrescrever dados dentro de loops, por exemplo, pedindo dentro do loop para que o usuário atribua um novo valor à alguma variável.

usuario = str(input("Insira um nome de usuário: "))
senha = str(input("Insira uma senha: "))

while usuario == senha:
    print(f"Sua senha é iválida, insira novamente!")
    usuario = str(input("Insira um nome de usuário: "))
    senha = str(input("Insira uma senha: "))
print(f"Você foi cadastrado com sucesso!!")