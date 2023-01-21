import csv
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QMenu, QMenuBar, QPushButton, QVBoxLayout, QWidget, QGridLayout
class MainWindow(QWidget):
    
    def __init__(self, matrix, path=[]):
        super().__init__()
        self.path = path #all the coordinates of the longest path
        self.matrix = matrix #original matrix
        self.grid = None

        self.resize(200,250)
        self.setWindowTitle('Find Longest Path')  

        self.grid = QGridLayout()  
        self.makeMatrix(matrix, self.grid)

        button = QPushButton("Solve")
        button.clicked.connect(self.buttonClicked)

        layout = QVBoxLayout()
        layout.addLayout(self.grid, Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(button)
        layout.setContentsMargins(10,10,10,10)

        self.setLayout(layout)

        self.show()

    def setPath(self, path):
        self.path = path

    #function that produces the original matrix in the correct format
    def makeMatrix(self, matrix, grid):
        for i in range(len(matrix)):
            for j in range(len(matrix[1])):
                widget = QLabel(str(matrix[i][j]))
                widget.setStyleSheet('color: #002d7c;background-color:white;'
                                     'font-weight: bold;')
                widget.setMargin(10)
                widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
                

                grid.addWidget(widget, i , j)

        grid.setHorizontalSpacing(1)
        grid.setVerticalSpacing(1)

    #function that modifies the original matrix to highlight the path of the longest sequence in the correct format
    def highlight(self, matrix, grid, row, column):
        for i in range(len(self.path)):
            widget = QLabel(str(matrix[self.path[i][0]][self.path[i][1]]))
            widget.setStyleSheet('color: #002d7c;background-color:yellow;'
                                'font-weight: bold;')
            widget.setMargin(10)
            widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
            grid.replaceWidget(grid.itemAtPosition(self.path[i][0],self.path[i][1]).widget(), widget)


    def buttonClicked(self):
        self.highlight(self.matrix, self.grid, 1, 2)

#the following diagram shows all the possible paths of x
# a | b | c
# d | x | e
# f | g | h
class Matrix():
    def __init__(self, matrix):
        self.__matrix = matrix
        self.numRows = len(matrix)
        self.numColumns = len(matrix[1])

        #variables storing information about the longest path
        self.longestSequenceRow = -1
        self.longestSequenceColumn = -1
        self.longestSequenceLength = -1
        self.longestSequenceDirection = None

        self.__path = []#2d array storing all the coordinates of the longest path

    #function that returns the matrix of the csv file
    def getMatrix(self):
        return self.__matrix

    #function that returns the path
    def getPath(self):
        return self.__path

    #function that returns the path in one of the above directions
    #Condition: only 1 direction variable must be set to True
    def findPath(self, matrix, row, column, a=False, b=False, c=False, d=False, e=False, f=False, g=False, h=False):
        #counting the longest path in the a direction of x
        if a is True:
            if row-1 < 0 or column-1 < 0 or matrix[row][column] != matrix[row-1][column-1]:
                return 1
            else:
                return 1+ self.findPath(matrix, row-1, column-1, a=True)

        #counting the longest path in the b direction of x
        if b is True:
            if row-1 < 0 or matrix[row][column] != matrix[row-1][column]:
                return 1
            else:
                return 1+ self.findPath(matrix, row-1, column, b=True)
        
        #counting the longest path in the c direction of x
        if c is True:
            if row-1 < 0 or column+1 >= len(matrix[1]) or matrix[row][column] != matrix[row-1][column+1]:
                return 1
            else:
                return 1+ self.findPath(matrix, row-1, column+1, c=True)

        #counting the longest path in the d direction of x
        if d is True:
            if column-1 < 0 or matrix[row][column] != matrix[row][column-1]:
                return 1
            else:
                return 1+ self.findPath(matrix, row, column-1, d=True)
        #counting the longest path in the e direction of x
        if e is True:
            if column+1 >= len(matrix[1]) or matrix[row][column] != matrix[row][column+1]:
                return 1
            else:
                return 1+ self.findPath(matrix, row, column+1, e=True)
        #counting the longest path in the f direction of x
        if f is True:
            if row+1 >= len(matrix) or column-1 < 0 or matrix[row][column] != matrix[row+1][column-1]:
                return 1
            else:
                return 1+ self.findPath(matrix, row+1, column-1, f=True)
        #counting the longest path in the g direction of x
        if g is True:
            if row+1 >= len(matrix) or matrix[row][column] != matrix[row+1][column]:
                return 1
            else:
                return 1+ self.findPath(matrix, row+1, column, g=True,)
        #counting the longest path in the h direction of x
        if h is True:
            if row+1 >= len(matrix) or column+1 >= len(matrix[1]) or matrix[row][column] != matrix[row+1][column+1]:
                return 1
            else:
                return 1+ self.findPath(matrix, row+1, column+1, h=True)

    #function that finds the longest path of an entry in the matrix and returns the row, column, length, and direction
    def findLongestPath(self, matrix, row, column):
        aCount, bCount, cCount, dCount, eCount, fCount, gCount, hCount = 0,0,0,0,0,0,0,0
        if (row-1 >= 0 and column-1 >= 0 and matrix[row][column] == matrix[row-1][column-1]):
                aCount = self.findPath(matrix, row, column, a=True)

        if (row-1 >= 0 and matrix[row][column] == matrix[row-1][column]):
                bCount = self.findPath(matrix, row, column, b=True)
            
        if (row-1 >= 0 and column+1 < len(matrix[1]) and matrix[row][column] == matrix[row-1][column+1]):
                cCount = self.findPath(matrix, row, column, c=True)

        if (column-1 >= 0 and matrix[row][column] == matrix[row][column-1]):
                dCount = self.findPath(matrix, row, column, d=True)

        if (column+1 < len(matrix[1])) and matrix[row][column] == matrix[row][column+1]:
                eCount = self.findPath(matrix, row, column, e=True)

        if (row+1 < len(matrix) and column-1 >= 0 and matrix[row][column] == matrix[row+1][column-1]):
                fCount = self.findPath(matrix, row, column, f=True)

        if (row+1 < len(matrix[1]) and matrix[row][column] == matrix[row+1][column]):
                gCount = self.findPath(matrix, row, column, g=True)

        if (row+1 < len(matrix) and column+1 < len(matrix[1])) and matrix[row][column] == matrix[row+1][column+1]:
                hCount = self.findPath(matrix, row, column, h=True)

        dic = {aCount:"a", bCount:"b", cCount:"c", dCount:"d", eCount:"e", fCount:"f", gCount:"g", hCount:"h"}
        return row, column, max(dic), dic.get(max(dic))
        
    #function that finds the the row, column, length, and direction of the longest path in the whole matrix 
    def solveMatrix(self):
        for i in range(self.numRows):
            for j in range(self.numColumns):
                currentRow, currentColumn, currentLength, currentDirection = self.findLongestPath(self.getMatrix(), i, j)
                if currentLength > self.longestSequenceLength:
                    self.longestSequenceRow = currentRow
                    self.longestSequenceColumn = currentColumn
                    self.longestSequenceLength = currentLength
                    self.longestSequenceDirection = currentDirection
        self.findLongestPathCords(self.getMatrix(), self.longestSequenceRow, self.longestSequenceColumn, self.longestSequenceDirection)

    #function that finds and stores all the coordinates of the longest path
    def findLongestPathCords(self, matrix, row, column, direction):
        value = matrix[row][column]#original value of the entry
        while(row >= 0) and (row < len(matrix)) and column >= 0 and (column < len(matrix[1])) and value == matrix[row][column]:
            self.getPath().append([row,column])
            if (direction == "a"):
                row -=1
                column -= 1
            if (direction == "b"):
                row -=1
            if (direction == "c"):
                row -=1
                column += 1
            if (direction == "d"):
                column -= 1
            if (direction == "e"):
                column += 1
            if (direction == "f"):
                row += 1
                column -= 1
            if (direction == "g"):
                row += 1
            if (direction == "h"):
                row += 1
                column += 1

def main():
    matrix = Matrix(list(csv.reader(open(sys.argv[1], 'r'))))
    matrix.solveMatrix()
    app = QApplication(sys.argv)
    window = MainWindow(matrix.getMatrix())
    window.setPath(matrix.getPath())
    window.show()
    app.exec()

main()
