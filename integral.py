# Calculo de área por aproximação geométrica à função seno com angulos de 0 à pi

# Importando biblioteca math
import math

# Input dos ângulos inicial e final dentro do intervalo de 0 à pi - ***ainda falta validar dados de entrada***
ai = float(input('\nDigite o angulo para o início do intervalo: '))
af = float(input('Digite o angulo para o final do intervalo: '))
    
# Quantas partes será dividido o intervalo para o calculo aproximado geométrico em áreas de retângulos - inteiro
n = int(input('Digite em quantas partes quer dividir o intervalo: '))
    
# Calculando áreas e somando
count = 0  
a = 0  
while count < n:
    b = (((af-ai)/n)*math.pi)/180
    xh = ((((af-ai)/(2*n))+(count*((af-ai)/n)))*math.pi)/180
    h = math.sin(xh)

    a = a + b*h
    count += 1

# fazer e exibir resultado do calculo por intregal defina para comparação

# Apresentação dos dados e resultado
print(f'\n\nIntervalos: {n}\nÂngulo Inicial: {ai}\nÂngulo Final: {af}\nÁrea: {a}\n')