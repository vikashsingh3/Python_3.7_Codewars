# Title: Find The Parity Outlier
# Source: codewars.com
# Site: https://www.codewars.com/kata/5526fc09a1bbd946250002dc
# Code by: Vikash Singh
#
# Description:
# You are given an array (which will have a length of at least 3, but could be very large) containing integers.
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a
# single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
#
# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)
#
# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)


def find_outlier(integers):
    even_count = odd_count = 0
    for i in range(3):
        if integers[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    if even_count < odd_count:
        # outlier = "odd"
        for num in integers:
            if num % 2 == 0:
                return num
    else:
        # outlier = "even"
        for num in integers:
            if num % 2 == 1:
                return num
