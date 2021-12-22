# c = str(input('Digite seu sexo [F/M]: ')).lower().strip()[0]
# while c != 'f' or c != 'm':
#     c = str(input('Digite seu sexo [F/M]: ')).lower().strip()[0]
#     if c == 'f' or c == 'm':
#         print('Fim!')
#         break
#################################Exercicio2##################################
# import random
# n = random.randint(0, 10)
# acerto = False
# count = 0
# while not acerto:
#     i = int(input('Digite um numero de 0 a 10: '))
#     count += 1
#     if n != i:
#         print('Escolha novamente!')
#     if n == i:
#         acerto = True
# print('O numero de tentativas ate a vitoria foi de {}'.format(count))


###############################Exercicio3###################################
# valor1 = int(input('Digite o primeiro valor: '))
# valor = int(input('Digite o segundo valor: '))
# while valor2 != 5:
#     print('''ESCOLHA UMA OPCAO:
#                     [1]SOMAR
#                     [2]MULTIPLICAR
#                     [3]MAIOR
#                     [4]NOVOS NÚMEROS
#                     [5] SAIR DO PROGRAMA
#           ''')
#     valor2 = int(input('Digite qual ação você quer tomar: '))
#     if valor2 == 1:
#         soma = valor + valor1
#         print('A soma de {} + {} é de {}'.format(valor, valor1, soma))
#     elif valor2 == 2:
#         soma = valor1 * valor
#         print('A soma de {} * {} é de {}'.format(valor, valor1, soma))
#
#     elif valor2 == 3:
#         if valor > valor1:
#             print('O maior valor entre {} e {} é {}'.format(valor, valor1, valor))
#
#         else:
#             print('O maior valor é {} e {} é {}'.format(valor1, valor, valor1))
#
#     elif valor or valor1 == 4:
#         print('O novo valor é: ')
#         valor1 = int(input('Digite o primeiro valor: '))
#         valor = int(input('Digite o segundo valor: '))
#     else:
#         print('Opcao invalida!!')
# print('Fim do programa!')
##########################################Exercicio4#############################

# numero = int(input('Digite um numero: '))
#
# soma = 1
# count = 1
# while count <= numero:
#     soma *= count
#     count += 1
# print('O valor fatorial de {} é {}'.format(numero, soma))

##########################################Exercicio5#############################

# p = int(input('Digite o primeiro numero: '))
# r = int(input('Digite a razão: '))
# s = 1
# termo = p
# while s <= 10:
#     print('{} =>'.format(termo), end='')
#     termo += r
#     s += 1
# print('FIM!')



##########################################Exercicio6#############################
# primeiro = int(input('Digite o primeiro numero:'))
# r = int(input('Digite a razão: '))
# s = 1
# total = 0
# mais = 10
# termo = primeiro
# while mais != 0:
#     total = total + mais
#     while s <= total:
#         print('{} =>'.format(termo), end='')
#         termo += r
#         s += 1
#     print('FIM?')
#     mais = int(input('Quantos termos voçê quer mais? '))
# print('O desafio terminou!! e voce pedeiu {} termos'.format(total))
#######################################Exercicio7###############################

#
# p = int(input('Digite o primeiro numero: '))
# t1 = 0
# t2 = 1
# print(' {} => {}'.format(t1, t2), end='')
# count = 3
# while count <= p:
#     num = t1 + t2
#     print(' => {}'.format(num), end='')
#     t1 = t2
#     t2 = num
#     count += 1
# print('\nAcabou!!')

#######################################Exercicio8###############################
# p = 0
# count = 0
# t = 0
# p = int(input('Digite o primeiro numero: '))
# while p != 999:
#     t += p
#     count += 1
#     p = int(input('Digite o primeiro numero: '))
# print('A quantidade de numeros que foi digitado foi de {}'.format(t))

#######################################Exercicio9###############################

c = 'S'
q = media = count = maior = menor = 0
while c in 'S':
    p = int(input('Digite o primeiro numero: '))
    q += p
    count += 1
    if count == 1:
        maior = menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p

    c = str(input('Deseja continuar [S/N]? ')).upper()
media = q / count
print('o valor da media é {}'.format(media))
print('O valor do maior valor é de {} e do menor valor é de {}'.format(maior, menor))

print('fim!')
