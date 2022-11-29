from random import shuffle
import PySimpleGUI as sg

with open('arquivo.txt', 'r') as f:
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
    print(computador)

    sg.theme('DarkAmber')

    layout = [  [sg.Text('Advinhe a palavra!')],
                [sg.InputText()],
                [sg.Text('Pontos: ',pontos)],
                [sg.Button('Ok'), sg.Button('Fechar')] ]

    window = sg.Window('Quote', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Fechar':
            break
        window.close()
        if (values[0]) == computador:
            print('Você acertou a Palavra Secreta!\n')
            pontos += 50
            n += 1
        elif (values[0]) != computador:
            chances -= 1
            layout = [  [sg.Text('Advinhe a palavra!')],
                [sg.InputText()],
                [sg.Text('\nVocê errou. Ainda tem mais 4 chances')],
                [sg.Button('Ok'), sg.Button('Cancel')] ]
            window = sg.Window('Quote', layout)
            computador = lista[n]
            
            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED or event == 'Fechar':
                    break
                window.close()
                if (values[0]) == computador:
                    print('Você acertou a Palavra Secreta!\n')
                    pontos += 50
                    n += 1
                elif (values[0]) != computador:
                    chances -= 1
                    layout = [  [sg.Text('Advinhe a palavra!')],
                        [sg.InputText()],
                        [sg.Text('\nVocê errou. Ainda tem mais 3 chances')],
                        [sg.Button('Ok'), sg.Button('Cancel')] ]
                    window = sg.Window('Quote', layout)
                    computador = lista[n]

                    while True:
                        event, values = window.read()
                        if event == sg.WIN_CLOSED or event == 'Fechar':
                            break
                        window.close()
                        if (values[0]) == computador:
                            print('Você acertou a Palavra Secreta!\n')
                            pontos += 50
                            n += 1
                        elif (values[0]) != computador:
                            chances -= 1
                            layout = [  [sg.Text('Advinhe a palavra!')],
                                [sg.InputText()],
                                [sg.Text('\nVocê errou. Ainda tem mais 2 chances')],
                                [sg.Button('Ok'), sg.Button('Cancel')] ]
                            window = sg.Window('Quote', layout)
                            computador = lista[n]

                            while True:
                                event, values = window.read()
                                if event == sg.WIN_CLOSED or event == 'Fechar':
                                    break
                                window.close()
                                if (values[0]) == computador:
                                    print('Você acertou a Palavra Secreta!\n')
                                    pontos += 50
                                    n += 1
                                elif (values[0]) != computador:
                                    chances -= 1
                                    layout = [  [sg.Text('Advinhe a palavra!')],
                                        [sg.InputText()],
                                        [sg.Text('\nVocê errou. Ainda tem mais 1 chance')],
                                        [sg.Button('Ok'), sg.Button('Cancel')] ]
                                    window = sg.Window('Quote', layout)
                                    computador = lista[n]

    
            
        print('Sua pontuação atual é de ', pontos, 'pontos\n')
        if n == linhas:
            break
        else:
            ''
