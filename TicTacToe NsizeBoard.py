#import modules
import random

#VARIABLES
player1="XX"
player2="OO"
flag=1
drawvalue=0
rowvalue=0
columnvalue=0
multiplayerflag=0
leftdiagonalai=0
rightdiagonalai=0
rowai=0
columnai=0

#GET BOARD VALUES
try:
    boardvalue=int(input("\nEnter Board value 3-10: "))
except ValueError:
    print("Board value must be an integer")
    exit()

#CREATE BOARD
if((boardvalue) >=3 and (boardvalue) <=10):
    board=list("%02d" % a for a in range(0,boardvalue*boardvalue))
    for i in [board[c:c+boardvalue] for c in range(0,len(board),boardvalue) if c%boardvalue == 0]:
        print("\t")
        print(*i)   #PRINT LIST AS BOARD
        print("\t")
else:
    print("Board value must be greater than 3 and less than 10")
    exit()

#Multiplayer or CPU
try:
    multiplayerflag=int(input("\n0 for 2P; 1 for CPU: "))
    if(multiplayerflag>1 or multiplayerflag<0):
        print("0 for 2P and 1 for CPU")
        exit()
except ValueError:
    print("0 for 2P and 1 for CPU - Must be an integer")
    exit()

#DIAGONAL VALUES
leftdiagonal=list(range(0, boardvalue*boardvalue, boardvalue+1))
rightdiagonal=list(range(boardvalue-1,boardvalue*boardvalue-1,boardvalue-1))

#ROW VALUES
row_list = [board[rowlist:rowlist+boardvalue] for rowlist in range(0, len(board),boardvalue)]
row_list = [list(map(int, rowx)) for rowx in row_list]
#INDIVIDIUAL ROW VALUES
for rowlist in range(0, len(board),boardvalue):
    globals()['row%s' % rowvalue]=[]
    globals()['row%s' % rowvalue]=(board[rowlist:rowlist+boardvalue])
    globals()['row%s' % rowvalue] = list(map(int, globals()['row%s' % rowvalue])) 
    rowvalue=rowvalue+1
rowvalue=0

#COLUMN VALUES
column_list=[board[i::boardvalue] for i in range(boardvalue)]
column_list = [list(map(int, columnx)) for columnx in column_list]
#INDIVIDIUAL COLUMN VALUES
for i in range(boardvalue):
    globals()['column%s' % columnvalue]=[]
    globals()['column%s' % columnvalue]=board[i::boardvalue]
    globals()['column%s' % columnvalue] = list(map(int, globals()['column%s' % columnvalue]))
    columnvalue=columnvalue+1
columnvalue=0

#USER PLAY
while True:
        try:
            if(flag%2!=0):
                value=int(input("Player "+player1+" - Enter value between 0-"+str(boardvalue*boardvalue-1)+": "))
            elif(flag%2==0 and multiplayerflag==1):
                value=random.randrange(boardvalue*boardvalue)
                #LeftDiagonalAI
                for x in leftdiagonal:
                    if board[x]==player1:
                        leftdiagonalai=leftdiagonalai+1
                        if(leftdiagonalai==len(leftdiagonal)-1):
                            for x in leftdiagonal:
                                if board[x]!=player1:
                                    value=x
                #RightDiagonalAI
                for x in rightdiagonal:
                    if board[x]==player1:
                        rightdiagonalai=rightdiagonalai+1
                        if(rightdiagonalai==len(rightdiagonal)-1):
                            for x in rightdiagonal:
                                if board[x]!=player1:
                                    value=x
                #RowAI
                for x in range(boardvalue):
                    for y in globals()['row%d' % x]:
                        if board[y]==player1:
                            rowai=rowai+1
                            if(rowai==len(globals()['row%d' % x])-1):   # == with %
                                for x in range(boardvalue):
                                    for y in globals()['row%d' % x]:
                                        if board[y]!=player1:
                                            value=y
                #ColumnAI
                for x in range(boardvalue):
                    for y in globals()['column%d' % x]:
                        if board[y]==player1:
                            columnai=columnai+1
                            if(columnai==len(globals()['column%d' % x])-1): # == with %
                                for x in range(boardvalue):
                                    for y in globals()['column%d' % x]:
                                        if board[y]!="XX":
                                            value=y
            else:
                value=int(input("Player "+player2+" - Enter value between 0-"+str(boardvalue*boardvalue-1)+": "))
        except ValueError:
            print("Error - That wasn't an integer")
    
        try:
            if (board[value]!=player1 and board[value]!=player2):
                if(flag%2!=0):
                    board[value]=player1
                    drawvalue=drawvalue+1
                    flag=flag+1
                else:
                    board[value]=player2
                    drawvalue=drawvalue+1
                    flag=flag+1
        except IndexError:
            print("Error - Expected values 0-"+str(boardvalue*boardvalue-1))
        
        #PRINT LIST AS BOARD
        for i in [board[c:c+boardvalue] for c in range(0,len(board),boardvalue) if c%boardvalue == 0]:
            print("\t")
            print(*i)
            print("\t")
        
        #DIAGONAL CHECK
        if(all(board[leftvalues]==player1 for leftvalues in leftdiagonal)==1):
            print("Player "+player1+" Wins - Left Diagonal")
            exit()
        if(all(board[leftvalues]==player2 for leftvalues in leftdiagonal)==1):
            print("Player "+player2+" Wins - Left Diagonal")
            exit()
        if(all(board[rightvalues]==player1 for rightvalues in rightdiagonal)==1):
            print("Player "+player1+" Wins - Right Diagonal")
            exit()
        if(all(board[rightvalues]==player2 for rightvalues in rightdiagonal)==1):
            print("Player "+player2+" Wins - Right Diagonal")
            exit()
        
        #ROW CHECK
        for rowvalues in range(0,boardvalue):
            if(all(board[rowvalues]==player1 for rowvalues in row_list[rowvalues])==1):
                print("Player "+player1+" Wins - ROW "+str(rowvalues+1))
                exit()
        for rowvalues in range(0,boardvalue):
            if(all(board[rowvalues]==player2 for rowvalues in row_list[rowvalues])==1):
                print("Player "+player2+" Wins - ROW "+str(rowvalues+1))
                exit()
        
        #COLUMN CHECK
        for columnvalues in range(0,boardvalue):
            if(all(board[columnvalues]==player1 for columnvalues in column_list[columnvalues])==1):
                print("Player "+player1+" Wins - COLUMN "+str(columnvalues+1))
                exit()
        for columnvalues in range(0,boardvalue):
            if(all(board[columnvalues]==player2 for columnvalues in column_list[columnvalues])==1):
                print("Player "+player2+" Wins - COLUMN "+str(columnvalues+1))
                exit()
        
        #DRAW CHECK
        if(drawvalue==boardvalue*boardvalue):
            print("DRAW MATCH")
            exit()