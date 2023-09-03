import random

#setando as cores
bg_verde = "\u001b[42m"
bg_amarelo = "\u001b[43m"
reset = "\u001b[0m"

#puxando o arquivo, padronizando e escolhendo a palavra
with open('lista_palavras.txt', 'r', encoding='utf-8') as arquivo:
    linhas = [linha.strip().encode('utf-8').decode('utf-8') for linha in arquivo]
correta = random.choice(linhas)
correta_list = list(correta)

#lista de letras disponiveis
disponiveis = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#preparando a tela    
def letras_ocultas(n):
    for i in range(0, len(n)):
        print("[]", end="" )

#iniciando o jogo
for i in range(0, len(correta)):
    print("[]", end="" )

for j in range(6):
    #fazendo a tela
    print("=============================================================================================================================================")
    print("Letras disponiveis: ")
    print(disponiveis)
    print("\nPalavra para acertar: ")

    letras_ocultas(correta)

    chute = input("\n\nDiga uma palavra: ")
    chute_list = list(chute)
    
    if chute == correta:
        print("Você ganhou!!!")
        break

    #verificar se a letra não está na lista de letras disponiveis vai pedir para falar outra palavra
    #caso a letra estiver disponivel, vai verificar se está na posição correta e assim adicionando a cor de fundo
    for i in range (0,len(correta)):
        #if chute[i] not in disponiveis:
         #   print("Você já usou essa letra, escolha outra: \n")
          #  continue
        
        if chute[i] == correta[i]:
            print(f"{bg_verde}{chute[i]}{reset}", end = "")
            disponiveis.remove(chute[i])


        elif chute[i] in correta:
            print(f"{bg_amarelo}{chute[i]}{reset}", end = "")
            disponiveis.remove(chute[i])

        else:
            print(chute[i], end = "")
            disponiveis.remove(chute[i])

    print()
