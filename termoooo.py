from random import shuffle
import PySimpleGUI

with open('arquivo.txt', 'r') as f:
    lista_de_palavras = f.readlines()

lista_de_palavras = [x.strip() for x in lista_de_palavras]

shuffle(lista_de_palavras)

while True:
    n = 0
    palavra = lista_de_palavras[n]
    print(palavra)
    pontos = 0
    pontosp = 0
    pontos = pontos + pontosp
    chute = ''
    
    while chute != palavra:
        chute = input('\nDigite uma palavra: ')
        if chute == palavra:
            n = n+1
            print('acertou')
            pontosp = pontosp + 50

        elif chute != palavra:
            chances = 5
            chances = chances - 1
            for i in chute:
                impressao = i if i in palavra else ''
                impressao2 = '_' if i not in palavra else ''
                print(impressao + impressao2)
            if chances < 5:
                pontosp = chances*10
            if chances == 0:
                n = n+1
                print('você errou! a palavra era: ', palavra)

    print('sua pontuação atual é: ', pontosp)
