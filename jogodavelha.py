def criar_tabuleiro():
    return [[' ' for _ in range(3)] for _ in range(3)]

def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 5)

def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(celula == jogador for celula in linha):
            return True
    
    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True
    
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    
    return False

def verificar_empate(tabuleiro):
    return all(celula != ' ' for linha in tabuleiro for celula in linha)

def jogada_valida(tabuleiro, linha, coluna):
    return 0 <= linha < 3 and 0 <= coluna < 3 and tabuleiro[linha][coluna] == ' '

def jogo_da_velha():
    tabuleiro = criar_tabuleiro()
    jogador_atual = 'X'
    
    while True:
        exibir_tabuleiro(tabuleiro)
        try:
            linha = int(input(f'Jogador {jogador_atual}, escolha a linha (0-2): '))
            coluna = int(input(f'Jogador {jogador_atual}, escolha a coluna (0-2): '))
        except ValueError:
            print("Entrada inválida! Insira números entre 0 e 2.")
            continue

        if not jogada_valida(tabuleiro, linha, coluna):
            print("Posição inválida ou já ocupada! Escolha outra.")
            continue
        
        tabuleiro[linha][coluna] = jogador_atual
        
        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f'Jogador {jogador_atual} venceu!')
            break
        
        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print('O jogo empatou!')
            break
        
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

if __name__ == "__main__":
    jogo_da_velha()
