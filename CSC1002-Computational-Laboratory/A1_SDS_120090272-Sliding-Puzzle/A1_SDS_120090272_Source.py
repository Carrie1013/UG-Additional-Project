import random
current_matrix = []
user_op_letter = []
move = []
g_row, g_line = 0, 0
standard_name = ['left', 'right', 'up', 'down']


introduction = '''Welcome!\n
This is 120090272's sliding puzzle game! First you can enter 4 letters to denote move 'left', 'right', 'up' and 'down'.
(Such as 'j', 'k', 'r', 'f' for 'left', 'right', 'up' and 'down')
Then choose a dimension n between 3 and 10 to start your game (in an n * n matrix) to play. 
Game 'win' when you move the puzzles into its correct orders.
'''


def operate_move_puzzle():  # Create an operate number list for judging what movement to take
    global size, g_row, g_line, move
    move.clear()  # Clear anad reset the possible movement each time
    if g_line != size-1:
        move.append(0)  # 0 = left
    if g_line != 0:
        move.append(1)  # 1 = right
    if g_row != size-1:
        move.append(2)  # 2 = up
    if g_row != 0:
        move.append(3)  # 3 = down
    return move


def move_blank(op_number):  # Use number to operate the movement of blank
    global size, g_row, g_line, move, current_matrix
    # The position of the blank
    a = g_row * size + g_line
    if op_number == 0:
        b = g_row * size + g_line + 1
    if op_number == 1:
        b = g_row * size + g_line - 1
    if op_number == 2:
        b = (g_row + 1) * size + g_line
    if op_number == 3:
        b = (g_row - 1) * size + g_line
    current_matrix[a], current_matrix[b] = current_matrix[b], current_matrix[a]
    return current_matrix


def matrix_generate():  # To generate the original matrix
    global size, g_row, g_line, move, current_matrix
    # Create an list to put in number of matrix in order
    current_matrix = list(range(size ** 2))
    for m in range(random.randint(3*(size**2), 6*(size**2))):
        s = current_matrix.index(0)
        g_row, g_line = divmod(s, size)  # locate the position of '0'
        operate_move_puzzle()
        command = random.choice(move)  # Randomly move the matrix
        move_blank(command)
    zero = current_matrix.index(0)
    g_row, g_line = divmod(zero, size)  # locate the current '0'
    for i in range(size):
        for j in range(size):
            if i == g_row and j == g_line:
                print("   ", end=" ")  # Print blank at 0
            else:
                # Print out the original matrix
                print("%3d" % current_matrix[i * size + j], end=" ")
        print('\n')


def input_directions():  # For user to input his letter as controller
    global size, g_row, g_line, move, current_matrix
    user_op_letter.clear()
    while True:
        # To make sure the letters are at lower case
        op_letter = input(
            'Enter 4 letters for left, right, up, and down directions: ').lower()
        for item in op_letter:
            if item.isalpha() == True and item not in user_op_letter:  # The input must be in letter form
                # Also the letter couldn't be repeated
                user_op_letter.append(item)
                continue
            if len(user_op_letter) == 4:
                break
        if len(user_op_letter) != 4:
            print('The input is invalid, please try it again! ')
            continue
        return user_op_letter


def step_information():  # To inform the user what to do at each step
    global size, g_row, g_line, move, current_matrix, user_op_letter
    print('enter your move:', end='')
    for i in move:  # Different position has different way of moving
        print(' [{}]-{} '.format(user_op_letter[i], standard_name[i]), end='')
    print(": ", end="")
    return


def win():  # To check whether the user win or not
    global size
    for i in range(size**2 - 1):
        g_row, g_line = divmod(i, size)
        if current_matrix[g_row * size + g_line] != i + 1:
            return False
    return True


def main():  # The main body of playing this game
    global size, g_row, g_line, move, current_matrix, user_op_letter
    flg = True
    print(introduction)
    input_directions()
    # To change the input letter into operation number
    name_to_number = dict.fromkeys(user_op_letter)
    for i in range(4):
        name_to_number[user_op_letter[i]] = i
    print("Now you can play the game: ")
    # play the game
    while True:
        n = input(
            "\nEnter a number n in range 3 to 10 to choose the dimenssion, enter 'q' to quit game: ").lower()
        # ask the user to choose the dimension of game
        if n == 'q':
            print('quit')
            break
        if n.isdigit() == False or int(n) < 3 or int(n) > 10:
            # check whether the input is right
            print('the input is invalid, please input a number in 3 to 10! ')
            continue
        size = int(n)
        matrix_generate()
        # generate the original matrix
        cnt_move = 0  # Count how many moves have the users moved
        while True:
            if win() == True:
                # check whether the game win or not
                print('\nCongratulations! You win in {} moves !\n'.format(cnt_move))
                opt = input(
                    'Enter [q] to quit or enter any other letter to start a new game : ')
                if opt == 'q':
                    flg = 0
                break
            else:
                operate_move_puzzle()
                step_information()
                # inform the user whether what to do and how to operate the game
                a = input()
                if a in name_to_number and name_to_number[a] in move:
                    cnt_move += 1
                    op_number = name_to_number[a]
                    move_blank(op_number)
                    S = current_matrix
                    g_row, g_line = divmod(
                        current_matrix.index(0), size)
                    for i in range(size):
                        for j in range(size):
                            if i == g_row and j == g_line:
                                print("   ", end=" ")
                            else:
                                print(
                                    "%3d" % current_matrix[i * size + j], end=" ")
                        print('\n')
                else:
                    print('Invalid Input\n')
        if flg == 0:
            print("quit","\nThank you for playing this game!")
            break


main()
