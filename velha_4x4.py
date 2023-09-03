# Imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 15)

# Iniciar o tabuleiro 4x4
tabuleiro = [[" " for i in range(4)] for i in range(4)]

# Jogadores
jogadores = {1: "X", 2: "O"}

# Iniciar o jogo com um maximo de 16 jogadas
jogador_atual = 1
for i in range(16):
    #A cada jogada vai chamar o tabuleiro
    imprimir_tabuleiro(tabuleiro)
    print(f"Jogador {jogador_atual}, é sua vez.")
    linha = int(input("Digite o número da linha (0-3): "))
    coluna = int(input("Digite o número da coluna (0-3): "))

    #Se a casa selecionada estiver vazia, vai colocar o jogador atual na posição
    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = jogadores[jogador_atual]
    else:
        print("Essa posição já está ocupada. Tente novamente.")
        continue

    # Verificar se há um vencedor
    # Vai eprcorrer todas as linhas e verificar se estão todas completas com um unico jogador
    for i in range(4):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == tabuleiro[i][3] != " " \
                or tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == tabuleiro[3][i] != " ":
            imprimir_tabuleiro(tabuleiro)
            print(f"Parabéns! Jogador {jogador_atual} venceu!")
            break
    # Vai percorrer todas as diagonais e verificar se estão todas completas com um unico jogador
    else:
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == tabuleiro[3][3] != " " \
                or tabuleiro[0][3] == tabuleiro[1][2] == tabuleiro[2][1] == tabuleiro[3][0] != " ":
            imprimir_tabuleiro(tabuleiro)
            print(f"Parabéns! Jogador {jogador_atual} venceu!")
            break
    #vai fazer a alternação dos jogadores
    jogador_atual = 3 - jogador_atual
else:
    imprimir_tabuleiro(tabuleiro)
    print("Empate! O jogo terminou sem vencedor.")
