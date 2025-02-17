def exibir_tabuleiro():
    print(tabuleiro1)
    print(tabuleiro2)
    print(tabuleiro3)

def jogo_da_velha():
    global tabuleiro1, tabuleiro2, tabuleiro3
    tabuleiro1 = [" ", " ", " "]
    tabuleiro2 = [" ", " ", " "]
    tabuleiro3 = [" ", " ", " "]
    jogador_atual = "X"
    
    for _ in range(9):
        exibir_tabuleiro()
        linha = int(input("Linha (0-2): "))
        coluna = int(input("Coluna (0-2): "))
        
        if linha == 0:
            if tabuleiro1[coluna] != " ":
                print("Posição ocupada!")
                continue
            tabuleiro1[coluna] = jogador_atual
        elif linha == 1:
            if tabuleiro2[coluna] != " ":
                print("Posição ocupada!")
                continue
            tabuleiro2[coluna] = jogador_atual
        elif linha == 2:
            if tabuleiro3[coluna] != " ":
                print("Posição ocupada!")
                continue
            tabuleiro3[coluna] = jogador_atual
        else:
            print("Linha inválida!")
            continue
        
        jogador_atual = "O" if jogador_atual == "X" else "X"
    
    exibir_tabuleiro()
    print("Fim do jogo!")

jogo_da_velha()
