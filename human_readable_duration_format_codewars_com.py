# Title: Human readable duration format
# Source: codewars.com
# Site: https://www.codewars.com/kata/52742f58faf5485cae000b9a
# Code by: Vikash Singh
# 
# Description:
# Your task in order to complete this Kata is to write a function which formats a duration, given as a number of
# seconds, in a human-friendly way.
#
# The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise,
# the duration is expressed as a combination of years, days, hours, minutes and seconds.
#
# It is much easier to understand with an example:
#
# format_duration(62)    # returns "1 minute and 2 seconds"
# format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
# For the purpose of this Kata, a year is 365 days and a day is 24 hours.
#
# Note that spaces are important.
#
# Detailed rules
# The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer
# and one of the valid units of time, separated by a space. The unit of time is used in plural
# if the integer is greater than 1.
#
# The components are separated by a comma and a space (", "). Except the last component, which is separated
# by " and ", just like it would be written in English.
#
# A more significant units of time will occur before than a least significant one. Therefore, 1 second
# and 1 year is not correct, but 1 year and 1 second is.
#
# Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.
#
# A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid,
# but it should be just 1 minute.
#
# A unit of time must be used "as much as possible". It means that the function should not return 61 seconds,
# but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than
# any valid more significant unit of time.

def format_duration(seconds):
    msg = ""
    if seconds >= 31536000:
        msg = str(int(seconds/31536000)) + " years" if int(seconds/31536000) > 1 else "1 year"
    remaining = seconds % 31536000
    if remaining >= 86400:
        msg = msg + ", " if len(msg) > 0 else msg
        msg = msg + str(int(remaining/86400)) + " days" if int(remaining/86400) > 1 else msg + "1 day"
    remaining = remaining % 86400
    if remaining >= 3600:
        msg = msg + ", " if len(msg) > 0 else msg
        msg = msg + str(int(remaining / 3600)) + " hours" if int(remaining / 3600) > 1 else msg + "1 hour"
    remaining = remaining % 3600
    if remaining >= 60:
        msg = msg + ", " if len(msg) > 0 else msg
        msg = msg + str(int(remaining/60)) + " minutes" if int(remaining/60) > 1 else msg + "1 minute"
    if remaining % 60 > 0:
        msg = msg + ", " if len(msg) > 0 else msg
        msg = msg + str(int(remaining % 60)) + " seconds" if remaining % 60 > 1 else msg + "1 second"
    elif len(msg) == 0:
        msg = "now"
    return " and".join(msg.rsplit(",", 1))