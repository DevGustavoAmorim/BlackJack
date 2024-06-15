import random
import os

#___________ Cartas_do_baralho____________________
cartas = list(range(2,11))
letras = ['J', 'Q', 'K']
letra_A = ['A']
baralho = (cartas + letras + letra_A) * 4
random.shuffle(baralho)


#__________Alterando_as_cartas_de_letras_valor_10______________________
for i, carta in enumerate(baralho):
    if carta in letras:
        baralho[i] = 10
    if carta in letra_A:
        baralho[i] = 11

# Puxando a carta e excluindo do baralho

def vencedor(mao_jogador,mao_maquina):
    if sum(mao_jogador) > 21:
        return print('Jogador estourou os 21 pontos, máquina venceu!')
    
    elif sum(mao_maquina) > 21:
        return print('Máquina estourou os 21 pontos, jogador venceu!')
    
    elif sum(mao_jogador) > sum(mao_maquina):
        return print('Jogador venceu!')
    
    elif sum(mao_jogador) < sum(mao_maquina):
        return print('Máquina venceu!')
    
    else:
        return print('Empate!')

def nova_carta(mao):
    """Adiciona uma nova carta à mão do jogador"""
    mao.append(baralho[0])
    del baralho[0]
    return baralho[0]

def verificar_cartas(mao):
    """Verifica se a mão do jogador excede 21 e ajusta o valor do Ás, se necessário"""
    while sum(mao) > 21 and 11 in mao:
        mao[mao.index(11)] = 1

def decisao_maquina(mao):
    """Determina se a máquina deve continuar comprando cartas"""
    pontuacao_atual = sum(mao)  
    cartas_favoraveis = sum(1 if 2 <= carta <= 6 else 0 if 7 <= carta <= 9 else -1 if 10 <= carta <= 11 else 0 for carta in mao)

    return pontuacao_atual < 17 or (pontuacao_atual >= 17 and cartas_favoraveis < 0)  

# ____________________Iniciando_Partida_________________________
while True:
    if len(baralho) > 6:
        mao_jogador = []
        mao_maquina = []

        print("""
            0. Cancelar
            1. Começar a partida
    """)
        opcao = input('Insira a opcao desejada: ')
        
        if opcao == '0':
            print('Jogo cancelado')
            break
        if opcao == '1':
            #____Começando o jogo____
            print('Pessoa jogando')
            print("""
                    1. Puxar uma carta
                    2. Para passar a vez
            """)
            
            while sum(mao_jogador) < 21:
                opcao_jogador = input('Insira a opcao desejada: ')
                    # PUXAR CARTA
                if opcao_jogador == '1':
                    nova_carta(mao_jogador)
                    verificar_cartas(mao_jogador)
                    print(f"Mão de cartas: {mao_jogador}")
                    
                    if sum(mao_jogador) > 21:
                        print(f'Voce perdeu! Total da mão {sum(mao_jogador)}')
                        break
                    elif sum(mao_jogador) == 21:
                        print('21 pontos')
                        break
                    
                    #PASSAR A VEZ
                elif opcao_jogador == '2':
                    break
    #___________________________Maquina_____________________________________________________
            print('\nMaquina jogando')
            nova_carta(mao_maquina)
            print(f"Mão de cartas: {mao_maquina}")
            
            while True:
                chance_compra = decisao_maquina(mao_maquina)
                if sum(mao_jogador) > 21:
                    break
                
                #____Maquina vai decidir se compra__
                if chance_compra:
                    # Maquina começa a jogar
                    nova_carta(mao_maquina)
                    verificar_cartas(mao_maquina)
                    print(f"Mão de cartas: {mao_maquina}")
                    if sum(mao_maquina) > 21:
                        print(f'Máquina perdeu! Total da mão {sum(mao_maquina)}')
                        break
                    if sum(mao_maquina) > sum(mao_jogador):
                        break
                    elif sum(mao_maquina) == 21:
                        print('21 pontos')
                        break
                else:
                    break

            # Verificação do vencedor após a máquina parar de comprar
            vencedor(mao_jogador,mao_maquina)
            del mao_jogador
            del mao_maquina

            #____Jogar Novamente___
            while True:
                x = input("Deseja jogar novamente? (s/n): ").lower()
                if x == 'n':
                    break
                elif x == 's':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
            if x == 'n':
                break
            elif x == 's':
                continue

        else:
            print('\nOpcao inválida!')
        break
    else:
        print('\n\nAcabou as cartas do baralho!')
        break