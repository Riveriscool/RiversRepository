"""class Board:
    def __init__(self):
        self.board =  [[" ", " ", " "],
                       [" ", " ", " "],
                       [" ", " ", " "]]
    def display(self):
        print("---+---+---")
        for i in range(len(self.board)):
            print(self.board[i][0], " |", self.board[i][1], "| ", self.board[i][2])
            print("---+---+---")
            
        print(board)
    def gamestate(self):
        for i in range(len(self.board)):
            if self.board[i] == ["X","X","X"]:
                return "X"
            if self.board[i] == ["Y","Y","Y"]:
                return "Y"
        
                
        
    def canmove(self, posx, posy):
        if self.board[posy-1][posx-1] ==  " ":
            return True
        else: 
            return False
            
    
    def place(self, char, posx, posy):
        
        self.board[posy-1][posx-1] = char
        
            
        
    
    def turn(self, char, posx, posy):
        if self.canmove(posx, posy) == True:
            self.place(char, posx, posy)
            return True
        else:
            return False
    
    def main(self):
        i = 0
        done = False
        while done == False:
            x_coordinate = int(input("what x coordinate ")) + 1#1,2,3
            y_coordinate = int(input("what y coordinate")) + 1#1,2,3 but bottom is 1
            if i%2 == 0:
                player = "X"
            else:
                player = "O"
            success = self.turn(player, x_coordinate, y_coordinate)
            if success:
                #self.display()
                self.display()
            i += 1

board = Board()
board.main()"""

class Smallboard:
    def __init__(self):
        self.board =  [[" ", " ", " "],
                       [" ", " ", " "],
                       [" ", " ", " "]]
    def display(self):
        
        string = ''
        
        for i in range(len(self.board)):
            if i < len(self.board) - 1:
                string += "\n" +self.board[i][0]+ "  | "+ self.board[i][1]+ " | "+ self.board[i][2]
                string += ("\n" + "---+---+---")
            else:
                string += "\n" +self.board[i][0]+ "  | "+ self.board[i][1]+ " | "+ self.board[i][2]
        return string
    def place(self, char, posx, posy):
        self.board[posy][posx] = char
        
    
        
    def canmove(self, posx, posy):
        if self.board[posy-1][posx-1] ==  " ":
            return True
        else: 
            return False
    def turn(self, char, posx, posy):
        if self.canmove(posx, posy) == True:
            self.place(char, posx, posy)
            return True
        else:
            return False
        
        
    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            # Check rows
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != "":
                return self.board[i][0]
            # Check columns
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != "":
                return self.board[0][i]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != "":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != "":
            return self.board[0][2]

        # Check for a tie
        for row in self.board:
            if "" in row:
                # If any cell is still empty, the game is ongoing
                return ""
        
        # If no winner and no empty cells, it's a tie
        return "T"
class Bigboard:
    def __init__(self):
        self.board = [
            [Smallboard(), Smallboard(), Smallboard()],
            [Smallboard(), Smallboard(), Smallboard()],
            [Smallboard(), Smallboard(), Smallboard()]
            
        ]
        self.stateboard = [
            ["","",""],
            ["","",""],
            ["","",""]
        ]
        self.solved = False
    def display(self):
        #
        string = "             ||           ||          "
        print(self.board[0][0].display())
        for i in range(len(self.board)):
            #break each board into lines, concatinate lines into rows, then put together
            first,second,third = self.board[i][0].display().split("\n"),self.board[i][1].display().split("\n"),self.board[i][2].display().split("\n")
            print(f'first:{first}, second:{second}, third:{third}')
            #firstrow = first[0]+ "||"+second[0]+ "||"+third[0]
            secondrow = "  " +first[1] + " ||" + second[1] + " ||" + third[1]
            thirdrow = "  "+first[2] + "||" + second[2] + "||" + third[2]
            fourthrow = "  " + first[3] + " ||" + second[3] + " ||" + third[3]
            fifthrow = "  "+first[4] + "||" + second[4] + "||" + third[4]
            sixthrow = "  "+first[5] + " ||" + second[5] + " ||" + third[5]
           
            string +=  "\n" +secondrow + "\n"+thirdrow +"\n"+ fourthrow +"\n"+ fifthrow + "\n" + sixthrow 
            
            if i <= 1:
                string+= "\n=============||===========||============="
            else:
                string += ""
        string += "\n             ||           ||          "
            
        print(string)
    def canbigmove(self, y_coord, x_coord):
        print(f'y:{y_coord}, x:{x_coord}, sb:{self.stateboard}')
        if self.stateboard[y_coord][x_coord] == "":
            print("true")
            return True
        else:
            return False
        
        
    def check_solved(self):
        pass
    def main(self):
        first_square_x = int(input("first x"))
        first_square_y = int(input("first y"))
        curr_board = [first_square_x, first_square_y]
        n = 0
        while not self.solved:
            
            n += 1
            print(f"N:{n}")
            continuea = True

            x_coord = int(input("What is the x coordinate: ")) 
            y_coord = int(input("What is the y coordinate: ")) 


            print(f"n2 = {n%2}")
            if n%2 == 0:
                char = "X"
                print(f'Character X')
            if n%2 == 1:
                char = "O"
                print("Character O")
            print("hi")
            small_success = self.board[curr_board[1]][curr_board[0]].turn(char,y_coord,x_coord )
            print(small_success)
            
            if small_success:
                print(f'small success succesful, smallboard:{self.board[curr_board[1]][curr_board[0]].display()}')
                if self.canbigmove(x_coord, y_coord):
                    
                        curr_board = [y_coord, x_coord]
                else:
                        y_coord = int(input("Where you should have gone is taken, where is the new y coord")) - 1
                        x_coord = int(input("where you should have gone is taken, what x coordinate do you want to go to"))- 1
                        curr_board = [x_coord][y_coord]
                        
            for i in range(len(self.board)):
                for j in range(len(self.board)):
                    self.stateboard[i][j] == self.board[i][j].check_winner()
            
            self.display()
            
            
   
board = Bigboard()
board.main()
"""x = Smallboard()
x.turn("X", 1, 1)
print(x.display())"""