print("WELCOME TO TIC TAC TOE - KRISHNAPRASADH.R")

#VARIABLES
flag=1
drawvalue=0
rowvalue=0
columnvalue=0

#GET BOARD VALUES
try:
    boardvalue=int(input("\nEnter Board value 3-10: "))
except ValueError:
    print("Rowvalue and ColumnValue must be an integer")
    exit()

#CREATE BOARD
if((boardvalue) >=3 and (boardvalue) <=10):
    board=list("%02d" % a for a in range(0,boardvalue*boardvalue))
    for i in [board[c:c+boardvalue] for c in range(0,len(board),boardvalue) if c%boardvalue == 0]:
        print("\t")
        print(*i)   #PRINT LIST AS BOARD
        print("\t")
else:
    print("Rowvalue and Columnvalue must be greater than 3 and less than 10")
    exit()

#DIAGONAL VALUES
leftdiagonal=list(range(0, boardvalue*boardvalue, boardvalue+1))
rightdiagonal=list(range(boardvalue-1,boardvalue*boardvalue-1,boardvalue-1))

#ROW VALUES
row_list = [board[rowlist:rowlist+boardvalue] for rowlist in range(0, len(board),boardvalue)]
row_list = [list(map(int, rowx)) for rowx in row_list]

#for rowlist in range(0, len(board),boardvalue):
#    globals()['row%s' % rowvalue]=[]
#    globals()['row%s' % rowvalue]=(board[rowlist:rowlist+boardvalue])
#    globals()['row%s' % rowvalue] = list(map(int, globals()['row%s' % rowvalue])) 
#    rowvalue=rowvalue+1
#rowvalue=0

#COLUMN VALUES
column_list=[board[i::boardvalue] for i in range(boardvalue)]
column_list = [list(map(int, columnx)) for columnx in column_list]

#column_list = [list(map(int, column_list)) for column_list in nested]
#for i in range(boardvalue):
#    globals()['column%s' % columnvalue]=[]
#    globals()['column%s' % columnvalue]=board[i::boardvalue]
#    globals()['column%s' % columnvalue] = list(map(int, globals()['column%s' % columnvalue]))
#    columnvalue=columnvalue+1
#columnvalue=0

#USER PLAY
while True:
        try:
            if(flag%2!=0):
                value=int(input("Player XX - Enter value between 0-"+str(boardvalue*boardvalue-1)+": "))
            else:
                value=int(input("Player OO - Enter value between 0-"+str(boardvalue*boardvalue-1)+": "))
        except ValueError:
            print("Error - That wasn't an integer")
    
        try:
            if (board[value]!="XX" and board[value]!="OO"):
                if(flag%2!=0):
                    board[value]="XX"
                    drawvalue=drawvalue+1
                    flag=flag+1
                else:
                    board[value]="OO"
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
        if(all(board[leftvalues]=="XX" for leftvalues in leftdiagonal)==1):
            print("Player XX Wins - Left Diagonal")
            exit()
        if(all(board[leftvalues]=="OO" for leftvalues in leftdiagonal)==1):
            print("Player OO Wins - Left Diagonal")
            exit()
        if(all(board[rightvalues]=="XX" for rightvalues in rightdiagonal)==1):
            print("Player XX Wins - Right Diagonal")
            exit()
        if(all(board[rightvalues]=="OO" for rightvalues in rightdiagonal)==1):
            print("Player OO Wins - Right Diagonal")
            exit()
        
        #ROW CHECK
        for rowvalues in range(0,boardvalue):
            if(all(board[rowvalues]=="XX" for rowvalues in row_list[rowvalues])==1):
                print("Player XX Wins - ROW"+str(rowvalues))
                exit()
        for rowvalues in range(0,boardvalue):
            if(all(board[rowvalues]=="OO" for rowvalues in row_list[rowvalues])==1):
                print("Player OO Wins - ROW"+str(rowvalues))
                exit()
        
        #COLUMN CHECK
        for columnvalues in range(0,boardvalue):
            if(all(board[columnvalues]=="XX" for columnvalues in column_list[columnvalues])==1):
                print("Player XX Wins - COLUMN"+str(columnvalues))
                exit()
        for columnvalues in range(0,boardvalue):
            if(all(board[columnvalues]=="OO" for columnvalues in column_list[columnvalues])==1):
                print("Player OO Wins - COLUMN"+str(columnvalues))
                exit()
        
        #DRAW CHECK
        if(drawvalue==boardvalue*boardvalue):
            print("DRAW MATCH")
            exit()