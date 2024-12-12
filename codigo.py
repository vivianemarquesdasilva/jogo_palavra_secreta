import random
import os

from temas import lista_palavras

print('___ JOGO DA PALAVRA SECRETA ___')

print('\nTemas:')
print(' [1]Natureza\n [2]Música\n [3]Esportes\n [4]Animais\n [5]Profissões')

tema_escolhido = ''
while True:
    tema_escolhido = input('Escolha um tema: ').strip()

    numeros_aceitos = '12345'
    if tema_escolhido not in numeros_aceitos or tema_escolhido == '':
        print('Por favor digite um número de 1 a 5.')
        continue
    else:
        break

tema_da_partida = []
match tema_escolhido:
    case '1':
        tema_da_partida = lista_palavras[0]['natureza'].copy()                       
    case '2':
        tema_da_partida = lista_palavras[1]['musica'].copy()         
    case '3':
        tema_da_partida = lista_palavras[2]['esportes'].copy()         
    case '4':
        tema_da_partida = lista_palavras[3]['animais'].copy()         
    case '5':
        tema_da_partida = lista_palavras[4]['profissoes'].copy()

palavra_secreta = random.choice(tema_da_partida)
palavra_oculta = ['_'] * len(palavra_secreta)

os.system('cls')
print('--ADIVINHE A PALAVRA SECRETA--')

tentativas = 6
lista_letras_digitadas = []
print(" ".join(palavra_oculta))
while True:    
    print(f'\nVocê têm {tentativas} tentativas:')
    print(f'Letras que você já digitou: {sorted(lista_letras_digitadas)}')
    letra_digitada = input('Digite uma letra: ').strip()

    if letra_digitada not in lista_letras_digitadas:
        lista_letras_digitadas.append(letra_digitada)

    if letra_digitada in palavra_secreta:
        for i, l in enumerate(palavra_secreta):
            if l == letra_digitada:
                palavra_oculta[i] = letra_digitada
    else:
        tentativas -= 1

    os.system('cls')
    print(" ".join(palavra_oculta))

    if tentativas == 0:
        print('\nInfelizmente, você perdeu :(')
        print(f'A palavra era "{palavra_secreta}".')
        break

    if '_' not in palavra_oculta:
        print('\nParabéns!, você venceu :)')
        break