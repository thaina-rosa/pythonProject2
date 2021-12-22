# emprestimo bancario
# casa = float(input('Digite o valor da casa que deseja comprar: '))
# salario = float(input('Digite o valor do seu salario: '))
# sa = (salario * 30) / 100
# if cal > sa:
    # print('Você não pode comprar esta casa seu emprestimo esta negado!')
# else:
#     print('Seu emprestimo foi aprovado')
# o valor n pode exceder 30% do salario

#######################################Exercicio2######################################

# num = int(input('Digite um numero : '))
# print('''posibilidades de conversão
            # [1] - conversao para binario
            # [2] - conversão para octal
            # [3] - conversão para hexadecimal'''
      # )
# base = int(input('Escolha a base de conversão: '))
# if base == 1:
    # print('A conversao de inteiro {}  binario é {}'.format(num, bin(num)[2:]))
# elif base == 2:
    # print('A conversao de inteiro {} para octal é {}'.format(num, oct(num)[2:]))

# elif base == 3:
    # print('A conversao de inteiro {} para hexadecimal é {}'.format(num, hex(num)[2:]))

# else:
    # print('Escolha uma opção valida!')

#######################################Exercicio3######################################

# valor = int(input('Digite o primeiro numero: '))
# valor2 = int(input('Digite o segundo numero: '))
# if valor > valor2:
#     print('O primeiro valor é maior!')
# elif valor2 > valor:
    # print('O segundo valor é o maior!')
# else:
#     print('Não existe valor maior, os dois sao iguais!')

#######################################Exercicio4######################################
# from datetime import date
# idade = int(input('Digite seu ano de nascimento '))
# soma = date.today().year - idade
# if soma == 18:
#     print('Voce precisa se alistar!')

# elif soma <= 18:
#     print('Voce esta na hora de se alistar! falta {}'.format(18 - soma))

# else:
#     print('Ja passou o tempo de se alistar, passou {} ano(s)'.format(soma - 18))

#######################################Exercicio5######################################

# nota1 = float(input('Digite a primeira nota: '))
# nota2 = float(input('Digite a primeira nota: '))
# media = (nota1 + nota2) / 2
# if media <= 4:
    # print('REPROVADO')

# elif media == 5 or media <= 6.9:
    # print('RECUPERAÇÃO')

# else:
#     print('APROVADO')

########################################Exercicio6######################################
# from datetime import date
# data = date.today().year
# idade = int(input('Digite seu ano de nascimento '))
# soma = data - idade
# if soma <= 9:
    # print('Classe: Mirim')
# elif soma == 10 or soma <= 14:
#     print('Classe: Infantil!')
# elif soma == 15 or soma <= 19:
#     print('Classe: Junior')
# elif soma == 20:
#     print('Classe: Sênior')
# else:
#     print('Classe: Master')

#######################################Exercicio7######################################
# print('[==================== jogo do triangulo ===============]')
# d1 = int(input('Digite a primeira retas:'))
# d2 = int(input('Digite a segunda retas:'))
# d3 = int(input('Digite a terceira retas:'))
# if d1 < d2 + d3 and d2 < d1 + d3 and d3 < d1 + d2:
    # print('Parabens voce tem um triangulo')
    # if d1 == d2 == d3:
    #     print('Você tem um triangulo Equilatero')

    # elif d1 != d2 != d3 != d1:
    #     print('Voce tem um triangulo Escaleno')
    # else:
    #     print('Você tem um triangulo Isóceles')
# else:
    # print('Ols lados nao se encaixam você nao pode formar um triangulo!')

#######################################Exercicio8######################################

# peso = int(input('Qual é o seu peso: '))
# altura = float(input('Digite sua altura: '))
# imc = peso/(altura**2)

# if imc <= 18.4:
#     print('Você esta abaixo do peso!')

# elif imc >= 18.5 and imc <=25:
#     print('Você esta no peso ideal!')

# elif imc >=25 and imc <=30:
#     print('Você esta com sobrepeso!')

# elif imc >30 and imc <=40:
#     print('Você esta com obesidade!')

# else:
#     print('Você esta com obesidade morbida!!')

#######################################Exercicio9######################################

# preco = int(input('Quanto custa o produto: '))
# print('''tipo de pagamentos:
#       1 - A vista no dinheiro,
#       2 - A vista cartao,
#       3 - 3x no cartao
#       4 - 2x no cartao''')
#
# tipo = int(input('Digite o tipo de pagamento '))
# vista = (preco * 10)/100
# cart = (preco * 5)/100
# juros = (preco * 20)/100
#
# if tipo == 1:
#     print('O pagamento a ser feito sera de {}'.format(preco - vista))
#
# elif tipo == 2:
#     print('O pagamento a ser feito sera de {}'.format(preco - cart))
# elif tipo == 3:
#     print('O pagamento a ser feito sera de {}'.format(preco + juros))
# elif tipo == 4:
#     print('O pagamento a ser feito sera de {}'.format(preco ))
# else:
#     print('escolha uma opcao valida')
#
#######################################Exercicio10######################################
# from random import randint
# print('[==================== jogo de jokenpô==================]')
# print('''
#           [0] - pedra
#           [1] - papel
#           [2] - tesoura''')
#
#
# opcao = ('Pedra', 'Papel', 'Tesoura')
# c = randint(0, 2)
# entrada = int(input('Qual é a sua jogada? '))
# print('O computador escolheu {}'.format(opcao[c]))
# print('O você escolheu {}'.format(opcao[entrada]))
# if c == 0:
#     if entrada == 0:
#         print('''Você empatou com a maquina
#      [Q][Q,]
#         L
#         === '''
#               )
#     elif entrada == 1:
#         print('''Parabens você ganhou!
#     [^] [^]
#        L
#        V''')
#     elif entrada == 2:
#         print('''Infelizmente você perdeu
#         [Q] [Q,]
#             L
#             ===''')
#     else:
#         print('Escolha uma opção valida!')
# elif c == 1:
#     if entrada == 1:
#         print('''Você empatou com a maquina
#      [Q][Q,]
#         L
#         === '''
#               )
#     elif entrada == 2:
#         print('''Parabens você ganhou!
#     [^] [^]
#        L
#        V''')
#     elif entrada == 0:
#         print('''Infelizmente você perdeu
#         [Q] [Q,]
#             L
#             ===''')
#     else:
#         print('Escolha uma opção valida!')
#
# elif c == 2:
#     if entrada == 2:
#         print('''Você empatou com a maquina
#      [Q][Q,]
#         L
#         === '''
#               )
#     elif entrada == 0:
#         print('''Parabens você ganhou!
#     [^] [^]
#        L
#        V''')
#     elif entrada == 1:
#         print('''Infelizmente você perdeu
#         [Q] [Q,]
#             L
#             ===''')
#     else:
#         print('Escolha uma opção valida!')
#
# else:
#     print('Escolha uma opcao valida!!')