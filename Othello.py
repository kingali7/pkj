# CSCI3180 Principles of Programming Languages
#
# --- Declaration ---
#
# I declare that the assignment here submitted is original except for source
# material explicitly acknowledged. I also acknowledge that I am aware of
# University policy and regulations on honesty in academic work, and of the
# disciplinary guidelines and procedures applicable to breaches of such policy
# and regulations, as contained in the website
# http://www.cuhk.edu.hk/policy/academichonesty/
#
# Assignment 2
# Name : Alshir Soyunjov
# Student ID : 1155119170
# Email Addr : 1155119170@link.cuhk.edu.hk

class Othello:

    def __init__(self):
        self.gameBoard = GameBoard()
        self.player1 = None
        self.player2 = None
        self.turn = 0


    def createPlayer(self, symbol, playerNum):
        if symbol == 'O':
            if playerNum == '1':
                return Human(symbol)
            else:
                return Computer(symbol)
        else:
            if playerNum == '1':
                return Human(symbol)
            else:
                return Computer(symbol)

    def startGame(self):
	    #basic logic
        self.player1 = self.createPlayer('O', choice1)
        self.player2 = self.createPlayer('X', choice2)
        self.gameBoard.init_gameBoard()
        self.gameBoard.printGameBoard()

        while not self.gameBoard.check_ending():
            current_player = [self.player1,self.player2][self.turn]
            print("Player %s's turn." % current_player.playerSymbol)
            if self.gameBoard.check_legal_move(current_player.playerSymbol):
                pos = current_player.nextMove(self.gameBoard.board)
                self.gameBoard.execute_flip(pos, current_player.playerSymbol)
            else:
                print("There is no valid move for Player %s." % current_player.playerSymbol)
            self.turn = 1 - self.turn

            self.gameBoard.printGameBoard()

        s1, s2 = self.gameBoard.check_winner()
        if s1 > s2:
            winner = 'O'  # Black
        elif s1 < s2:
            winner = 'X'  # White
        elif s1 == s2:
            winner = ' '  # Tie

        print('Count O : {}'.format(s1))
        print('Count X : {}'.format(s2))
        if winner != ' ':
            print('Player {} won!\n'.format(winner))
        else:
            print('A tie')


class Player:

    def __init__(self, symbol):
        self.playerSymbol = symbol

    def nextMove(self, board):
        pass

class Human(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def nextMove(self,board):
        validMove = False
        while validMove == False:
            validMove = False
            inp = input("Type the row and col to put the disc:")
            l = inp.split(' ')

            #check if input is valid
            if(len(l) != 2):
                validMove = False
            else:
                l[0] = int(l[0]) - 1
                l[1] = int(l[1]) - 1
                if(l[0] < 1 or l[0] > 8 or l[1] <1 or l[1] > 8):
                    validMove = False
                if(board[l[0]][l[1]] != ' '):
                    validMove = False
                else:
                    if(self.checkCell(board, l) == False):
                        validMove = False
                    else:
                        validMove = True
            if(validMove == False):
                print("Invalid Input")
                print("Player %s's turn." % self.playerSymbol)
        return [l[0], l[1]]

    def checkCell(self, board, cell):
        if (self.playerSymbol == 'O'):
            anti_symbol = 'X'
        else:
            anti_symbol = 'O'
        symbol = self.playerSymbol
        x = cell[0]
        y = cell[1]
        counter = 0

        while y < 7:
            if board[x][y + 1] == anti_symbol:
                counter = counter + 1
                y = y + 1
            elif board[x][y + 1] == symbol and counter > 0:
                return True
            else:
                break

        x = cell[0]
        y = cell[1]
        counter = 0
        while y > 0:
            if board[x][y - 1] == anti_symbol:
                counter = counter + 1
                y = y - 1
            elif board[x][y - 1] == symbol and counter > 0:
                return True
            else:
                break
        x = cell[0]
        y = cell[1]
        counter = 0
        while x < 7:
            if board[x + 1][y] == anti_symbol:
                counter = counter + 1
                x = x + 1
            elif board[x + 1][y] == symbol and counter > 0:
                return True
            else:
                break

        x = cell[0]
        y = cell[1]
        counter = 0
        while x > 0:
            if board[x - 1][y] == anti_symbol:
                counter = counter + 1
                x = x - 1
            elif board[x - 1][y] == symbol and counter > 0:
                return True
            else:
                break
        x = cell[0]
        y = cell[1]
        counter = 0
        while x > 0 and y > 0:
            if board[x - 1][y - 1] == anti_symbol:
                counter = counter + 1
                x = x - 1
                y = y - 1
            elif board[x - 1][y - 1] == symbol and counter > 0:
                return True
            else:
                break
        x = cell[0]
        y = cell[1]
        counter = 0
        while x > 0 and y < 7:
            if board[x - 1][y + 1] == anti_symbol:
                counter = counter + 1
                x = x - 1
                y = y + 1
            elif board[x - 1][y + 1] == symbol and counter > 0:
                return True
            else:
                break
        x = cell[0]
        y = cell[1]
        counter = 0
        while x < 7 and y > 0:
            if board[x + 1][y - 1] == anti_symbol:
                counter = counter + 1
                x = x + 1
                y = y - 1
            elif board[x + 1][y - 1] == symbol and counter > 0:
                return True
            else:
                break
        x = cell[0]
        y = cell[1]
        counter = 0
        while x < 7 and y < 7:
            if board[x + 1][y + 1] == anti_symbol:
                counter = counter + 1
                x = x + 1
                y = y + 1
            elif board[x + 1][y + 1] == symbol and counter > 0:
                return True
            else:
                break
        return False


class GameBoard:
    def __init__(self):
        self.board = None

    def init_gameBoard(self):
        self.board = [[' ' for i in range(8)] for j in range(8)]
        self.board[3][3] = 'X'
        self.board[4][4] = 'X'
        self.board[3][4] = 'O'
        self.board[4][3] = 'O'

    def check_ending(self):
        # check whether the game is over or not
        if (self.check_legal_move('O') == False and self.check_legal_move('X') == False):
            return True
        else:
            return False

    def check_legal_move(self, symbol):
        if symbol == 'O':
            anti_symbol = 'X'
        else:
            anti_symbol = 'O'
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == ' ':
                    x = i
                    y = j
                    counter = 0
                    while y < 7:
                        if self.board[x][y + 1] == anti_symbol:
                            counter = counter + 1
                            y = y + 1
                        elif self.board[x][y + 1] == symbol and counter > 0:
                            return True
                        else:
                            break

                    x = i
                    y = j
                    counter = 0
                    while y > 0:
                        if self.board[x][y - 1] == anti_symbol:
                            counter = counter + 1
                            y = y - 1
                        elif self.board[x][y - 1] == symbol and counter > 0:
                            return True
                        else:
                            break
                    x = i
                    y = j
                    counter = 0
                    while x < 7:
                        if self.board[x + 1][y] == anti_symbol:
                            counter = counter + 1
                            x = x + 1
                        elif self.board[x + 1][y] == symbol and counter > 0:
                            return True
                        else:
                            break

                    x = i
                    y = j
                    counter = 0
                    while x > 0:
                        if self.board[x - 1][y] == anti_symbol:
                            counter = counter + 1
                            x = x - 1
                        elif self.board[x - 1][y] == symbol and counter > 0:
                            return True
                        else:
                            break
                    x = i
                    y = j
                    counter = 0
                    while x > 0 and y > 0:
                        if self.board[x - 1][y - 1] == anti_symbol:
                            counter = counter + 1
                            x = x - 1
                            y = y - 1
                        elif self.board[x - 1][y - 1] == symbol and counter > 0:
                            return True
                        else:
                            break
                    x = i
                    y = j
                    counter = 0
                    while x > 0 and y < 7:
                        if self.board[x - 1][y + 1] == anti_symbol:
                            counter = counter + 1
                            x = x - 1
                            y = y + 1
                        elif self.board[x - 1][y + 1] == symbol and counter > 0:
                            return True
                        else:
                            break
                    x = i
                    y = j
                    counter = 0
                    while x < 7 and y > 0:
                        if self.board[x + 1][y - 1] == anti_symbol:
                            counter = counter + 1
                            x = x + 1
                            y = y - 1
                        elif self.board[x + 1][y - 1] == symbol and counter > 0:
                            return True
                        else:
                            break
                    x = i
                    y = j
                    counter = 0
                    while x < 7 and y < 7:
                        if self.board[x + 1][y + 1] == anti_symbol:
                            counter = counter + 1
                            x = x + 1
                            y = y + 1
                        elif self.board[x + 1][y + 1] == symbol and counter > 0:
                            return True
                        else:
                            break
        return False

    def check_winner(self):
        x = 0
        o = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 'X':
                    x = x + 1
                if self.board[i][j] == 'O':
                    o = o + 1
        return [x, o]

    def execute_flip(self, pos, symbol):
        if symbol == 'O':
            anti_symbol = 'X'
        else:
            anti_symbol = 'O'
        count = 0
        x = pos[0]
        y = pos[1]
        while y < 7:
            if self.board[x][y + 1] == anti_symbol:
                count = count + 1
                y = y + 1

            else:
                if count > 0 and self.board[x][y + 1] == symbol:
                    for i in range(0, count + 1):
                        self.board[x][pos[1] + i] = symbol

                break
        count = 0
        x = pos[0]
        y = pos[1]
        while y > 0:
            if self.board[x][y - 1] == anti_symbol:
                count = count + 1
                y = y - 1
            else:
                if count > 0 and self.board[x][y - 1] == symbol:
                    for i in range(0, count + 1):
                        self.board[x][pos[1] - i] = symbol

                break
        count = 0
        x = pos[0]
        y = pos[1]
        while x < 7:
            if self.board[x + 1][y] == anti_symbol:
                count = count + 1
                x = x + 1

            else:
                if count > 0 and self.board[x + 1][y] == symbol:
                    for i in range(0, count + 1):
                        self.board[pos[0] + i][y] = symbol

                break
        count = 0
        x = pos[0]
        y = pos[1]
        while x > 0:

            if self.board[x - 1][y] == anti_symbol:
                count = count + 1
                x = x - 1
            else:
                if count > 0 and self.board[x - 1][y] == symbol:
                    for i in range(0, count + 1):
                        self.board[pos[0] - i][y] = symbol

                break
        count = 0
        x = pos[0]
        y = pos[1]
        while x < 7 and y < 7:

            if self.board[x + 1][y + 1] == anti_symbol:
                count = count + 1
                x = x + 1
                y = y + 1
            else:
                if count > 0 and self.board[x + 1][y + 1] == symbol:
                    for i in range(0, count + 1):
                        self.board[pos[0] + i][pos[1] + i] = symbol

                break
        count = 0
        x = pos[0]
        y = pos[1]
        while x < 7 and y > 0:

            if self.board[x + 1][y - 1] == anti_symbol:
                count = count + 1
                x = x + 1
                y = y - 1
            else:
                if count > 0 and self.board[x + 1][y - 1] == symbol:
                    for i in range(0, count + 1):
                        self.board[pos[0] + i][pos[1] - i] = symbol

                break
        count = 0
        x = pos[0]
        y = pos[1]
        while x > 0 and y > 0:

            if self.board[x - 1][y - 1] == anti_symbol:
                count = count + 1
                x = x - 1
                y = y - 1
            else:
                if count > 0 and self.board[x - 1][y - 1] == symbol:
                    for i in range(0, count + 1):
                        self.board[pos[0] - i][pos[1] - i] = symbol

                break
        count = 0
        x = pos[0]
        y = pos[1]
        while x > 0 and y < 7:

            if self.board[x - 1][y + 1] == anti_symbol:
                count = count + 1
                x = x - 1
                y = y + 1
            else:
                if count > 0 and self.board[x - 1][y + 1] == symbol:
                    for i in range(0, count + 1):
                        self.board[pos[0] - i][pos[1] + i] = symbol

                break

    def printGameBoard(self):
        for i in range(9):
            for j in range(9):
                if (i > 0 and j == 0):
                    print(str(i) + ' | ', end='')
                    continue
                if (i == 0 and j > 0):
                    print(str(j) + ' | ', end='')
                    continue
                print(self.board[i - 1][j - 1] + ' | ', end='')
            print('')
            print('-' * 35)

class Computer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def nextMove(self, board):
        # randomly place a valid move
        for i in range(0,8):
            for j in range(0,8):
                if(board[i][j] == ' ' and self.checkCell(board, [i,j]) == True):
                    return [i,j]

    def checkCell(self, board, cell):
        if (self.playerSymbol == 'O'):
            anti_symbol = 'X'
        else:
            anti_symbol = 'O'
        symbol = self.playerSymbol
        x = cell[0]
        y = cell[1]
        counter = 0

        while y < 7:
            if board[x][y + 1] == anti_symbol:
                counter = counter + 1
                y = y + 1
            elif board[x][y + 1] == symbol and counter > 0:
                return True
            else:
                break

        x = cell[0]
        y = cell[1]
        counter = 0
        while y > 0:
            if board[x][y - 1] == anti_symbol:
                counter = counter + 1
                y = y - 1
            elif board[x][y - 1] == symbol and counter > 0:
                return True
            else:
                break
        x = cell[0]
        y = cell[1]
        counter = 0
        while x < 7:
            if board[x + 1][y] == anti_symbol:
                counter = counter + 1
                x = x + 1
            elif board[x + 1][y] == symbol and counter > 0:
                return True
            else:
                break

        x = cell[0]
        y = cell[1]
        counter = 0
        while x > 0:
            if board[x - 1][y] == anti_symbol:
                counter = counter + 1
                x = x - 1
            elif board[x - 1][y] == symbol and counter > 0:
                return True
            else:
                break
        x = cell[0]
        y = cell[1]
        counter = 0
        while x > 0 and y > 0:
            if board[x - 1][y - 1] == anti_symbol:
                counter = counter + 1
                x = x - 1
                y = y - 1
            elif board[x - 1][y - 1] == symbol and counter > 0:
                return True
            else:
                break
        x = cell[0]
        y = cell[1]
        counter = 0
        while x > 0 and y < 7:
            if board[x - 1][y + 1] == anti_symbol:
                counter = counter + 1
                x = x - 1
                y = y + 1
            elif board[x - 1][y + 1] == symbol and counter > 0:
                return True
            else:
                break
        x = cell[0]
        y = cell[1]
        counter = 0
        while x < 7 and y > 0:
            if board[x + 1][y - 1] == anti_symbol:
                counter = counter + 1
                x = x + 1
                y = y - 1
            elif board[x + 1][y - 1] == symbol and counter > 0:
                return True
            else:
                break
        x = cell[0]
        y = cell[1]
        counter = 0
        while x < 7 and y < 7:
            if board[x + 1][y + 1] == anti_symbol:
                counter = counter + 1
                x = x + 1
                y = y + 1
            elif board[x + 1][y + 1] == symbol and counter > 0:
                return True
            else:
                break
        return False

if __name__ == "__main__":
    print('Please choose player 1 (O):')
    print('1. Human\n2. Computer Player')
    choice1 = input('Your choice is: ')
    if(choice1 == '1'):
        print('Player O is Human.')
    else:
        print('Player O is Computer.')

    print('Please choose player 2 (X):')
    print('1. Human\n2. Computer Player')
    choice2 = input('Your choice is: ')
    if(choice2 == '1'):
        print('Player X is Human.')
    else:
        print('Player X is Computer.')

    othello = Othello()
    othello.startGame()