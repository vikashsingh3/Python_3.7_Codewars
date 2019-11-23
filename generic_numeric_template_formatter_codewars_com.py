# Title: Generic numeric template formatter
# Source: codewars.com
# Site: https://www.codewars.com/kata/59901fb5917839fe41000029
# Code by: Vikash Singh
#
# Description:
# Your goal is to create a function to format a number given a template; if the number is not present, use the
# digits 1234567890 to fill in the spaces.
#
# A few rules:
#
# the template might consist of other numbers, special characters or the like: you need to replace only alphabetical
# characters (both lower- and uppercase);
# if the given or default string representing the number is shorter than the template, just repeat it to fill all the
# spaces.
# A few examples:
#
# numeric_formatter("xxx xxxxx xx","5465253289") == "546 52532 89"
# numeric_formatter("xxx xxxxx xx") == "123 45678 90"
# numeric_formatter("+555 aaaa bbbb", "18031978") == "+555 1803 1978"
# numeric_formatter("+555 aaaa bbbb") == "+555 1234 5678"
# numeric_formatter("xxxx yyyy zzzz") == "1234 5678 9012"


def numeric_formatter(template="", number="1234567890"):
    if template != "":
        new_number = ""
        j = 0
        for i in range(len(template)):
            if template[i].isalpha():
                new_number += number[j]
                j += 1
                if j == len(number):
                    j = 0
            else:
                new_number += template[i]
        return new_number
