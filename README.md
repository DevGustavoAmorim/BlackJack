## Black Jack - Contagem de Carta
Este projeto implementa um jogo de Blackjack em Python, focando na prática do manuseio de funções, manipulação de listas, strings e lógica para um jogo fluido. A seguir, detalhes sobre a configuração, execução e lógica do jogo.
##
### Índice
1. Introdução
2. Uso
3. Regras do Jogo
4. Código:
    * Gerar e embaralhar o baralho
    * Funções principais
    * Lógica do jogo
5. Atualizações

##
### Introdução
Este projeto implementa um jogo de Blackjack, ao usuário uma partida contra a máquina (dealer). As regras serão as clássicas do jogo, apenas o dealer terá a contagem das cartas até o fim do programa.
##
### Regras do Jogos
1. **Objetivo**:
   * O jogador terá como objetivo, alcançar 21 pontos, ou um valor de pontos superior ao da máquina, caso o valor ultrapasse, a vitória será dada ao dealer.
2. **Cartas**:
   * Cartas numeradas de (2 a 10) mantêm seus pontos pelo número
   * Cartas de figura (J,Q,K) valem 10 pontos
   * Cartas ÀS (A), terão o valor inicial de 11, que será alterado para 1, caso a soma das cartas ultrapassem 21 pontos.
3. **Jogabilidade**:
   * O jogador inicia a partida, puxando cartas até alcançar 21 pontos, ou decidir passar a vez.
   * O dealer por sua vez, iniciara comprando uma carta, e dará sequencia na partida conforme estratégia programada (Hi-Lo Counting).
4. **Condições de vitória**:
   * A mão que ultrapassar 21 pontos perde imediatamente.
   * Se nenhuma mão ultrapssar 21, a mão com mais pontos, será a vencedora.
   * Empate se as mãos tiverem o mesmo valor.
##
### Código
#### Gerar e embaralhar o baralho

```
import random

cartas = list(range(2, 11))
letras = ['J', 'Q', 'K']
letra_A = ['A']
baralho = (cartas + letras + letra_A) * 4
random.shuffle(baralho)
```

Nesse trecho, foi criado um baralho padrão e embaralhado
##
### Funções Principais

```
def vencedor(mao_jogador, mao_maquina):
    if sum(mao_jogador) > 21:
        print('Jogador estourou os 21 pontos, máquina venceu!')
    elif sum(mao_maquina) > 21:
        print('Máquina estourou os 21 pontos, jogador venceu!')
    elif sum(mao_jogador) > sum(mao_maquina):
        print('Jogador venceu!')
    elif sum(mao_jogador) < sum(mao_maquina):
        print('Máquina venceu!')
    else:
        print('Empate!')

def nova_carta(mao):
    mao.append(baralho[0])
    del baralho[0]
    return baralho[0]

def verificar_cartas(mao):
    while sum(mao) > 21 and 11 in mao:
        mao[mao.index(11)] = 1

def decisao_maquina(mao):
    pontuacao_atual = sum(mao)
    cartas_favoraveis = sum(1 if 2 <= carta <= 6 else 0 if 7 <= carta <= 9 else -1 if 10 <= carta <= 11 else 0 for carta in mao)
    return pontuacao_atual < 17 or (pontuacao_atual >= 17 and cartas_favoraveis < 0)
```

  * def vencedor:
    * Verifica a pontuação e se a mão estourou de ponto
  * def nova_carta:
    * Transfere a primeira carta do baralho para a mão
  * def verificar_cartas:
    * Faz a correção dos pontos de todos os ÁS caso haja alguma carta com valor 11 e a mão tenha ultrapassado 21 pontos
##
### Lógica do jogo
```
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
            print('Pessoa jogando')
            print("""
                    1. Puxar uma carta
                    2. Para passar a vez
            """)
            
            while sum(mao_jogador) < 21:
                opcao_jogador = input('Insira a opcao desejada: ')
                if opcao_jogador == '1':
                    nova_carta(mao_jogador)
                    verificar_cartas(mao_jogador)
                    print(f"Mão de cartas: {mao_jogador}")
                    
                    if sum(mao_jogador) > 21:
                        print(f'Você perdeu! Total da mão {sum(mao_jogador)}')
                        break
                    elif sum(mao_jogador) == 21:
                        print('21 pontos')
                        break
                    
                elif opcao_jogador == '2':
                    break

            print('\nMáquina jogando')
            print(f"Mão de cartas: {mao_maquina}")
            
            nova_carta(mao_maquina)
            while True:
                chance_compra = decisao_maquina(mao_maquina)
                if sum(mao_jogador) > 21:
                    break
                
                if chance_compra:
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

            vencedor(mao_jogador, mao_maquina)
            del mao_jogador
            del mao_maquina

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
            print('\nOpção inválida!')
        break
    else:
        print('\n\nAcabaram as cartas do baralho!')
        break
```
Foi aplicado loops para manter a vez do jogador ou dealer, sempre preservando a regra de contagem de cartas e correção para os valores de ÁS.
O dealer acompanhará a contagem, de forma interrupta, até o encerramento do programa.
##
### Atualizações
No momento a estratégia do dealer, se resume na contagem Hei-lo, mas irei buscar outras alternativas para a realização da contagem. Buscarei alternativas com IA e outros métodos Estatisticos.

