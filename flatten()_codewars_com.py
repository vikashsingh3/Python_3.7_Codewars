# Title: flatten()
# Source: codewars.com
# Site: https://www.codewars.com/kata/513fa1d75e4297ba38000003
# Code by: Vikash Singh
#
# Description:
# For this exercise you will create a global flatten method. The method takes in any number of arguments and
# flattens them into a single array. If any of the arguments passed in are an array then the individual objects
# within the array will be flattened so that they exist at the same level as the other arguments. Any nested arrays,
# no matter how deep, should be flattened into the single array result.
#
# The following are examples of how this function would be used and what the expected results would be:
#
# flatten(1, [2, 3], 4, 5, [6, [7]]) # returns [1, 2, 3, 4, 5, 6, 7]
# flatten('a', ['b', 2], 3, None, [[4], ['c']]) # returns ['a', 'b', 2, 3, None, 4, 'c']


list_v = []


def flatten(*test):
    global list_v
    list_v = []
    for i in test:
        if str(type(i)) == "<class 'list'>":
            sep_list(i)
        else:
            list_v.append(i)
    return list_v
    

def sep_list(abc):
    global list_v
    for j in abc:
        if str(type(j)) == "<class 'list'>":
            sep_list(j)
        else:
            list_v.append(j)
    return list_v
