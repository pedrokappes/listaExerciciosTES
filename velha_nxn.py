# Vai imprimir o tbauleiro
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * (4 * len(linha) - 1))

# Vai criar o tabuleiro
def criar_tabuleiro(tamanho):
    return [[" " for _ in range(tamanho)] for _ in range(tamanho)]

# Vai ver se alçgum jogador venceu após a sua jogada, onde vai verificar todas as linhas/colunas/diagonais
def verificar_vitoria(tabuleiro, jogador, linha, coluna):
    tamanho = len(tabuleiro)

    # Verificar horizontal
    if all(tabuleiro[linha][c] == jogador for c in range(tamanho)):
        return True

    # Verificar vertical
    if all(tabuleiro[r][coluna] == jogador for r in range(tamanho)):
        return True

    # Verificar diagonais
    if linha == coluna and all(tabuleiro[i][i] == jogador for i in range(tamanho)):
        return True

    if linha + coluna == tamanho - 1 and all(tabuleiro[i][tamanho - 1 - i] == jogador for i in range(tamanho)):
        return True

    return False

# Decidi fazer uma função apenas para toda a aprte do jogo por ser bem mais complexa do que o tabuleiro 4x4
def main():
    tamanho = int(input("Digite o tamanho do tabuleiro: "))
    tabuleiro = criar_tabuleiro(tamanho)
    jogadores = {1: "X", 2: "O"}
    jogador_atual = 1
    jogadas = 0

    #inicio do jogo
    while True:
        imprimir_tabuleiro(tabuleiro)
        print(f"Jogador {jogador_atual}, é sua vez.")

        linha = int(input(f"Digite o número da linha (0-{tamanho - 1}): "))
        coluna = int(input(f"Digite o número da coluna (0-{tamanho - 1}): "))

        #vai verificar se a jogada é valida (se a linha ou coluna for maior que o tamanho determinado não rola)
        if linha < 0 or linha >= tamanho or coluna < 0 or coluna >= tamanho:
            print("Jogada inválida. Tente novamente.")
            continue

        #se o espaço estiver vazio vai inserir o jogador nele
        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogadores[jogador_atual]
            jogadas += 1
        else:
            print("Essa posição já está ocupada. Tente novamente.")
            continue

        #vai verificar se em todos os campos dentro das regras estão ocupados pelo jogador e dar a vitoria
        if verificar_vitoria(tabuleiro, jogadores[jogador_atual], linha, coluna):
            imprimir_tabuleiro(tabuleiro)
            print(f"Parabéns! Jogador {jogador_atual} venceu!")
            break
        #Se o numero de jogadas for maior que o tamanho do tabuleiro vai ocorrer um empate
        if jogadas == tamanho * tamanho:
            imprimir_tabuleiro(tabuleiro)
            print("Empate! O jogo terminou sem vencedor.")
            break

        # Vai alternar entre os jogadores
        jogador_atual = 3 - jogador_atual
main()
