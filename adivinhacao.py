import random
def jogar():



    print("**********************************")
    print("Bem vindo ao Jogo de Adivinhações!")
    print("**********************************")

    numero = 42
    tentativas = 0
    pontos = 1000

    print('Qual nível de dificuldade')
    print('(1) Fácil (2) Médio (3) Dificil ')

    nivel = int(input('Define o nível: '))

    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, tentativas))
        chute_str = input('Digite seu numero entre 1 a 100:')
        print('Voce digitou:', chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print('Voce deve digitar um numero entre 1 e 100!')
            continue

        acertou = numero == chute
        maior = chute > numero
        menor = chute < numero

        if not acertou:
            if (maior):
                print("Voce errou!O seu chute foi maior que o numero secreto")
            elif (menor):
                print('Voce errou!O seu chute foi menor que o numero secreto.')
            pontos_perdidos = abs(numero - chute)
            pontos = pontos - pontos_perdidos
        else:
            print('Voce acertou e fez {} pontos!'.format(pontos))
            break

    print('Fim de jogo!')
if(__name__ == '__main__'):
    jogar()