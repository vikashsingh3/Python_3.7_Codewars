# Title: RoboScript #2 - Implement the RS1 Specification
# Source: codewars.com
# Site: https://www.codewars.com/kata/5870fa11aa0428da750000da
# Code by: Vikash Singh
#
# Description:
# RoboScript #2 - Implement the RS1 Specification
# Disclaimer
# The story presented in this Kata Series is purely fictional; any resemblance to actual programming languages,
# products, organisations or people should be treated as purely coincidental.
#
# About this Kata Series
# This Kata Series is based on a fictional story about a computer scientist and engineer who owns a firm that
# sells a toy robot called MyRobot which can interpret its own (esoteric) programming language called RoboScript.
# Naturally, this Kata Series deals with the software side of things (I'm afraid Codewars cannot test your ability
# to build a physical robot!).
#
# Story
# Now that you've built your own code editor for RoboScript with appropriate syntax highlighting to make it look
# like serious code, it's time to properly implement RoboScript so that our MyRobots can execute any RoboScript
# provided and move according to the will of our customers. Since this is the first version of RoboScript, let's
# call our specification RS1 (like how the newest specification for JavaScript is called ES6 :p)
#
# Task
# Write an interpreter for RS1 called execute() which accepts 1 required argument code, the RS1 program to be
# executed. The interpreter should return a string representation of the smallest 2D grid containing the full
# path that the MyRobot has walked on (explained in more detail later).
#
# Initially, the robot starts at the middle of a 1x1 grid. Everywhere the robot walks it will leave a path "*".
# If the robot has not been at a particular point on the grid then that point will be represented by a whitespace
# character " ". So if the RS1 program passed in to execute() is empty then:
#
# execute(""); // => "*"
# The robot understand 3 major commands:
#
# F - Move forward by 1 step in the direction that it is currently pointing. Initially, the robot faces to the right.
# L - Turn "left" (i.e. rotate 90 degrees anticlockwise)
# R - Turn "right" (i.e. rotate 90 degrees clockwise)
# As the robot moves forward, if there is not enough space in the grid, the grid should expand accordingly. So:
#
# execute("FFFFF"); // => "******"
# As you will notice, 5 F commands in a row should cause your interpreter to return a string containing 6 "*"s in a row.
# This is because initially, your robot is standing at the middle of the 1x1 grid facing right. It leaves a mark on
# the spot it is standing on, hence the first "*". Upon the first command, the robot moves 1 unit to the right.
# Since the 1x1 grid is not large enough, your interpreter should expand the grid 1 unit to the right.
# The robot then leaves a mark on its newly arrived destination hence the second "*". As this process is repeated
# 4 more times, the grid expands 4 more units to the right and the robot keeps leaving a mark on its newly arrived
# destination so by the time the entire program is executed, 6 "squares" have been marked "*" from left to right.
#
# Each row in your grid must be separated from the next by a CRLF (\r\n). Let's look at another example:
#
# execute("FFFFFLFFFFFLFFFFFLFFFFFL"); // => "******\r\n*    *\r\n*    *\r\n*    *\r\n*    *\r\n******"
#
# /*
#   The grid looks like this:
#   ******
#   *    *
#   *    *
#   *    *
#   *    *
#   ******
# */
# The robot moves 5 units to the right, then turns left, then moves 5 units upwards, then turns left again, then
# moves 5 units to the left, then turns left again and moves 5 units downwards, returning to the starting point before
# turning left one final time. Note that the marks do not disappear no matter how many times the robot steps on them,
# e.g. the starting point is still marked "*" despite the robot having stepped on it twice (initially and on the last
# step).
#
# Another example:
#
# execute("LFFFFFRFFFRFFFRFFFFFFF"); // => "    ****\r\n    *  *\r\n    *  *\r\n********\r\n    *   \r\n    *   "
#
# /*
#   The grid looks like this:
#       ****
#       *  *
#       *  *
#   ********
#       *
#       *
# */
# Initially the robot turns left to face upwards, then moves upwards 5 squares, then turns right and moves 3 squares,
# then turns right again (to face downwards) and move 3 squares, then finally turns right again and moves 7 squares.
#
# Since you've realised that it is probably quite inefficient to repeat certain commands over and over again by
# repeating the characters (especially the F command - what if you want to move forwards 20 steps?), you decide to
# allow a shorthand notation in the RS1 specification which allows your customers to postfix a non-negative integer
# onto a command to specify how many times an instruction is to be executed:
#
# Fn - Execute the F command n times (NOTE: n may be more than 1 digit long!)
# Ln - Execute L n times
# Rn - Execute R n times
# So the example directly above can also be written as:
#
# LF5RF3RF3RF7
# These 5 example test cases have been included for you :)


from _datetime import datetime
import numpy as np
coordinates = []


def get_position(steps, coordinates_value=False, x_dist_tot=0, y_dist_tot=0):
    current_direction = 0
    steps_count = 0
    directions = [["east", 0], ["south", 0], ["west", 0], ["north", 0]]
    for i in steps:
        if i == "L":
            steps_count = 0
            current_direction = (current_direction - 1) % 4
        elif i == "R":
            steps_count = 0
            current_direction = (current_direction + 1) % 4
        else:
            steps_count += 1
            if directions[current_direction][1] < steps_count:
                directions[current_direction][1] = steps_count
            if directions[current_direction][0] == "east":
                x_dist_tot += 1
            elif directions[current_direction][0] == "west":
                x_dist_tot -= 1
            elif directions[current_direction][0] == "north":
                y_dist_tot -= 1
            elif directions[current_direction][0] == "south":
                y_dist_tot += 1

        if coordinates_value:
            coordinates[y_dist_tot][x_dist_tot] = "*"
    return directions


def robot_script(steps):
    global coordinates
    directions = get_position(steps)
    x_dist_tot = directions[0][1] + directions[2][1] + 1000
    y_dist_tot = directions[1][1] + directions[3][1] + 1000
    coordinates = np.zeros((x_dist_tot, y_dist_tot), dtype=object)
    coordinates[:] = " "
    x = 500
    y = 500
    coordinates[y][x] = "*"

    get_position(steps, True, x, y)
    # Remove Empty column
    data_column_row = []
    for counter in range(len(coordinates[0])):
        all_row_col_data = "".join(coordinates[:, counter])
        all_row_col_data = all_row_col_data.strip()
        if all_row_col_data != "":
            data_column_row.append(counter)
    coordinates = coordinates[:, data_column_row]
    # Remove Empty row
    data_column_row = []
    for counter in range(len(coordinates)):
        all_row_col_data = "".join(coordinates[counter, :])
        all_row_col_data = all_row_col_data.strip()
        if all_row_col_data != "":
            data_column_row.append(counter)
    coordinates = coordinates[data_column_row, :]

    return_value = ""
    for i in range(len(coordinates)):
        return_value += "".join(coordinates[i]) + "\r\n"
    return return_value[:-2]


def execute(step_code):
    new_code = last_value = ""
    for i in range(0, len(step_code)):
        if step_code[i].isnumeric() and not step_code[i - 1].isnumeric():
            num = ""
            while i < len(step_code) and step_code[i].isnumeric():
                num += step_code[i]
                i += 1

            for j in range(int(num)-1):
                new_code += last_value
        elif not step_code[i].isnumeric():
            last_value = step_code[i]
            new_code += step_code[i]
    return robot_script(new_code)
