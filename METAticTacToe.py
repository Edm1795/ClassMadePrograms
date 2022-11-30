#----------------------------------------------------

# Assignment 2: Tic Tac Toe classes

# 

# Author: 

# Collaborators:

# References: Set code based on csestack.org (In the end this was not used.)



#----------------------------------------------------



class NumTicTacToe:

    def __init__(self):

        '''

        Initializes an empty Numerical Tic Tac Toe board.

        Inputs: none

        Returns: None

        '''       

        self.board = [] # list of lists, where each internal list represents a row

        self.size = 3   # number of columns and rows of board

       

        

        #populate the empty squares in board with 0

        for i in range(self.size):

            row = []

            for j in range(self.size):

                row.append(0)

            self.board.append(row)

                

                

    def drawBoard(self):

        '''

        Displays the current state of the board, formatted with column and row 

        indicies shown.

        Inputs: none

        Returns: None

        '''

        # TO DO: delete pass and print out formatted board

        # e.g. an empty board should look like this:

        #    0   1   2  

        # 0    |   |   

        #   -----------

        # 1    |   |   

        #   -----------

        # 2    |   |  

        

        print('   0   1   2') # Print top line coordinates

        x = 0 # Initiaize value for column coordiantes

        c = 0 # counter to set number of '|'

        for row in self.board:

            s = '%d ' % (x) # Initialize each the '0 ' for each line of type ('0    |   |   ')

            for cell in row:

                c += 1

                if cell == 0: # if cell is 0, replace 0 with space (null)

                    if c < 3:

                        cell = '  ' # null space

                        s += '   |' # add to '0    |   |   ' a triple space and |('   |') (Only make two of these)

                    else:  

                        cell = '  ' 

                        s += '   ' # if on third iteration, add triple space but no |

                        c = 0

                elif c < 3:

                    s += ' '+str(cell)+' ' # If cell is not 0, add ' num |'(3 spots with num in centre, then |)

                    s += '|'

                else:

                    s += ' '+str(cell)+' ' # If cell is not 0 (and on 3rd iter.), add ' num '(3 spots with num in centre))

                    c = 0

                    

                

            print(s)

            if x < 2:

                print('  '+'-'*11)

            x = x + 1

        print()

                

        #print('0'' ',myBoard.getValue(0,0),'|',myBoard.getValue(0,1),'|',myBoard.getValue(0,2))

        #print('  '+'-'*11)

        #print('1'' ',myBoard.getValue(1,0),'|',myBoard.getValue(1,1),'|',myBoard.getValue(1,2))

        #print('  '+'-'*11)

        #print('2'' ',myBoard.getValue(2,0),'|',myBoard.getValue(2,1),'|',myBoard.getValue(2,2))       

      



    #def getValue(self,row,col):

        

        #if self.board[row][col] == 0:

            #return ' '

        #else:

            #return self.board[row][col]    

    





    def squareIsEmpty(self, row, col):

        '''

        Checks if a given square is empty, or if it already contains a number 

        greater than 0.

        Inputs:

           row (int) - row index of square to check

           col (int) - column index of square to check

        Returns: True if square is empty; False otherwise

        '''

        # TO DO: delete pass and complete method

        

        if self.board[row][col] == 0:

            return True

        else:

            return False

        

        

        

    

    

    def update(self, row, col, num):

        '''

        Assigns the integer, num, to the board at the provided row and column, 

        but only if that square is empty.

        Inputs:

           row (int) - row index of square to update

           col (int) - column index of square to update

           num (int) - entry to place in square

        Returns: True if attempted update was successful; False otherwise

        '''

        # TO DO: delete pass and complete method

        

        if self.squareIsEmpty(row,col):

            self.board[row][col] = num

            return True

        else:

            return False

        

        

    

    

    def boardFull(self):

        '''

        Checks if the board has any remaining empty squares.

        Inputs: none

        Returns: True if the board has no empty squares (full); False otherwise

        '''

        # TO DO: delete pass and complete method

        

        if any(0 in sl for sl in self.board):

            return False

        else:

            return True

            

        

           

    def isWinner(self):

        '''

        Checks whether the current player has just made a winning move.  In order

        to win, the player must have just completed a line (of 3 squares) that 

        adds up to 15. That line can be horizontal, vertical, or diagonal.

        Inputs: none

        Returns: True if current player has won with their most recent move; 

                 False otherwise

        '''

        # TO DO: delete pass and complete method

        

        for i in range(3):

            if self.board[i][0]+self.board[i][1]+self.board[i][2] == 15: # Check first row, then second row, third row

                return True

            elif self.board[0][i]+self.board[1][i]+self.board[2][i] == 15: # Check first column, then second col., third col

                return True

            elif self.board[0][0]+self.board[1][1]+self.board[2][2] == 15: # Check diagonal (1,5,9)

                return True

            elif self.board[0][2]+self.board[1][1]+self.board[2][0] == 15: # Check diagonal (3,5,7)

                return True

        else:

            return False

        

        

class ClassicTicTacToe:

    def __init__(self):

        '''

        Initializes an empty Classical Tic Tac Toe board.

        Inputs: none

        Returns: None

        '''       

        self.board = [] # list of lists, where each internal list represents a row

        self.size = 3   # number of columns and rows of board

       

        

        #populate the empty squares in board with 0

        for i in range(self.size):

            row = []

            for j in range(self.size):

                row.append('E')

            self.board.append(row)

                

                

    def drawBoard(self):

        '''

        Displays the current state of the board, formatted with column and row 

        indicies shown.

        Inputs: none

        Returns: None

        '''

        # TO DO: delete pass and print out formatted board

        # e.g. an empty board should look like this:

        #    0   1   2  

        # 0    |   |   

        #   -----------

        # 1    |   |   

        #   -----------

        # 2    |   |  

        

        print('   0   1   2') # Print top line coordinates

        x = 0 # Initiaize value for column coordiantes

        c = 0 # counter to set number of '|'

        for row in self.board:

            s = '%d ' % (x) # Initialize each the '0 ' for each line of type ('0    |   |   ')

            for cell in row:

                c += 1

                if cell == 'E': # if cell is 0, replace 0 with space (null)

                    if c < 3:

                        cell = '  ' # null space

                        s += '   |' # add to '0    |   |   ' a triple space and |('   |') (Only make two of these)

                    else:  

                        cell = '  ' 

                        s += '   ' # if on third iteration, add triple space but no |

                        c = 0

                elif c < 3:

                    s += ' '+str(cell)+' ' # If cell is not 0, add ' num |'(3 spots with num in centre, then |)

                    s += '|'

                else:

                    s += ' '+str(cell)+' ' # If cell is not 0 (and on 3rd iter.), add ' num '(3 spots with num in centre))

                    c = 0

                    

                

            print(s)

            if x < 2:

                print('  '+'-'*11)

            x = x + 1

        print()

                

        #print('0'' ',myBoard.getValue(0,0),'|',myBoard.getValue(0,1),'|',myBoard.getValue(0,2))

        #print('  '+'-'*11)

        #print('1'' ',myBoard.getValue(1,0),'|',myBoard.getValue(1,1),'|',myBoard.getValue(1,2))

        #print('  '+'-'*11)

        #print('2'' ',myBoard.getValue(2,0),'|',myBoard.getValue(2,1),'|',myBoard.getValue(2,2))       

      



    #def getValue(self,row,col):

    # get number from specified location on board

        

        #if self.board[row][col] == 0:

            #return ' '

        #else:

            #return self.board[row][col]    

    





    def squareIsEmpty(self, row, col):

        '''

        Checks if a given square is empty

        Inputs:

           row (int) - row index of square to check

           col (int) - column index of square to check

        Returns: True if square is empty; False otherwise

        '''

        # TO DO: delete pass and complete method

        

        if self.board[row][col] == 'E':

            return True

        else:

            return False

        

        

        

    

    

    def update(self, row, col,c):

        '''

        Assigns the appropriate character (X or O) to the classicGame board at the provided row and column, 

        but only if that square is empty.

        Inputs:

           row (int) - row index of square to update

           col (int) - column index of square to update

           c   (int) - player switching counter (ensures player 1 and 2 alternate)

        Returns: True if attempted update was successful; False otherwise

        '''

        

        if self.squareIsEmpty(row,col):

            if player(c) == '1':

                self.board[row][col] = 'X'

            else:

                if player(c) == '2':

                    self.board[row][col] = 'O'                

            return True

        else:

            return False

        

        

    

    

    def boardFull(self):

        '''

        Checks if the board has any remaining empty squares.

        Inputs: none

        Returns: True if the board has no empty squares (full); False otherwise

        '''

        # TO DO: delete pass and complete method

        

        if any('E' in sl for sl in self.board):

            return False

        else:

            return True

            

        

           

    def isWinner(self):

        

        '''

        Checks whether the current player has just made a winning move.  In order

        to win, the player must a sequence of 3 squares that of their character (x or O). 

        That line can be horizontal, vertical, or diagonal.

        Inputs: none

        Returns: True if current player has won with their most recent move; 

                 False otherwise

        '''

        # TO DO: delete pass and complete method

        #row = ''.join(self.board[i])

            #if row == 'XXX' or row == 'OOO':

                #return True

            #elif:

                #row = ''.join(self.board[i])        

        for i in range(3):       

            

            if self.board[i][0]+self.board[i][1]+self.board[i][2] == 'XXX' or self.board[i][0]+self.board[i][1]+self.board[i][2] == 'OOO': # Check first row, then second row, third row

                return True

            elif self.board[0][i]+self.board[1][i]+self.board[2][i] == 'XXX' or self.board[0][i]+self.board[1][i]+self.board[2][i] == 'OOO' : # Check first column, then second col., third col

                return True

            elif self.board[0][0]+self.board[1][1]+self.board[2][2] == 'XXX' or self.board[0][0]+self.board[1][1]+self.board[2][2] == 'OOO': # Check diagonal (1,5,9)

                return True

            elif self.board[0][2]+self.board[1][1]+self.board[2][0] == 'XXX' or self.board[0][2]+self.board[1][1]+self.board[2][0] == 'OOO': # Check diagonal (3,5,7)

                return True

        else:

            return False

      





class MetaTicTacToe:

    def __init__(self, configFile):

        '''

        Initializes an empty Meta Tic Tac Toe board, based on the contents of a 

        configuration file.

        Inputs: 

           configFile (str) - name of a text file containing configuration information

        Returns: None

        '''       

        # TO DO: delete pass (and this comment) and complete method

        

        self.board = [] # list of lists, where each internal list represents a row

        self.size = 3   # number of columns and rows of board

        

        

        file = open(configFile,'r')

        configList = file.read().split() # Output as long list-> ['c', 'c', 'n', 'c', 'n', 'c', 'n', 'c', 'n']

        file.close()

        # Convert configList to nested structure -> [['c', 'c', 'n'], ['c', 'n', 'c'], ['n', 'c', 'n']

        c = 0

        for i in range(self.size):

            row = []

            for j in range(self.size):

                row.append(configList[c])

                c += 1

            self.board.append(row)

              



        # Output -> ['c c n', 'c n c', 'n c n']

        #config = []

        #file = open(configFile,'r')

        #for line in file:

            #line = line.strip()

            #config.append(line)

        #print(config)        

        

                

    def drawBoard(self):

        '''

        Displays the current state of the board, formatted with column and row 

        indices shown.

        Inputs: none

        Returns: None

        '''

        

        

        print('   0   1   2') # Print top line coordinates

        x = 0 # Initiaize value for column coordiantes

        c = 0 # counter to set number of '|'        

        for row in self.board:

            s = '%d ' % (x) # Initialize the '0 ' for each line of type ('0    |   |   ')

            for cell in row:

                c += 1

                if c < 3:

                    s += ' '+str(cell)+' ' # Add: ' char |' (3 spots with char in centre, then |)

                    s += '|'

                else:

                    s += ' '+str(cell)+' ' # On 3rd iter., add: ' char ' (3 spots with char in centre)

                    c = 0

                    

                

            print(s)

            if x < 2:

                print('  '+'-'*11) # Print demarcation line: '---------'

            x = x + 1

        print()





    def squareIsEmpty(self, row, col):

        '''

        Checks if a given square contains a non-played local game board ("empty"),

        or the result of a played local game board (not "empty").

        Inputs:

           row (int) - row index of square to check

           col (int) - column index of square to check

        Returns: True if square is empty; False otherwise

        '''

         # TO DO: delete pass (and this comment) and complete method

        if self.board[row][col] == 'c' or self.board[row][col] == 'n':

            return True

        else:

            return False

    

    

    def update(self, row, col, result):

        '''

        Assigns the string, result, to the board at the provided row and column, 

        but only if that square is "empty".

        Inputs:

           row (int) - row index of square to update

           col (int) - column index of square to update

           result (str) - entry to place in square (X, O, or D)

        Returns: True if attempted update was successful; False otherwise

        '''

         # TO DO: delete pass (and this comment) and complete method

        if self.squareIsEmpty(row,col):

            self.board[row][col] = result

            return True

        else:

            False

    

    

    def boardFull(self):

        '''

        Checks if the board has any remaining "empty" squares (i.e. any un-played

        local boards).

        Inputs: none

        Returns: True if the board has no "empty" squares (full); False otherwise

        '''

        # TO DO: delete pass (and this comment) and complete method

        for row in self.board:

            for cell in row:

                if cell == 'c' or cell == 'n':

                    return False

        else:

            return True

        

           

    def isWinner(self):

        '''

        Checks whether the current player has just made a winning move.  In order

        to win, the player must have just completed a line (of 3 squares) of their

        mark (three Xs for Player 1, three Os for Player 2), or 3 draws. That line

        can be horizontal, vertical, or diagonal.

        Inputs: none

        Returns: True if current player has won with their most recent move; 

                 False otherwise

        '''

        # TO DO: delete pass (and this comment) and complete method

        # Check all sequences for a sequence of identical items (ie: XXX, OOO, DDD)

        # Set code based on csestack.org

        

        # Note: this code is liable to returning a win incorrectly depending on the config file.

        # if Config file contains an identical sequence  (c,c,c), there will be a win. 

        

        #for row in self.board:

            #if len(set(row)) == 1: # Check all rows

                #return True

        #for i in range(3):

            #if len(set((self.board[0][i],self.board[1][i],self.board[2][i]))) == 1: # Check all columns

                #return True

        #if len(set((self.board[0][0],self.board[1][1],self.board[2][2]))) == 1: # Check diagonal (upper left start)

            #return True

        #elif len(set((self.board[0][2],self.board[1][1],self.board[2][0]))) == 1: # Check diagonal (upper right start)

            #return True

        #else:

            #return False

        for i in range(3):

            # Check all columns

            if self.board[0][i]+self.board[1][i]+self.board[2][i] == 'XXX' or self.board[0][i]+self.board[1][i]+self.board[2][i] == 'OOO' or self.board[0][i]+self.board[1][i]+self.board[2][i] == 'DDD': 

                return True 

            # Check all Rows

            if self.board[i][0]+self.board[i][1]+self.board[i][2] == 'XXX' or self.board[i][0]+self.board[i][1]+self.board[i][2] == 'OOO' or self.board[i][0]+self.board[i][1]+self.board[i][2] == 'DDD': 

                return True 

        # Check diagonal (upper left start)

        if self.board[0][0]+self.board[1][1]+self.board[2][2]== 'XXX' or self.board[0][0]+self.board[1][1]+self.board[2][2] == 'OOO' or self.board[0][0]+self.board[1][1]+self.board[2][2] == 'DDD': 

            return True

        # Check diagonal (upper right start)

        if self.board[0][2]+self.board[1][1]+self.board[2][0] == 'XXX' or self.board[0][2]+self.board[1][1]+self.board[2][0] == 'OOO' or self.board[0][2]+self.board[1][1]+self.board[2][0] == 'DDD': 

            return True

        else:

            return False        

    def getLocalBoard(self, row, col):

        '''

        Returns the instance of the empty local board at the specified row, col 

        location (i.e. either ClassicTicTacToe or NumTicTacToe).

        Inputs:

           row (int) - row index of square

           col (int) - column index of square

        Returns: instance of appropriate empty local board if un-played; 

                 None if local board has already been played

        '''

        # TO DO: delete pass (and this comment) and complete method

        instance = self.board[row][col]

        if instance == 'X' or instance == 'O' or instance == 'D':

            return None

        else:

            return instance

        

def player(c):

    '''

    Player switching function; ensures player 1 and 2 alternate when appropriate. Inititalizaes with returning player 1, then alternates

    inputs: c (int) - Player switching counter

    outputs: player - set to either '1' or '2'

    '''

    if c % 2 == 0:    

        player = '1'

        

    else:    

        player = '2'

        

    return player

        

def winningChar(c):

    '''

    Returns corressponding character of winning player (X or O)

    inputs: c (int) - Player switching counter

    outputs: char - character of winning player (X or O)

    '''

    if c % 2 == 0:            

        char = 'X'

    else:            

        char = 'O'   

    

    return char





def getCoord(c):

    '''

    Validates and prompts player for the row and col values

    Validates all entries: 1. checks ints are proper range; 2. checks if invalid literal given (ie. non-ints)

    inputs: c (int) - Player switching counter

    Returns: row and col ints

    '''

    tryLoop = True

    while tryLoop: # validate correct range of row numbers

        try:

            row = int(input('Player %s, please enter a row: ' % player(c)))

            assert(row<3 and row > -1),'Sorry you have inputed an incorrect number.' 

            

        except AssertionError as i:

            print(i.args[0])

        except Exception:

            print('You have not entered a number')

        else:

            tryLoop = False

    tryLoop2 = True

    while tryLoop2: # validate correct range of col numbers

        try:

            col = int(input('Player %s, please enter a column: ' % player(c)))

            assert(col<3 and col > -1),'Sorry you have inputed an incorrect number.'        

            

        except AssertionError as i:

            print(i.args[0])

        except Exception:

            print('You have not entered a number')

        else:

            tryLoop2 = False    

    return row, col



def numGamePrompts(c):

    '''

    prompts and validates player for number choice in Numerical Game according to player 1 or 2.

    Validates that each player choses correctly either even or odd numbers

    inputs: c (int) - Player switching counter

    outputs: num - int of value given by player

    '''

    if c % 2 == 0:

        num = int(input('Player %s, please enter an even number (2-8): ' % player(c)))

        assert(num%2==0),'sorry you have inputed a wrong number.'

        

    else:

        num = int(input('Player %s, please enter an odd number (1-9): ' % player(c)))

        assert(num%2==1),'sorry you have inputed a wrong number.'

        

     

        

    return num

    

#def determineClassicOrNum(boardType):

    ## based on board type chosen by player, instantiate the correct game type class and return that instantiation.

    #if boardType == 'c':

        #return  1

    #elif boardType == 'n':

        #return  2

    

def displayWinner(c):

    '''

    Prints on screen winning player for inner board games (Classic or Numerical)

    inputs: c (int) - Player switching counter

    outputs: None

    '''

    print('Player %s wins. Congrats!' % player(c))



def displayFinalWinner(c):

    '''

    Prints on screen final winner of global game.

    inputs: c (int) - Player switching counter

    outputs: none

    '''

    print('Player %s wins Meta Tic Tac Toe game. GOOD GAME!' % player(c))

    

def displayTie():

    '''

    prints on screen if there is a tie

    inputs: none

    outputs: none

    '''

    print("It's a tie")

    

def main():

    '''

    Runs program flow.

    Instantiates Meta class, Numerical Class and Classic class

    Runs loops on each instantiation according to needs of the game.

    inputs: none

    outputs: none

    ''' 

    

    

    c = 2 # Player switching counter. Initialized at 2 (player 1)

    game = True

    globalBoard = MetaTicTacToe('MetaTTTconfig.txt')

    TITLE = "Starting new Meta Tic Tac Toe game"

    print("-"*len(TITLE))

    print(TITLE)

    print("-"*len(TITLE))    

    while game: # GLOBAL BOARD LOOP HERE

        

        globalBoard.drawBoard()

        

        # Player selects cell from global board; returns ints: (row, col)

        mainTryLoop = True

        while mainTryLoop: # validate correct row and col numbers

            try:

                boardTypePosition = getCoord(c)

            except AssertionError as i:

                print(i.args[0])

            else:

                mainTryLoop = False

        

        # returns None (if X, O or D), returns c or n for classic and num.

        boardType = globalBoard.getLocalBoard(boardTypePosition[0],boardTypePosition[1]) 

        

        

        localGameLoop = True

        if boardType == 'c': # Classic Game Code Starts Here

            classicGame = ClassicTicTacToe()

            print("-"*((len(TITLE))+2))

            print('This is a Classical Tic Tac Toe Game') 

            while localGameLoop: # CLASSIC GAME LOOP HERE            

                classicGame.drawBoard()

                

                classicTryLoop = True

                while classicTryLoop: # validate correct row and col numbers

                    try:

                        coord = getCoord(c) # returns a tuple and validates entry within proper range

                    except AssertionError as i:

                        print(i.args[0])

                    else:

                        if classicGame.update(coord[0],coord[1],c): # Returns True if update works, and updates classic board

                            classicTryLoop = False

                        else:

                            print('Error: could not make move!')

                            classicGame.drawBoard()

                

               

                

                #classicGame.update(coord[0],coord[1],c)

                if classicGame.isWinner(): # Check for winner

                    localGameLoop = False

                    classicGame.drawBoard()

                    displayWinner(c)

                    globalBoard.update(boardTypePosition[0],boardTypePosition[1],winningChar(c))

                    

                elif classicGame.boardFull(): # Check for tie (board full but no winner)

                    displayTie()

                    classicGame.drawBoard()

                    localGameLoop = False

                    globalBoard.update(boardTypePosition[0],boardTypePosition[1],'D') # Update Global board with 'D'                   

                    c += 1

                else:

                    c += 1

                         

        else:

            if boardType == 'n': # NUMERICAL GAME LOOP HERE              

                numGame = NumTicTacToe()

                print("-"*((len(TITLE))+2))

                print('This is a Numerical Tic Tac Toe Game')                

                while localGameLoop:                

                    numGame.drawBoard()

                    

                    numTryLoop = True

                    while numTryLoop: # validate correct even and odd numbers

                        try:

                            num = numGamePrompts(c) # validates and returns the num chosen

                        except AssertionError as i:

                            print(i.args[0])

                        else:

                            numTryLoop = False

                            

                    coordLoop = True

                    while coordLoop: # validate and get coordinates

                        try:

                            numGameCoord = getCoord(c) # validates and returns the coords chosen

                        except AssertionError as i:

                            print(i.args[0])

                        else:

                            if numGame.update(numGameCoord[0],numGameCoord[1],num): # returns True if update works, and updates num board

                                coordLoop = False

                            else:

                                print('Error: could not make move!')

                                numGame.drawBoard()          

                        

                    

                    if numGame.isWinner(): # Check for winner

                        localGameLoop = False

                        numGame.drawBoard()

                        displayWinner(c)

                        globalBoard.update(boardTypePosition[0],boardTypePosition[1],winningChar(c))

                        

                    elif numGame.boardFull(): # check for tie (board full but no winner)

                        displayTie()

                        numGame.drawBoard()

                        localGameLoop = False

                        globalBoard.update(boardTypePosition[0],boardTypePosition[1],'D')

                        c += 1                        

                    else:

                        c += 1

            else:

                c += 1 

            

        if globalBoard.isWinner(): # CHECK GLOBAL BOARD FOR FINAL WINNER

            displayFinalWinner(c)

            globalBoard.drawBoard()

            game = False

            

        #else: # Increment up to switch players.  This increment fouls up player switching. Do not use.

            #c += 1

  

main()



'''

if __name__ == "__main__":

    

    # TEST EACH CLASS THOROUGHLY HERE

    

    ##############################

    ##############################

    ##     Meta Board Tests    ###

    ##############################

    ##############################    

    

    line = '='*18

    print()

    print('ALL TESTS SHOWING BELOW')

    print()

    print('TESTS FOR META TIC TAC TOE CLASS')

    print(line)

    

    # Instantiate

    globalBoard = MetaTicTacToe('MetaTTTconfig.txt')

    

    # Draw test

    print('1. Draw global board according to configuration file given:')

    print()

    globalBoard.drawBoard()

    

    

    #test getLocalBoard

    print('2. Test return value of getLocalBoard(). Returns either "c" or "n".')

    print('Local board type:',globalBoard.getLocalBoard(0,0))

    print('Local board type:',globalBoard.getLocalBoard(2,2))

    print()

    

    

    

    

    # Test squareIsEmpty()

    print('3. Test squareIsEmpty() function on globalBoard. All should be True.')

    print(globalBoard.squareIsEmpty(0,0)) # all should be True

    print(globalBoard.squareIsEmpty(0,1))

    print(globalBoard.squareIsEmpty(0,2))

    print(globalBoard.squareIsEmpty(2,2))

    print()

      

      

    # test isWinner on globalBoard

    print('4. Test isWinner on globalBoard. should be False.')

    print('Is win?',globalBoard.isWinner()) # should be False

    print()

    

    # Test update on globalBoard

    print('5. Test update() on globalBoard')

    print('   Update with two "X"s and one "O"')

    

    globalBoard.update(0,0,'X')

    globalBoard.update(0,1,'X')

    globalBoard.update(2,2,'O')

    

    globalBoard.drawBoard()

    

    print('5.a. Test isWinner()? should be FALSE')# should be False

    print('Is win?',globalBoard.isWinner())

    print()

    

    print('5.b. Update board with a winning move')

    globalBoard.update(0,2,'X')

    globalBoard.drawBoard()



    print('    Test isWinner()? Should be TRUE') # should be True

    print('    Is win?', globalBoard.isWinner())

    print()

    

    print('6. Reset globalBoard to configuration file.')

    globalBoard = MetaTicTacToe('MetaTTTconfig.txt')

    globalBoard.drawBoard()

    print()

    

    print('7. Fill fresh board with winning "O"s')

    globalBoard.update(2,0,'O')

    globalBoard.update(2,1,'O')

    globalBoard.update(2,2,'O')

    globalBoard.drawBoard()

    

    print()    

    

    print('8. Test isWinner(). Should be TRUE')

    print('Is win?', globalBoard.isWinner()) 

    print()   

    

    # Board Full test

    print('9. Test boardFull(). Should give False')

    print('boardFull?',globalBoard.boardFull()) #--> should give False

    print()    

    

    print('10. Reset globalBoard and test a draw win.')

    globalBoard.update(1,0,'D')

    globalBoard.update(1,1,'D')

    globalBoard.update(1,2,'D')

    globalBoard.drawBoard()

    

    print('Is win?', globalBoard.isWinner()) 

    print() 

    

    print('11. Reset board and test a DIAGONAL draw win.')

    globalBoard = MetaTicTacToe('MetaTTTconfig.txt')

    globalBoard.update(0,0,'D')

    globalBoard.update(1,1,'D')

    globalBoard.update(2,2,'D')

    globalBoard.drawBoard()

    

    print('Is win?', globalBoard.isWinner()) 

    print()    

        

    print('12. Reset board and test a DIAGONAL "X" win.')

    globalBoard = MetaTicTacToe('MetaTTTconfig.txt')

    globalBoard.update(0,0,'X')

    globalBoard.update(1,1,'X')

    globalBoard.update(2,2,'X')

    globalBoard.drawBoard()

    print('Is win?', globalBoard.isWinner()) 

    print()     

    

    

    print('12. Reset board and test other DIAGONAL "O" win.')

    globalBoard = MetaTicTacToe('MetaTTTconfig.txt')

    globalBoard.update(0,2,'O')

    globalBoard.update(1,1,'O')

    globalBoard.update(2,0,'O')

    globalBoard.drawBoard() 

    print('Is win?', globalBoard.isWinner()) 

    print()     

    

    print('12a. Reset new board, and test a column win')

    globalBoard = MetaTicTacToe('MetaTTTconfig.txt')

    globalBoard.update(0,2,'O')

    globalBoard.update(1,2,'O')

    globalBoard.update(2,2,'O')

    globalBoard.drawBoard()

    print('Is win?', globalBoard.isWinner()) 

    print()     

         

    

    print('13. Reset globalBoard to configuration file.')

    globalBoard = MetaTicTacToe('MetaTTTconfig.txt')

    globalBoard.drawBoard()

    print() 

    

    print('14. Fill board')

    globalBoard = MetaTicTacToe('MetaTTTconfig.txt')

    

    globalBoard.update(1,0,'X')

    globalBoard.update(1,1,'O')

    globalBoard.update(1,2,'X')

    globalBoard.update(0,0,'D')

    globalBoard.update(0,1,'O')

    globalBoard.update(0,2,'D')

    globalBoard.update(2,0,'D')

    globalBoard.update(2,1,'D')

    globalBoard.update(2,2,'O')

    

    globalBoard.drawBoard()

    print()

    print('15. Test boardFull(). Should give TRUE')

    print('boardFull?',globalBoard.boardFull()) #--> should give False

    print() 

    

    print('16. Test is win. Should give FALSE.')

    print('Is win?',globalBoard.isWinner())

    print()

    

    

    ##############################

    ##############################

    ## Classic Tic Tac Toe Tests #

    ##############################

    ##############################  

    

    print('CLASSIC TIC TAC TOE CLASS TESTS BELOW')

    print(line)

    

    print()

    print('1. Show empty classic board.')

    print()

    classicGame = ClassicTicTacToe()

    classicGame.drawBoard() 

    

    

    # Test squareIsEmpty()

    print('2. Test squareIsEmpty() function on classicGame. All should be True.')

    print()

    print(classicGame.squareIsEmpty(0,0)) # all should be True

    print(classicGame.squareIsEmpty(0,1))

    print(classicGame.squareIsEmpty(0,2))

    print(classicGame.squareIsEmpty(2,2))

    print()

    

    # Update two plays on Classic Board 

    print()

    print('3. Update two plays. Should alternate x and O automatically.')

    print()

    classicGame.update(0,0,2)

    classicGame.update(0,1,3)

    classicGame.drawBoard()

    print()

      

    # test isWinner on classicGame

    print('4. Test isWinner on classicGame. Should be False.')

    print('Is win?',classicGame.isWinner()) # should be False

    print()

    

    # Test further updates on classicGame

    print()

    print('5. Test update(): add 4 more plays on classicGame')

      

    

    classicGame.update(1,2,4)

    classicGame.update(1,1,5)

    classicGame.update(2,2,6)

    classicGame.update(1,0,7)

    

    classicGame.drawBoard()

    

    print('5.a. Test isWinner()? should be FALSE')# should be False

    print('Is win?',classicGame.isWinner())

    print()

    

    print('5.b. Update board with a winning move')

    print()

    classicGame.update(0,2,8)

    classicGame.drawBoard()



    print('    Test isWinner()? Should be TRUE') # should be True

    print('    Is win?', classicGame.isWinner())

    print()

    

    

    print('6. Fill fresh board with winning "O"s')

    classicGame = ClassicTicTacToe()

    

    

    classicGame.update(0,1,2)

    classicGame.update(0,0,3)

    classicGame.update(2,1,4)    

    classicGame.update(1,1,5)

    classicGame.update(2,0,6)

    classicGame.update(2,2,7)

    classicGame.drawBoard()

    

    print()    

    

    print('7. Test isWinner(). Should be TRUE')

    print('Is win?', classicGame.isWinner()) 

    print()

    

    # Update a square already taken

    print('8. Test updating a square already taken. Should return False')

    print()

    classicGame.drawBoard()    

    print('Update position 0,0')

    print('return value:',classicGame.update(0,0,8))

    print()

    

    ## Board Full test

    print('9. Test boardFull(). Should give False')

    print('boardFull?',classicGame.boardFull()) #--> should give False

    print()    

    

    

    # Fill board

    print('10. Fill board up and test boardFull()')

    print()

    classicGame.update(0,2,9)

    classicGame.update(1,0,10)

    classicGame.update(1,2,11)

    classicGame.drawBoard()    

    print()    

    print('boardFull() returns:',classicGame.boardFull())

    

    ################################

    ################################

    ## Numerical Tic Tac Toe Tests #

    ################################

    ################################ 

    

    print()

    print('NUMERICAL TIC TAC TOE TEST BELOW')

    print(line)

    print()

    

    # print empty board

    print('1. Show empty Numerical Board.')

    print()

    numGame = NumTicTacToe()

    numGame.drawBoard()

    

    # Add a number

    print('1. Add a number to board.')

    print()

    numGame.update(2,2,8)

    numGame.drawBoard()    

    

    # Add a number

    print('2. Add more numbers to board.')

    print()

    numGame.update(2,1,2)

    numGame.update(0,1,1)

    numGame.update(0,2,7)

    numGame.update(1,2,4)

    numGame.drawBoard()

    

    # Check if board is full

    print('3. Check if board is full. Should be False')

    print()

    print('boardFull?',numGame.boardFull())

    print()

    

    # Make winning sequence and check isWinner()

    

    print('4. Make a winning sequence and check isWinner()')

    print()

    numGame.update(2,0,5)

    numGame.drawBoard()

    print('isWinner()?',numGame.isWinner())

    print()

    

    # Clear board and test diagonal win

    

    print('5. Clear board and test diagonal win.')

    print()

    numGame = NumTicTacToe()

    numGame.update(2,0,5)

    numGame.update(1,1,6)

    numGame.update(0,2,4)

    numGame.drawBoard()

    print('isWinner()?',numGame.isWinner())    

    print()

    

    # Clear board and test column win

        

    print('5. Clear board and test column win.')

    print()

    numGame = NumTicTacToe()

    numGame.update(0,0,5)

    numGame.update(1,0,6)

    numGame.update(2,0,4)

    numGame.drawBoard()

    print('isWinner()?',numGame.isWinner()) 

    print()

    

    # Test squareIsEmpty() returns

    

    print('6. Test squareIsEmpty() returns True on empty square.')

    print('squareIsEmpty(2,2)?',numGame.squareIsEmpty(2,2))

    print()

    

    print('7. Test squareIsEmpty() returns False on full square.')

    print('squareIsEmpty(2,0)?',numGame.squareIsEmpty(2,0)) 

    

'''   

    

        

