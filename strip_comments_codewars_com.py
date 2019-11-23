# Title: Strip Comments
# Source: codewars.com
# Site: https://www.codewars.com/kata/51c8e37cee245da6b40000bd
# Code by: Vikash Singh
#
# Description:
# Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
# Any whitespace at the end of the line should also be stripped out.
#
# Example:
#
# Given an input string of:
#
# apples, pears # and bananas
# grapes
# bananas !apples
# The output expected would be:
#
# apples, pears
# grapes
# bananas
# The code would be called like so:
#
# result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# # result should == "apples, pears\ngrapes\nbananas"


def solution(strings, markers):
    for i in markers:
        while i in strings:
            strings = strings[:strings.find(i)].strip(" ") + \
                      strings[len(strings)
                              if strings.find("\n", strings.find(i)) == -1 else strings.find("\n", strings.find(i)):]
    return strings.rstrip(" ")
