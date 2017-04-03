import Epic

def pickWord():
    return 'apples'

def displayBoard(board):
    for ch in board:
        print "%s " % ch,
    print

def askUserForLetter():
    l = Epic.userString("Please select a letter: ")
    return l

def main():
    word = pickWord()
    board = []
    for ch in word:
        board.append('*')
    print board
    
    misses = 0
    gameOver = False
    while gameOver != True:
        displayBoard(board)
        letter = askUserForLetter()
        #if updateBoard(board, word, letter) == False:
         #   misses += misses
main()