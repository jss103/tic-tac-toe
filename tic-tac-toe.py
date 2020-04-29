#tic-tac-toe

playerOneTurn = True
validSpot = False

board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

d = ({'T': 0, 'M': 1, 'B': 2},{'L': 0, 'C': 1, 'R': 2})

print( '''
            To play tic-tac-toe: use keyletters to place your mark.
            Top = 'T', Middle = 'M', Bottom = 'B'.
            Left = 'L', Center = 'C', Right = 'R'.
            To play in the top left, type "TL" for Top-Left.
            To play in the middle, type "MC" for Middle-Center.
            To play in the bottom right, type "BR" for Bottom-Right.
            etc...

        ''')

print(f' {board[0][0]} | {board[0][1]} | {board[0][2]} \n---+---+---\n {board[1][0]} | {board[1][1]} | {board[1][2]} \n---+---+---\n {board[2][0]} | {board[2][1]} | {board[2][2]} ')

for i in range(9):
    if playerOneTurn == True:
        playerNumber, playerMark, playerOneTurn = 'one', 'X', False
    else:
        playerNumber, playerMark, playerOneTurn = 'two', 'O', True
    
    print('Player ' + playerNumber + ': pick a spot.')

    while validSpot == False:
        x = input()
        try:
            a = d[0][x[0]] 
            c = d[1][x[1]]
        except KeyError:
            print(x + ' is a not a valid spot. Player ' + playerNumber + ': pick a different spot.')
            continue
        if board[a][c] == playerMark:
            print('You already went here--pick a different spot.')
        elif board[a][c] == ' ':
            validSpot = True
        else:
            print('Your opponent went here--pick a different spot.')

    board[a][c] = playerMark
    print(f' {board[0][0]} | {board[0][1]} | {board[0][2]} \n---+---+---\n {board[1][0]} | {board[1][1]} | {board[1][2]} \n---+---+---\n {board[2][0]} | {board[2][1]} | {board[2][2]} ')
    if board[0][0] == board[0][1] == board[0][2] == playerMark:
        print('Player ' + playerNumber + ' wins!')
        break
    elif board[1][0] == board[1][1] == board[1][2] == playerMark:
        print('Player ' + playerNumber + ' wins!')
        break
    elif board[2][0] == board[2][1] == board[2][2] == playerMark:
        print('Player ' + playerNumber + ' wins!')
        break
    elif board[0][0] == board[1][0] == board[2][0] == playerMark:
        print('Player ' + playerNumber + ' wins!')
        break
    elif board[0][1] == board[1][1] == board[2][1] == playerMark:
        print('Player ' + playerNumber + ' wins!')
        break
    elif board[0][2] == board[1][2] == board[2][2] == playerMark:
        print('Player ' + playerNumber + ' wins!')
        break
    elif board[0][0] == board[1][1] == board[2][2] == playerMark:
        print('Player ' + playerNumber + ' wins!')
        break
    elif board[0][2] == board[1][1] == board[2][0] == playerMark:
        print('Player ' + playerNumber + ' wins!')
        break
    validSpot = False
