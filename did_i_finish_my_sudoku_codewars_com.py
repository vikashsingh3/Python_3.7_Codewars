# Title: Did I Finish my Sudoku?
# Source: codewars.com
# Site: https://www.codewars.com/kata/53db96041f1a7d32dc0004d2
# Code by: Vikash Singh
#
# Description:
# Write a function done_or_not/DoneOrNot passing a board (list[list_lines]) as parameter. If the board is valid
# return 'Finished!', otherwise return 'Try again!'
#
# Sudoku rules:
#
# Complete the Sudoku puzzle so that each and every row, column, and region contains the numbers one through
# nine only once.
#
# There are 9 rows in a traditional Sudoku puzzle. Every row must contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9.
# There may not be any duplicate numbers in any row. In other words, there can not be any rows that are identical.
#
# In the illustration the numbers 5, 3, 1, and 2 are the "givens". They can not be changed. The remaining numbers in
# black are the numbers that you fill in to complete the row.
#
# There are 9 columns in a traditional Sudoku puzzle. Like the Sudoku rule for rows, every column must also contain
# the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. Again, there may not be any duplicate numbers in any column.
# Each column will be unique as a result.
#
# In the illustration the numbers 7, 2, and 6 are the "givens". They can not be changed. You fill in the remaining
# numbers as shown in black to complete the column.
#
# A region is a 3x3 box like the one shown to the left. There are 9 regions in a traditional Sudoku puzzle.
#
# Like the Sudoku requirements for rows and columns, every region must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8,
# and 9. Duplicate numbers are not permitted in any region. Each region will differ from the other regions.
#
# In the illustration the numbers 1, 2, and 8 are the "givens". They can not be changed. Fill in the remaining numbers
# as shown in black to complete the region.
#
# For those who don't know the game, here are some information about rules and how to play Sudoku:
# http://en.wikipedia.org/wiki/Sudoku and http://www.sudokuessentials.com/


def done_or_not(board):  # board[i][j]
    # Check for rows values
    valid_flag = True
    for row in range(9):
        total = 0
        for col in range(9):
            total += board[row][col]
        if total != 45:
            valid_flag = False

    # Check for column values
    for col in range(9):
        total = 0
        for row in range(9):
            total += board[row][col]
        if total != 45:
            valid_flag = False

    # Check for regions
    for row in range(0, 8, 3):
        for col in range(0, 8, 3):
            total = 0
            for region_row in range(row, row + 3):
                for region_col in range(col, col + 3):
                    total += board[region_row][region_col]
            if total != 45:
                valid_flag = False
                print(row, col, region_row, region_col, total)

    if valid_flag:
        return 'Finished!'
    else:
        return 'Try again!'
