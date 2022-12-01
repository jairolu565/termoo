
#biblioteca para aleatorizar a lista de palavras
from random import shuffle
#biblioteca de decodificador de caracteres
import codecs

#abertura 
with codecs.open('arquivo.txt', 'r', encoding='utf-8') as f:
    lista_de_palavras = f.readlines()

lista = [x.strip() for x in lista_de_palavras]

shuffle(lista)

print('Adivinhe a Palavra Secreta\n')
pontos = 0
computador = ''
chances = 5
n = 0
linhas = len(lista)


while True:
    computador = lista[n]
    chute = str(input('Chute uma palavra: '))
    if chute == computador:
        print('Você acertou a Palavra Secreta!\n')
        pontos += 50
        n += 1
        
    elif chute != computador:
        chances -= 1
        for i in computador:
                print(i if i in chute else '_')
        print(
            f'\nVocê errou. Ainda tem mais 4 chances')
        computador = lista[n]

        chute = str(input('\nChute uma palavra novamente: '))
        if chute == computador:
            print(
                f'\nVocê acertou na 2º tentativa. A palavra era {computador}, parabéns')
            pontos += 40
            n += 1

        elif chute != computador:
            chances = -1
            for i in computador:
                print(i if i in chute else '_')
            print(
                f'\nVocê errou. Ainda tem 3 chances')
            computador = lista[n]

            chute = str(input('\nChute uma palavra novamente: '))
            if chute == computador:
                print(
                    f'\nVocê acertou na 3º tentativa. A palavra era {computador}, parabéns')
                pontos += 30
                n += 1
                
            elif chute != computador:
                chances = -1
                for i in computador:
                    print(i if i in chute else '_')
                print(
                    f'\nVocê errou. Ainda tem 2 chances')
                computador = lista[n]
                chute = str(input('\nChute uma palavra novamente: '))
                if chute == computador:
                    print(
                        f'\nVocê acertou na 4º tentativa. A palavra era {computador}, parabéns')
                    pontos += 20
                    n += 1

                elif chute != computador:
                    chances = -1
                    for i in computador:
                        print(i if i in chute else '_')
                    print(computador)
                    print(
                        f'\nVocê errou e possui apenas mais uma chance!')
                    computador = lista[n]

                    chute = str(input('\nChute uma palavra novamente: '))
                    if chute == computador:
                        print(
                            f'\nVocê acertou na 5º e última tentativa. A palavra era {computador}, parabéns')
                        pontos += 10
                        n += 1
                    elif chute != computador:
                        chances = -1
                        print(
                            f'\nVocê errou, e não tem mais nenhuma chance. A palavra era: {computador}')
                        print('\nSua pontuação total foi de ', pontos, 'pontos\n')
                        break
    print('Sua pontuação atual é de ', pontos, 'pontos\n')
    if n == linhas:
        break
    else:
        ''
