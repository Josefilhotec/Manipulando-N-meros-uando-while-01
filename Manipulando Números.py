# programa que leier vários números inteiros pelo teclado.
# No final da execução, mostre a soma e a média entre todos os valores e qual foi o maior e o menor valores lido.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
from time import sleep
from datetime import datetime
print('-=' * 20)
print('Calculando, soma, media, maior e menor valor.')
print('-=' * 20)
lista = []
contador = continuar = soma = media = 0
while continuar != 'N':
    numero = int(input('Digite um valor: '))
    lista.append(numero)
    contador += 1
    soma += numero
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        print('Opção errada')
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    print('~~~~' * 10)
media = soma / contador
print('Analizando os números, os resultados foram.')
sleep(2)
print('* A soma de todos os valores è {}'.format(soma))
print('* A media entre todos os valores é {:.2f}'.format(media))
print('* O maior valor da lista é {} e o menor valor da lista é {}'.format(max(lista), min(lista)))
print('-=' * 15)
print('Programa finalizado')
data_hora_atual = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
print(data_hora_atual)
