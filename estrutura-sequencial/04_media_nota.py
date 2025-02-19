# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.


# Pede as 4 notas bimestrais
bimonthly_grades: float = 0
for i in range(4): 
    grade: float = float(input(f'\nPor favor, digite o {i + 1}º número: '))
    bimonthly_grades += grade

# Mostra a média
average: float = bimonthly_grades / (i + 1)
print(f'\nA média das notas bimestrais é {average}\n')
