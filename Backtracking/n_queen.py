#exam - solve code only 
class Nqueen:
    def solveNqueen(self,n):
        board =[['.' for _ in range(n)] for _ in range(n)]
        result = []
    
    def solve(self,col,board,result,n):
        if col ==n:
            pass

        for row in range(n):
            if self.isSafe(row,col,board,n):
                board[row][col] = 'Q'
                self.solve(col+1,board,result,n)
                board[row][col] = '.'


    def isSafe(self,row,col,board,n):
        #check horizantally
        i = row
        for j in range(n):
           if board[row][j] == 'Q': #j 
                return False
        
        #vertical 
        for i in range(n):
            if board[i][col] == 'Q':
                return False

        #checking diagonal upward left 
        i = row 
        j = col
        while i >=0 and j >=0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        #checking diagonal downward left
        i = row 
        j = col 
        while i >=0 and j < n:
            if board[i][j] == 'Q':
                return False
            i += 1                        
            j -= 1

        #checking diagonal downward right
        i = row
        j = col
        while i < n and j < n:
            if board[i][j] == 'Q':
                return False
            i += 1
            j += 1

        return True     

            
                


