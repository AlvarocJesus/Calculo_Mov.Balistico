from math import *
from time import sleep

print("Bem vindo a calculadora de movimento balistico!")

x_i = float(input("Digite a posicao inicial em x: "))
y_i = float(input("Digite a posicao inicial em y: "))
v_i = float(input("Digite a velocidade inicial do lancamento: "))

t_d = float(input("Digite um instante de tempo qualquer apos o lancamento: "))
grav = 9.80
a_x = 0
a_y = -grav
alpha = 0

# Validaçao dos dados de entrada
while (True):
  if 0 <= alpha < 90:
    alpha = float(input("Digite o angulo de lancamento: "))
    break
  else:
    print("Valor do angulo invalido!!\nDigite um valor entre 0º e 89º")

# Variaveis globais
v_i_x= 0
v_i_y= 0
x_max= 0
y_max = 0
x = 0
y = 0
t_y_max= 0
t_x_max= 0

# Posiçao
def Posicao():
  x_max = (pow(v_i, 2) * sin(((2 * alpha) * pi) / 180)) / grav
  y_max = (pow(v_i, 2) * sin(((2 * alpha) * pi) / 180)) / (2 * grav)

  x = x_i + (v_i_x * t_d)
  y = y_i + (v_i_y * t_d) - (grav * pow(t_d, 2)) / 2

  print(f"Alçance maximo: {x_max}")
  print(f"Altura maximo: {y_max}")
  print(f"Posiçao no eixo X no tempo {t_d}: {x}")
  print(f"Posiçao no eixo Y no tempo {t_d}: {y}")


# Tempo
def Tempo():
  t_y_max = v_i_y / grav
  t_x_max = 2 * t_y_max

  print(f"Tempo de subida: {t_y_max}")
  print(f"Tempo de alcance: {t_x_max}")


# Velocidade
def Velocidade():
  v_i_x = v_i * cos((alpha * pi) / 180)  # igual a velocidade final
  v_i_y = v_i * sin((alpha * pi) / 180)

  v_y = v_i_y - (grav * t_d)
  v_x = v_i_x * t_d
  modulo_max = sqrt((pow(v_x, 2) + pow(v_y, 2)))

  print(f"Velocidade inicial no eixo X: {v_i_x}")
  print(f"Velocidade inicial no eixo Y: {v_y_x}")
  print(f"Velocidade final no eixo X no tempo {t_d}: {v_x}")
  print(f"Velocidade final no eixo X no tempo {t_d}: {v_y}")
  print(f"Módulo da velocidade no tempo {t_d}: {modulo_max}")


# velocidade em posicoes especificas
def Posicao_Especifica():
  # x maximo
  v_y = v_i_y - (grav * t_x_max)
  v_x = v_i_x * t_d
  modulo_x_max = sqrt((pow(v_x, 2) + pow(v_y, 2)))

  print(f"Velocidade de Y no alcance máximo: {v_y}")
  print(f"Velocidade de X no alcance máximo: {v_x}")
  print(f"Módulo da velocidade no alcance máximo: {modulo_x_max}")

  # h maximo
  v_h_y = 0
  v_h_x = v_i_x * t_y_max
  modulo_h_max = sqrt((pow(v_h_x, 2) + pow(v_h_y, 2)))

  print(f"Velocidade de Y na altura máxima: {v_h_y}")
  print(f"Velocidade de X na altura máxima: {v_h_x}")
  print(f"Módulo da velocidade na altura máxima: {modulo_h_max}")

while True:
  escolha = int(input('''
Digite:
1 - Para calcular as posicoes
2 - Para calcular as velocidades
3 - para calcular as velocidades em funcao do tempo no alcance maximo e na altura maxima
4 - para calcular as velocidades em funcao do tempo na 
  '''))

  if escolha == 1:
    Posicao()
  elif escolha == 2:
    Velocidade()
  elif escolha == 3:
    Posicao_Especifica()
  elif escolha == 4:
    Tempo()
  elif escolha == 0:
    print("Ate a proxima!")
    print('...')
    sleep(1)
    break
  elif escolha != 1 or escolha != 2 or escolha != 3 or escolha != 4 or escolha != 0:
    print('Digite uma opção valida!')