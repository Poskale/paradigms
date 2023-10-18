# Создание пустой доски 3x3
board = [[' ' for _ in range(3)] for _ in range(3)]

# Функция для отображения доски
def display_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Функция для проверки выигрышных комбинаций
def check_win(board, player):
    # Проверка по горизонтали
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Проверка по вертикали
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Проверка по диагоналям
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Функция для осуществления хода
def make_move(board, row, col, player):
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    else:
        return False

# Основной игровой цикл
def play_game():
    current_player = 'X'
    while True:
        display_board(board)
        print(f"Ход игрока {current_player}")
        row = int(input("Введите номер строки (0-2): "))
        col = int(input("Введите номер столбца (0-2): "))
        if make_move(board, row, col, current_player):
            if check_win(board, current_player):
                display_board(board)
                print(f"Игрок {current_player} выиграл! 🎉")
                break
            elif all(board[row][col] != ' ' for row in range(3) for col in range(3)):
                display_board(board)
                print("Ничья! ⚖️")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Некорректный ход. Попробуйте еще раз.")

# Запуск игры
play_game()