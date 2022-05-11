from math import *
from time import sleep

""" 
v0 = 28 m/s
alpha0 = 14.5º
altura de 56 cm do solo. 
td = 0.538 s
"""

print("Bem vindo a calculadora de movimento balistico!")

x_i = float(input("Digite a posicao inicial em x: "))
y_i = float(input("Digite a posicao inicial em y: "))
v_i = float(input("Digite a velocidade inicial do lancamento: "))
t_d = float(input("Digite um instante de tempo qualquer apos o lancamento: "))
grav = 9.80
a_x = 0
a_y = -grav
alpha = 0

# Validação dos dados de entrada
while True:
    if 0 <= alpha < 90:
        alpha = float(input("Digite o angulo de lancamento: "))
        break
    else:
        print("Valor do angulo invalido!!\nDigite um valor entre 0º e 89º")

print("\n")

# Velocidade
v_i_x = v_i * cos((alpha * pi) / 180)  # igual a velocidade final
v_i_y = v_i * sin((alpha * pi) / 180)

# Deu errado
v_y = v_i_y - (grav * t_d)
v_x = v_i_x
modulo_max = sqrt((pow(v_x, 2) + pow(v_y, 2)))

print(f"Velocidade inicial no eixo X: {v_i_x}")
print(f"Velocidade inicial no eixo Y: {v_i_y}")
print(f"Velocidade final no eixo X no tempo {t_d}: {v_x}")
print(f"Velocidade final no eixo Y no tempo {t_d}: {v_y}")
print(f"Módulo da velocidade no tempo {t_d}: {modulo_max}")

print("\n")

# Posição
beta = (pow(alpha, 2) * pi) / 180
print(f"Beta: {beta}")
x_max = (pow(v_i, 2) * sin(((2 * alpha) * pi) / 180)) / grav
y_max = pow(v_i, 2) * sin(pow((alpha * pi) / 180, 2)) / (2 * grav)

x = x_i + (v_i_x * t_d)
y = y_i + (v_i_y * t_d) - (grav * pow(t_d, 2)) / 2

print(f"Alcance máximo: {x_max}")
print(f"Altura máximo: {y_max}")
print(f"Posição no eixo X no tempo {t_d}: {x}")
print(f"Posição no eixo Y no tempo {t_d}: {y}")

print("\n")

# Tempo
t_y_max = (
    v_i * sin((alpha * pi) / 180)
) / grav  # """ (v_i * sin((alpha * pi) / 180)) """
t_x_max = 2 * t_y_max

print(f"Tempo de subida: {t_y_max}")
print(f"Tempo de alcance: {t_x_max}")

print("\n")

# velocidade em posições especificas
# x máximo
v_y = v_i_y - (grav * t_x_max)
v_x = v_i_x * t_d
modulo_x_max = sqrt((pow(v_x, 2) + pow(v_y, 2)))

print(f"Velocidade de X no alcance máximo: {v_x}")
print(f"Velocidade de Y no alcance máximo: {v_y}")
print(f"Módulo da velocidade no alcance máximo: {modulo_x_max}")

print("\n")

# h máximo
v_h_y = 0
v_h_x = v_i_x
modulo_h_max = sqrt((pow(v_h_x, 2) + pow(v_h_y, 2)))

print(f"Velocidade de X na altura máxima: {v_h_x}")
print(f"Velocidade de Y na altura máxima: {v_h_y}")
print(f"Módulo da velocidade na altura máxima: {modulo_h_max}")
