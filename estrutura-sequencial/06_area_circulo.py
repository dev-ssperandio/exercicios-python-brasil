# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math


radius: float = float(input('\nPor favor, digite o raio do círculo para calcular sua área: ')) 
area: float = math.pi * (radius ** 2)

print(f'\nA área do circulo que possui um raio de {radius} é igual a {area:.2f} metros quadrados.')
