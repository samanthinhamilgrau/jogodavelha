import pygame
import sys
import numpy as np

# Configurações do jogo
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 10
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 10
CROSS_WIDTH = 10
SPACE = 25

# Cores
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
TEXT_COLOR = (255, 255, 255)

# Inicializa o Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo da Velha')
screen.fill(BG_COLOR)

# Fonte para as mensagens
font = pygame.font.Font(None, 40)

# Tabuleiro
board = np.zeros((BOARD_ROWS, BOARD_COLS))

def draw_lines():
    """Desenha as linhas do tabuleiro."""
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE * i), (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)

def draw_figures():
    """Desenha os círculos e os X no tabuleiro."""
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, 
                                   (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), 
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, 
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), 
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

def mark_square(row, col, player):
    """Marca a jogada no tabuleiro."""
    board[row][col] = player

def available_square(row, col):
    """Verifica se a casa está vazia."""
    return board[row][col] == 0

def is_board_full():
    """Verifica se o tabuleiro está cheio."""
    return np.all(board != 0)

def check_winner(player):
    """Verifica se um jogador venceu."""
    for i in range(BOARD_ROWS):
        if np.all(board[i, :] == player) or np.all(board[:, i] == player):
            return True
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True
    return False

def show_message(text):
    """Exibe uma mensagem no centro da tela."""
    screen.fill(BG_COLOR)  # Limpa a tela
    text_surface = font.render(text, True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.update()
    pygame.time.delay(2000)  # Aguarda 2 segundos antes de reiniciar o jogo

def restart_game():
    """Reinicia o jogo."""
    screen.fill(BG_COLOR)
    draw_lines()
    global board
    board = np.zeros((BOARD_ROWS, BOARD_COLS))

# Variáveis do jogo
player = 1
game_over = False

# Desenha as linhas do tabuleiro no início
draw_lines()

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = event.pos
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)

                if check_winner(player):
                    show_message(f'Jogador {player} venceu!')
                    game_over = True
                    restart_game()
                    game_over = False
                    player = 1
                elif is_board_full():
                    show_message('Empate!')
                    game_over = True
                    restart_game()
                    game_over = False
                    player = 1
                else:
                    player = 2 if player == 1 else 1  # Alterna entre os jogadores

                draw_figures()

    pygame.display.update()
