import pygame
import sys

pygame.init()

SCREEN_SIZE = (300, 300)
CELL_SIZE = 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 80

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Tic-Tac-Toe")

board = [['', '', ''], ['', '', ''], ['', '', '']]

def draw_board():
    for x in range(3):
        for y in range(3):
            pygame.draw.rect(screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)
            font = pygame.font.Font(None, FONT_SIZE)
            text = font.render(board[y][x], True, WHITE)
            text_rect = text.get_rect(center=(x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2))
            screen.blit(text, text_rect)

def check_win(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def check_draw():
    return all(all(cell != '' for cell in row) for row in board)

def print_result(result):
    if result == 'X':
        print("Player 1 wins!")
    elif result == 'O':
        print("Player 2 wins!")
    elif result == 'draw':
        print("It's a draw!")

turn = 'X'
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            row, col = y // CELL_SIZE, x // CELL_SIZE
            if board[row][col] == '':
                board[row][col] = turn
                if check_win(turn):
                    game_over = True
                elif check_draw():
                    game_over = True
                else:
                    turn = 'O' if turn == 'X' else 'X'
            
    screen.fill(BLACK)
    draw_board()
    pygame.display.flip()

if check_win('X'):
    print_result('X')
elif check_win('O'):
    print_result('O')
elif check_draw():
    print_result('draw')

pygame.time.wait(2000)

board = [['', '', ''], ['', '', ''], ['', '', '']]
turn = 'X'
game_over = False
