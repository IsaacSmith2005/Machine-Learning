import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình và bàn cờ
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

# Khởi tạo màn hình
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False  # Trạng thái vua
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        """Tính toán vị trí quân cờ."""
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        """Nâng cấp thành vua."""
        self.king = True

    def draw(self, win):
        """Vẽ quân cờ."""
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            pygame.draw.circle(win, (255, 215, 0), (self.x, self.y), radius // 2)

    def move(self, row, col):
        """Di chuyển quân cờ."""
        self.row = row
        self.col = col
        self.calc_pos()

def create_board():
    """Tạo bàn cờ với các quân cờ."""
    board = [[0] * COLS for _ in range(ROWS)]
    for row in range(ROWS):
        if row % 2 == 0:
            start = 1
        else:
            start = 0
        for col in range(start, COLS, 2):
            if row < 3:
                board[row][col] = Piece(row, col, BLUE)  # Quân xanh
            elif row > 4:
                board[row][col] = Piece(row, col, RED)  # Quân đỏ
    return board

def draw_board(win, board):
    """Vẽ bàn cờ và các quân cờ."""
    win.fill(WHITE)
    for row in range(ROWS):
        for col in range(row % 2, COLS, 2):
            pygame.draw.rect(win, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            if piece != 0:
                piece.draw(win)

def valid_moves(board, piece):
    """Tìm các nước đi hợp lệ cho quân cờ."""
    moves = {}
    directions = [(-1, -1), (-1, 1)]  # Hướng đi tới chéo
    if piece.king:
        directions += [(1, -1), (1, 1)]  # Nếu là vua thì thêm hướng đi lùi chéo

    for drow, dcol in directions:
        row, col = piece.row + drow, piece.col + dcol
        if 0 <= row < ROWS and 0 <= col < COLS and board[row][col] == 0:
            moves[(row, col)] = None  # Nước đi hợp lệ

        elif 0 <= row < ROWS and 0 <= col < COLS:
            enemy = board[row][col]
            if enemy != 0 and enemy.color != piece.color:
                # Kiểm tra xem có thể ăn quân địch hay không
                jump_row, jump_col = row + drow, col + dcol
                if 0 <= jump_row < ROWS and 0 <= jump_col < COLS and board[jump_row][jump_col] == 0:
                    moves[(jump_row, jump_col)] = (row, col)  # Lưu nước đi ăn

    return moves

def main():
    run = True
    clock = pygame.time.Clock()
    board = create_board()
    selected_piece = None
    player_turn = RED  # Bắt đầu với người chơi đỏ

    while run:
        clock.tick(60)

        # In ra lượt chơi hiện tại để theo dõi
        print(f"Lượt của: {'Đỏ' if player_turn == RED else 'Xanh'}")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = pos[1] // SQUARE_SIZE, pos[0] // SQUARE_SIZE

                print(f"Chuột click vào: ({row}, {col})")  # Debug
                if board[row][col] != 0:
                    print(f"Quân cờ tại ({row}, {col}) là: {board[row][col].color}")  # Debug

                if selected_piece:
                    moves = valid_moves(board, selected_piece)
                    if (row, col) in moves:
                        # Thực hiện di chuyển quân cờ
                        board[selected_piece.row][selected_piece.col] = 0
                        selected_piece.move(row, col)
                        board[row][col] = selected_piece

                        if moves[(row, col)]:
                            enemy_row, enemy_col = moves[(row, col)]
                            board[enemy_row][enemy_col] = 0  # Ăn quân địch

                        if row == 0 or row == ROWS - 1:
                            selected_piece.make_king()  # Nâng cấp thành vua

                        # Chuyển lượt chơi
                        player_turn = BLUE if player_turn == RED else RED
                        print(f"Lượt chơi: {'Xanh' if player_turn == BLUE else 'Đỏ'}")  # Debug

                    selected_piece = None

                elif board[row][col] != 0 and board[row][col].color == player_turn:
                    selected_piece = board[row][col]

        draw_board(screen, board)
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()