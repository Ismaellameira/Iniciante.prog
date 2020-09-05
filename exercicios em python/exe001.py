# programa que faz o calculo das areas das figuras planas.

# def quadrado(a):
#     return a**2

# def triangulo(b, h):
#     return b * h / 2

# def retangulo(b, h):
#     return b * h

# def circulo(r):
#     return 3.14 * r**2

# print(quadrado(4))
# print(triangulo(6, 3))
# print(retangulo(2, 4))
# print(circulo(3))

# O programa irá efetuar o calculo da quantidade de litros gastos em uma viagem,
# por um automóvel que gasta 12km/litro.
# Função para ler valores. Função para calcular a distancia. Função para calcular
# a quantidade de litros e Função para apresentar os resultados.
# def valores():
#     tempo = float(input("Digite o tempo da viagem: "))
#     velocidade = float(input("Digite a velocidade: "))
#     return tempo, velocidade

# def distancia(tempo, velocidade):
#     return tempo * velocidade

# def quant_litros(distancia):
#     return distancia / 12

# def imprima(velocidade, tempo, distancia, litros):
#     print('tempo:', tempo)
#     print('velocidade:', velocidade)
#     print('distancia:', distancia)
#     print('litros:', litros)

# t, v = valores()
# d = distancia(t, v)
# q = quant_litros(d)
# imprima(v, t, d, q)

# Programa que ira receber tres argumentos e ira somá-los.
# def adição(p, a, c):
#     return p + a + c

# print(adição(3, 5, 8))

# Programa que retorna positivo ou negativo.
# def decisao(x):
#     if x > 0:
#         print('P')
#     if x < 0 or x == 0:
#         print('N')

# decisao(8)

# Programa que pergunta idade e diz sua faixa etária.
# def pergunta(idade):
#     if idade >= 18:
#         print('Voce é adulto.')
#     if idade < 18 and idade >= 15:
#         print('Voce é adolescente')
#     if idade < 15 and idade >= 9:
#         print('Voce é criança')
# pergunta(17).