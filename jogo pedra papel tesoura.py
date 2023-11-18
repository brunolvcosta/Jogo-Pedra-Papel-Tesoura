print('BEM-VINDO AO PEDRA, PAPEL, TESOURA')
jogador1 = input("Digite o nome do jogador 1:\n")
jogador2 = 'Máquina'

#escolher pedra papel ou tesoura
while True:
    print('O JOGO VAI COMEÇAR')
    print(f'{jogador1}, escolha pedra, papel ou tesoura')

    escolha_jogador_1 = input(f'{jogador1} Digite pedra, papel ou tesoura:\n')
    
    import random
    escolhas = ['pedra', 'papel', 'tesoura']
    escolha_jogador_2 = random.choice(escolhas)

    print(f'{jogador1} escolheu {escolha_jogador_1} e {jogador2} escolheu {escolha_jogador_2}.')

#empate
    if escolha_jogador_1 == escolha_jogador_2:
        print('O jogo empatou, desejam jogar novamente?')
        jogar_novamente = input('Digite SIM para jogar novamente ou NÃO para parar de jogar\n')
        if jogar_novamente == 'não':
            print('Fim de jogo!')
            break
        else:
            print('Joguem mais uma vez!')

#vitoria ou derrota    
    else:
        if escolha_jogador_1 == 'pedra' and escolha_jogador_2 == 'tesoura' or escolha_jogador_1 == 'papel' and escolha_jogador_2 == 'pedra' or escolha_jogador_1 == 'tesoura' and escolha_jogador_2 == 'papel':
            print( 'Você venceu!')
            print('Fim de jogo')
            break
        else:
            print('Você perdeu!')
            print('Fim de jogo')
            break
  
        