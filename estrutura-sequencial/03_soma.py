# 3. Faça um Programa que peça dois números e imprima a soma.


# Pede o primeiro número
first_number: int = int(input('\nPor favor, digite um número: '))

# Pede o segundo número
second_number: int = int(input('\nPor favor, digite outro número: '))

# Imprima a soma
sum_value = first_number + second_number
print(f'\nA soma entre {first_number} e {second_number} é igual a {sum_value}\n')
