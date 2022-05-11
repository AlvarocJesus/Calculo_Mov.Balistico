from math import *

print("Bem vindo a calculadora de movimento balistico!")

x_i = float(input("Digite a posicao inicial em x: "))
y_i = float(input("Digite a posicao inicial em y: "))
v_i = float(input("Digite a velocidade inicial do lancamento: "))
t_d = float(input("Digite um instante de tempo qualquer apos o lancamento: "))
grav = -9.80
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
v_i_x = v_i * cos((alpha * pi) / 180)
v_i_y = v_i * sin((alpha * pi) / 180)

v_y = v_i_y + (grav * t_d)
v_x = v_i_x
modulo_max = sqrt((pow(v_x, 2) + pow(v_y, 2)))

print(f"Velocidade inicial no eixo X: {round(v_i_x,2)}")
print(f"Velocidade inicial no eixo Y: {round(v_i_y,2)}")
print(f"Velocidade final no eixo X no tempo {t_d}: {round(v_x,2)}")
print(f"Velocidade final no eixo Y no tempo {t_d}: {round(v_y,2)}")
print(f"Módulo da velocidade no tempo {t_d}: {round(modulo_max,2)}")

print("\n")

delta = v_i_y**2 - 4 * (grav / 2) * y_i
Tcomplementar1 = float((-v_i_y + sqrt(delta)) / grav)
Tcomplementar2 = float((-v_i_y - sqrt(delta)) / grav)

# Tempo
t_y_max = v_i_y / grav
t_x_max = (2 * t_y_max) + Tcomplementar2

print(f"Tempo de subida: {round(t_y_max,2)}")
print(f"Tempo de alcance: {round(Tcomplementar2,2)}")

print("\n")

# Posição
y_max = (pow(v_i_y, 2) / (2 * -grav)) + y_i
x_max = v_i_x * Tcomplementar2

x = x_i + (v_i_x * t_d)
y = y_i + (v_i_y * t_d) - (a_y * pow(t_d, 2)) / 2

print(f"Alcance máximo: {round(x_max,2)}")
print(f"Altura máximo: {round(y_max,2)}")
print(f"Posição no eixo X no tempo {t_d}: {round(x,2)}")
print(f"Posição no eixo Y no tempo {t_d}: {round(y,2)}")

print("\n")

# velocidade em posições especificas
# x máximo
v_y = v_i_y + grav * Tcomplementar2
v_x = v_i_x
modulo_x_max = sqrt((pow(v_x, 2) + pow(v_y, 2)))

print(f"Velocidade de X no alcance máximo: {round(v_x,2)}")
print(f"Velocidade de Y no alcance máximo: {round(v_y,2)}")
print(f"Módulo da velocidade no alcance máximo: {round(modulo_x_max,2)}")

print("\n")

# h máximo
v_h_y = 0
v_h_x = v_i_x
modulo_h_max = sqrt((pow(v_h_x, 2) + pow(v_h_y, 2)))

print(f"Velocidade de X na altura máxima: {round(v_h_x,2)}")
print(f"Velocidade de Y na altura máxima: {round(v_h_y,2)}")
print(f"Módulo da velocidade na altura máxima: {round(modulo_h_max,2)}")
