#Clear Console
import os
def clear_console():
    os.system('cls')

#Your inputs
grid = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8 ,9]
]

#Tic-tac-toe grid
def ttt():
    print(f'  {grid[0][0]}  |  {grid[0][1]}  | {grid[0][2]} ') 
    print('----------------')
    print(f'  {grid[1][0]}  |  {grid[1][1]}  | {grid[1][2]} ') 
    print(f'----------------')
    print(f'  {grid[2][0]}  |  {grid[2][1]}  | {grid[2][2]} ')

#Logic for if someone wins or ties
def game_check():
    draw = 0
    if (grid[0][0] == grid[0][1]) and (grid[0][0] == grid[0][2]):
        return True
    elif (grid[0][0] == grid[1][0]) and (grid[0][0] == grid[2][0]):
        return True
    elif (grid[0][1] == grid[1][1]) and (grid[0][1] == grid[2][1]):
        return True
    elif (grid[0][2] == grid[1][2]) and (grid[0][2] == grid[2][2]):
        return True
    elif (grid[1][0] == grid[1][1]) and (grid[1][0] == grid[1][2]):
        return True
    elif (grid[2][0] == grid[2][1]) and (grid[2][0] == grid[2][2]):
        return True
    elif (grid[0][0] == grid[1][1]) and (grid[0][0] == grid[2][2]):
        return True
    elif (grid[0][2] == grid[1][1]) and (grid[0][2] == grid[2][0]):
        return True
    #if its a tie (cat's game)
    for i in range(len(grid)):
        for ii in range(len(grid[i])):
            if type(grid[i][ii]) == int:
                draw += 1
    if draw == 0:
        return True
    else:
        return False

#Start the game
    #decides which player's turn it is
player = 0
game_check()
while game_check() == False:
    game_check()
    clear_console()

    #decides which player's turn it is
    if player > 1:
        player = 0

    #Welcome
    print('Welcome to tic-tac-toe\n')
    ttt()

    #shows which player's turn it is
    if player == 0:
        uinput = int(input('\nPlease enter the number of the space where you would like to place your "X": '))
    elif player == 1:
        uinput = int(input('\nPlease enter the number of the space where you would like to place your "O": '))

    #Finds the specific grid number the user is looking for and replaces it with their input
    array_2d = 0
    for array_1d in range(len(grid)):
        for number in grid[array_1d]:
            if array_2d > 2:
                array_2d = 0
            if number == uinput:
                if player == 0:
                    grid[array_1d][array_2d] = 'x'
                elif player == 1:
                    grid[array_1d][array_2d] = 'o'
            array_2d += 1
    player += 1
clear_console()
print('Game over.\n')
ttt()





