# from time import sleep
# for c in range(10,  -1, -1,):
#     print(c)
#     sleep(1)
# print('Feliz ano novo!')
############################Exercicio2##########################
# for c in range(1, 51, 2):
#     print(c)

############################Exercicio3##########################
# soma = 0
# con = 0
# for c in range(1, 501):
#     if c % 2 == 1 and c % 3 == 0:
#         con += 1
#         soma += c
# print('A soma de todos os {} numeros inpares divisiveis por três é: {}'.format(con, soma))

############################Exercicio4##########################
# numero = int(input('Digite um numero: '))
# for n in range(0, 11):
#     t = numero * n
#     print('{} x {} = {}'.format(numero, n, t))

############################Exercicio5##########################

# count =0
# for c in range(0, 6,):
#     r = int(input('Digite seis valores: '))
#     if r % 2 == 0:
#         count += r
#         print('A soma dos valores informados sao: {}'.format(count))
#

############################Exercicio6##########################

# p = int(input('Digite o primeiro numero: '))
# r = int(input('Digite a razão: '))
# s = p + (10 - 1) * r
# print('-' * 20)
# for c in range(p, s + r, r):
#     print('--> {}'.format(c))
# print('fim!!!')

############################Exercicio7##########################
# tive dificuldade
# i = int(input('Digite um numero: '))
# m = 0
# for c in range(1, i + 1):
#     if i % c == 0:
#         print('\033[33m', end='')
#         m += 1
#     else:
#         print('\033[31', end='')
#     print('{}'.format(c), end='')
# print('\n\033[mO número {} foi divisivel {} vezes'.format(i, m))
# if m == 2:
#     print('E por isso ele é Primo!')
# else:
#     print('Por isso ele nao é Primo!')
############################Exercicio8##########################
# p = str(input('Digite uma frase: ')).strip().lower()
# palavras = p.split()
# junto = ''.join(palavras)
# i = junto[::-1]
# if i == junto:
#     print('Essa palavra {} é um palindromo'.format(i))
#
# else:
#     print('Essa palavra {} nao é um palindromo'.format(i))

############################Exercicio9##########################
# from datetime import date
#
# count = 0
# ano1 = date.today().year
# count1 = 0
# for a in range(7):
#     ano = int(input('Digite seu ano de nascimento: '))
#     idade = ano1 - ano
#
#     if idade <= 17:
#         count += 1
#         print('Voce ainda é muito novo! O numero de pessoas novas é de {}'.format(count))
#
#     else:
#         count1 += 1
#         print('Voce ja atingiu a maior idade! O numero de pessoas que ja passaram da maior idade é de {}'.format(count1))

############################Exercicio10##########################
# import math
# soma = 0
# idade = 0
# maiori = 0
# maisv = ''
# count = 0
#
# for i in range(0, 4):
#     n = str(input('Digite seu nome: ')).lower()
#     id = int(input('Digite sua idade: '))
#     s = str(input('Digite seu sexo [M/F]: ')).lower()
#     print(20 * '=')
#     soma += id
#     if i == 1 and s == 'm':
#         maiori = id
#         maisv = n
#     if s == 'm' and id > maiori:
#         maiori = id
#         maisv = n
#
#     if id < 20 and s == 'f':
#         count += 1
#
# idade = soma / 4
# print('A media de idade do grupo é de {}'.format(idade))
# print('O homem mais velho se chama {} e tem {} anos'.format(maisv, maiori))
# print('O numero de mulheres com menos de 20 anos é de {}'.format(count))
############################Exercicio11##########################
# mai = 0
# men = 0
# for i in range(1, 6):
#     p1 = float(input('Peso da {} pessoa : '.format(i)))
#     if i == 1:
#         mai = p1
#         men = p1
#
#     else:
#         if p1 > mai:
#             mai = p1
#         if p1 < men:
#             men = p1
#
# print('O maior peso lido até o momento foi kg {}'.format(mai))
# print(' O menor numero lido até o momento foi o de kg {}'.format(men))
