board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
i=1
print("\t"+board[0]+"\t"+board[1]+"\t"+board[2])
print("\t"+board[3]+"\t"+board[4]+"\t"+board[5])
print("\t"+board[6]+"\t"+board[7]+"\t"+board[8])
while True:
        try:
            if(i%2!=0):
                value=int(input("Player X - Enter value between 0-8: "))
            else:
                value=int(input("Player O - Enter value between 0-8: "))
        except ValueError:
            print("Error - That wasn't an integer")
    
        try:
            if (board[value]!="X" and board[value]!="O"):
                if(i%2!=0):
                    board[value]="X"
                    i=i+1
                else:
                    board[value]="O"
                    i=i+1
        except IndexError:
            print("Error - Expected values 0-8")
        
        print("\t"+board[0]+"\t"+board[1]+"\t"+board[2])
        print("\t"+board[3]+"\t"+board[4]+"\t"+board[5])
        print("\t"+board[6]+"\t"+board[7]+"\t"+board[8])
        
        if(board[0]=="X" and board[1]=="X" and board[2]=="X"):
            print("Player X - Wins")
            exit()
        if(board[3]=="X" and board[4]=="X" and board[5]=="X"):
            print("Player X - Wins")
            exit()
        if(board[6]=="X" and board[7]=="X" and board[8]=="X"):
            print("Player X - Wins")
            exit()
        if(board[0]=="X" and board[3]=="X" and board[6]=="X"):
            print("Player X - Wins")
            exit()
        if(board[1]=="X" and board[4]=="X" and board[7]=="X"):
            print("Player X - Wins")
            exit()
        if(board[2]=="X" and board[5]=="X" and board[8]=="X"):
            print("Player X - Wins")
            exit()
        if(board[0]=="X" and board[4]=="X" and board[8]=="X"):
            print("Player X - Wins")
            exit()
        if(board[2]=="X" and board[4]=="X" and board[6]=="X"):
            print("Player X - Wins")
            exit()
            
        if(board[0]=="O" and board[1]=="O" and board[2]=="O"):
            print("Player O - Wins")
            exit()
        if(board[3]=="O" and board[4]=="O" and board[5]=="O"):
            print("Player O - Wins")
            exit()
        if(board[6]=="O" and board[7]=="O" and board[8]=="O"):
            print("Player O - Wins")
            exit()
        if(board[0]=="O" and board[3]=="O" and board[6]=="O"):
            print("Player O - Wins")
            exit()
        if(board[1]=="O" and board[4]=="O" and board[7]=="O"):
            print("Player O - Wins")
            exit()
        if(board[2]=="O" and board[5]=="O" and board[8]=="O"):
            print("Player O - Wins")
            exit()
        if(board[0]=="O" and board[4]=="O" and board[8]=="O"):
            print("Player O - Wins")
            exit()
        if(board[2]=="O" and board[4]=="O" and board[6]=="O"):
            print("Player O - Wins")
            exit()
            
        if(board[0].isupper() and board[1].isupper() and board[2].isupper() and board[3].isupper() and board[4].isupper() and board[5].isupper() and board[6].isupper() and board[7].isupper() and board[8].isupper()):
            print("DRAW MATCH")
            exit()