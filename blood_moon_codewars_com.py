# Title: Blood Moon
# Source: codewars.com
# Site: https://www.codewars.com/kata/5cba04533e6dce000eaf6126
# Code by: Vikash Singh
#
# Description:
# Alan is going to watch the Blood Moon (lunar eclipse) tonight for the first time in his life.
# But his mother, who is a history teacher, thinks the Blood Moon comes with an evil intent. The ancient Inca people
# interpreted the deep red coloring as a jaguar attacking and eating the moon. But who believes in Inca myths these
# days? So, Alan decides to prove to her mom that there is no jaguar. How? Well, only little Alan knows that.
# For now, he needs a small help from you. Help him solve the following calculations so that he gets enough time to
# prove it before the eclipse starts.
#
# Screenshot-3
# Three semicircles are drawn on AB, AD, and AF. Here CD is perpendicular to AB and EF is perpendicular to AD.
#
# Task
# Given the radius of the semicircle ADBCA, find out the area of the lune AGFHA (the shaded area).


import math


def blood_moon(r): 
    length_ae = r * math.sqrt(2)/2
    length_af = length_ae * math.sqrt(2) * 0.5
    area = 0.5 * math.pi * length_af ** 2 - ((math.pi - 2) * 0.25 * length_ae ** 2 )
    return round(area * 4)/4
