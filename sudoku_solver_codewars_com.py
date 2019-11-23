# Title: Sudoku Solver
# Source: codewars.com
# Site: https://www.codewars.com/kata/5296bc77afba8baa690002d7
# Code by: Vikash Singh
#
# Description: Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument
# consisting of the 2D puzzle array, with the value 0 representing an unknown square.
#
# The Sudokus tested against your function will be "easy" (i.e. determinable; there will be no need to
# assume and test possibilities on unknowns) and can be solved with a brute-force approach.
#
# For Sudoku rules, see the Wikipedia article.
#
# But as part of this programme we will not use brute-force.


board = ""


def sudoku(sudoku_board):
    global board
    board = sudoku_board
    loop_number = 1

    while not verify_finished():
        board = sudoku_board
        solve_horizontally()
        solve_vertically()
        check_horizontally()
        possibility_in_section()
        loop_number += 1
    return board


def check_horizontally():
    global board
    for section in range(9):
        start_row = int(section/3) * 3
        start_col = (section % 3) * 3
        values_available = []
        for row in range(start_row, start_row + 3):
            for col in range(start_col, start_col + 3):
                values_available.append(board[row][col])
        for row in range(start_row, start_row + 3):
            for col in range(start_col, start_col + 3):
                if board[row][col] == 0:
                    possible_value = 0
                    possible_number = 0
                    for numbers in range(1, 10):
                        if board[row].count(numbers) == 0 \
                                and [x[col] for x in board].count(numbers) == 0 \
                                and numbers not in values_available:
                            possible_value += 1
                            possible_number = numbers
                    if possible_value == 1:
                        board[row][col] = possible_number


def possibility_in_section():
    for section in range(9):
        start_row = int(section/3) * 3
        start_col = (section % 3) * 3
        values_available = []
        for row in range(start_row, start_row + 3):
            for col in range(start_col, start_col + 3):
                values_available.append(board[row][col])
        for numbers in range(1, 10):
            possible_values = 0
            possible_row = 0
            possible_col = 0
            for row in range(start_row, start_row + 3):
                for col in range(start_col, start_col + 3):
                    if board[row][col] == 0:
                        if board[row].count(numbers) == 0 \
                                and [x[col] for x in board].count(numbers) == 0 \
                                and numbers not in values_available:
                            possible_values += 1
                            possible_row = row
                            possible_col = col
            if possible_values == 1:
                board[possible_row][possible_col] = numbers


def verify_finished():  # board[i][j]
    global board
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

    if valid_flag:
        return True
    else:
        return False


def possible_data(number, row_col, direction):
    global board
    irow = row_col
    subsection_1 = 99
    subsection_2 = 99
    if direction == "horizontal":
        for icol in range(0, len(board)):
            if number == board[irow][icol] or number == board[irow + 1][icol] or number == board[irow + 2][icol]:
                if subsection_1 == 99:
                    subsection_1 = 3 * int(irow / 3) + int(icol / 3)
                elif subsection_2 == 99:
                    subsection_2 = 3 * int(irow / 3) + int(icol / 3)
    else:
        for row in range(0, len(board)):
            if number == board[row][row_col] or number == board[row][row_col+1] or number == board[row][row_col+2]:
                if subsection_1 == 99:
                    subsection_1 = 3 * int(row / 3) + int(row_col / 3)
                elif subsection_2 == 99:
                    subsection_2 = 3 * int(row / 3) + int(row_col / 3)

    if direction == "horizontal":
        if subsection_1 + subsection_2 < 4:
            missing_sec = 3 - subsection_1 - subsection_2
        elif subsection_1 + subsection_2 < 13:
            missing_sec = 12 - subsection_1 - subsection_2
        else:
            missing_sec = 21 - subsection_1 - subsection_2
    else:
        if subsection_1 % 3 == 0:
            missing_sec = 9 - subsection_1 - subsection_2
        elif subsection_1 % 3 == 1:
            missing_sec = 12 - subsection_1 - subsection_2
        else:
            missing_sec = 15 - subsection_1 - subsection_2

    missing_col = (missing_sec % 3) * 3
    missing_row = int(missing_sec / 3) * 3
    if direction == "horizontal":
        # check in missing row
        for section_row in range(3):
            if board[3*int(subsection_1 / 3) + section_row].count(number) == 0:
                tp = board[3*int(subsection_1 / 3) + section_row][missing_col:missing_col+3]
                if len([i for i in tp if i > 0]) == 2:
                    for col in range(3):
                        if tp[col] == 0:
                            board[3*int(subsection_1 / 3) + section_row][missing_col+col] = number
                else:   # update by checking vertical columns:
                    possible_value = 0
                    possible_col_number = 0
                    for col in range(3):
                        if tp[col] == 0:
                            if [row[missing_col + col] for row in board].count(number) == 0:
                                possible_value += 1
                                possible_col_number = col
                    if possible_value == 1:
                        board[3 * int(subsection_1 / 3) + section_row][missing_col + possible_col_number] = number
    else:
        for section_col in range(3):
            if [x[row_col+section_col] for x in board].count(number) == 0:
                tp = [x[row_col+section_col] for x in board[missing_row:missing_row+3]]
                if len([i for i in tp if i > 0]) == 2:
                    for counter_row in range(3):
                        if board[missing_row+counter_row][row_col+section_col] == 0:
                            board[missing_row + counter_row][row_col + section_col] = number
                else:
                    possible_value = 0
                    possible_row_number = 0
                    for counter_row in range(3):
                        if board[missing_row+counter_row][row_col+section_col] == 0:
                            if board[missing_row + counter_row].count(number) == 0:
                                possible_value += 1
                                possible_row_number = missing_row + counter_row
                    if possible_value == 1:
                        board[possible_row_number][row_col + section_col] = number


def solve_vertically():
    global board
    for num in range(1, 1 + len(board)):
        for col in range(0, len(board), 3):
            if [row[col] for row in board].count(num) + \
                    [row[col+1] for row in board].count(num) + \
                    [row[col+2] for row in board].count(num) == 2:
                possible_data(num, col, "vertical")


def solve_horizontally():
    global board
    for num in range(1, 1 + len(board)):
        for irow in range(0, len(board), 3):
            if board[irow].count(num) + board[irow+1].count(num) + board[irow+2].count(num) == 2:
                possible_data(num, irow, "horizontal")
