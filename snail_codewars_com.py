# Title: Snail
# Source: codewars.com
# Site: https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
# Code by: Vikash Singh
#
# Description:
# Snail Sort
# Given an n x n array, return the array elements arranged from outermost elements to the middle element,
# traveling clockwise.
#
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:
#
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
#
# NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array
# in a clockwise snailshell pattern.
#
# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].


def snail(snail_map):
    loop = 0
    final_list = []
    while len(final_list) < len(snail_map) **2 and len(snail_map[0]) > 0:
        for go_right in range(loop, len(snail_map) - loop):
            final_list.append(snail_map[loop][go_right])
        for go_down in range(loop+1, len(snail_map) - loop):
            final_list.append(snail_map[go_down][len(snail_map) - 1 - loop])
        for go_left in range(len(snail_map) - loop - 2, loop - 1, -1):
            final_list.append(snail_map[len(snail_map) - 1 - loop][go_left])
        for go_up in range(len(snail_map) - loop - 2, loop, -1):
            final_list.append(snail_map[go_up][loop])
        loop += 1
    return final_list

