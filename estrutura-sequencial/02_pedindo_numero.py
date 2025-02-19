# 2. Faça um Programa que peça um número e então mostre a mensagem "O número informado foi [número]".


# Pede um número
number: str = input('\nPor favor, digite um número: ')

# Mostra a mensagem
message: str = f"\nO número informado foi {number}\n"
print(message)