
#biblioteca para aleatorizar a lista de palavras
from random import shuffle
#biblioteca de decodificador de caracteres
import codecs

#abertura do banco de palavras com o codificador 
with codecs.open('arquivo.txt', 'r', encoding='utf-8') as f:
    lista_de_palavras = f.readlines()

#inserção das palavras em uma lista
lista = [x.strip() for x in lista_de_palavras]

#aleatorização da lista
shuffle(lista)

#impressão inicial
print('Adivinhe a Palavra Secreta\n')

#declaração da lista para as letras já digitadas no round
letras_escolhidas = []

#a pontuação inicial do jogador é 0
pontos = 0

#computador = palavra computada pela fila do sistema
computador = ''

#o jogador inicia cada round com 5 chances
chances = 5

#n = o número do caractere específico na fila, onde 0 é o inicial
n = 0

#contagem de palavras na lista
linhas = len(lista)

#loop inicial do jogo
while True:
    #declaração da palavra sorteada a partir do número da lista
    computador = lista[n]
    #lê o chute do jogador 
    chute = input('Chute uma palavra: ')
    #caso o chute seja igual à palavra sorteada
    if chute == computador:
        print('Você acertou a Palavra Secreta!\n')
        #o jogador ganha 50 pontos e a fila de palavras avança
        pontos += 50
        n += 1
        letras_escolhidas.clear()
        
    #caso o chute seja diferente da palavra sorteada 
    elif chute != computador:
        #as chances diminuem em um ponto
        chances -= 1
        for i in computador:
                #impressão da comparação entre as letras da palavra digitada e a palavra sorteada
                print(i if i in chute else '_')
        #armazenamento das letras que já foram digitadas em uma lista e organização por bubblesort
        for letra in chute:
            if letra not in letras_escolhidas:
                letras_escolhidas.append(letra)
        def bubbleSort(letras_escolhidas): 
            for i in range(len(letras_escolhidas)-1): 
                for j in range(0, len(letras_escolhidas)-i-1): 
                    if letras_escolhidas[j] > letras_escolhidas[j+1] : 
                        letras_escolhidas[j], letras_escolhidas[j+1] = letras_escolhidas[j+1], letras_escolhidas[j] 
        bubbleSort(letras_escolhidas) 

        print('você já digitou as letras:\n',letras_escolhidas)
        print(
            f'\nVocê errou. Ainda tem mais 4 chances')
        computador = lista[n]

        chute = str(input('\nChute uma palavra novamente: '))
        #caso o jogador acerte a palavra sorteada na segunda tentativa
        if chute == computador:
            print(
                f'\nVocê acertou na 2º tentativa. A palavra era {computador}, parabéns')
            #ele receberá quarenta pontos e a fila avançará
            pontos += 40
            n += 1
            letras_escolhidas.clear()
        #o processo se repete 
        elif chute != computador:
            chances = -1
            for i in computador:
                print(i if i in chute else '_')
            for letra in chute:
                if letra not in letras_escolhidas:
                    letras_escolhidas.append(letra)
            def bubbleSort(letras_escolhidas): 
                for i in range(len(letras_escolhidas)-1): 
                    for j in range(0, len(letras_escolhidas)-i-1): 
                        if letras_escolhidas[j] > letras_escolhidas[j+1] : 
                            letras_escolhidas[j], letras_escolhidas[j+1] = letras_escolhidas[j+1], letras_escolhidas[j] 
            bubbleSort(letras_escolhidas) 

            print('você já digitou as letras:\n',letras_escolhidas)
            print(
                f'\nVocê errou. Ainda tem 3 chances')
            computador = lista[n]

            chute = str(input('\nChute uma palavra novamente: '))
            if chute == computador:
                print(
                    f'\nVocê acertou na 3º tentativa. A palavra era {computador}, parabéns')
                pontos += 30
                n += 1
                letras_escolhidas.clear()
            elif chute != computador:
                chances = -1
                for i in computador:
                    print(i if i in chute else '_')
                for letra in chute:
                    if letra not in letras_escolhidas:
                        letras_escolhidas.append(letra)
                def bubbleSort(letras_escolhidas): 
                    for i in range(len(letras_escolhidas)-1): 
                        for j in range(0, len(letras_escolhidas)-i-1): 
                            if letras_escolhidas[j] > letras_escolhidas[j+1] : 
                                letras_escolhidas[j], letras_escolhidas[j+1] = letras_escolhidas[j+1], letras_escolhidas[j] 
                bubbleSort(letras_escolhidas) 

                print('você já digitou as letras:\n',letras_escolhidas)
                print(
                    f'\nVocê errou. Ainda tem 2 chances')
                computador = lista[n]
                chute = str(input('\nChute uma palavra novamente: '))
                if chute == computador:
                    print(
                        f'\nVocê acertou na 4º tentativa. A palavra era {computador}, parabéns')
                    pontos += 20
                    n += 1
                    letras_escolhidas.clear()
                elif chute != computador:
                    chances = -1
                    for i in computador:
                        print(i if i in chute else '_')
                    for letra in chute:
                        if letra not in letras_escolhidas:
                            letras_escolhidas.append(letra)
                    def bubbleSort(letras_escolhidas): 
                        for i in range(len(letras_escolhidas)-1): 
                            for j in range(0, len(letras_escolhidas)-i-1): 
                                if letras_escolhidas[j] > letras_escolhidas[j+1] : 
                                    letras_escolhidas[j], letras_escolhidas[j+1] = letras_escolhidas[j+1], letras_escolhidas[j] 
                    bubbleSort(letras_escolhidas) 
                    print('você já digitou as letras:\n',letras_escolhidas)
                    print(
                        f'\nVocê errou e possui apenas mais uma chance!')
                    computador = lista[n]

                    chute = str(input('\nChute uma palavra novamente: '))
                    if chute == computador:
                        print(
                            f'\nVocê acertou na 5º e última tentativa. A palavra era {computador}, parabéns')
                        pontos += 10
                        n += 1
                        letras_escolhidas.clear()
                    #caso o jogador não acerte em nenhuma das tentativas, o jogo para e a pontuação total é exibida.
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
