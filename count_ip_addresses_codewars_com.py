# Title: Count IP Addresses
# Source: codewars.com
# Site: https://www.codewars.com/kata/526989a41034285187000de4
# Code by: Vikash Singh
#
# Description:
# Implement a function that receives two IPv4 addresses, and returns the number of addresses between them
# (including the first one, excluding the last one).
#
# All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater
# than the first one.
#
# Examples
# ips_between("10.0.0.0", "10.0.0.50")  ==   50
# ips_between("10.0.0.0", "10.0.1.0")   ==  256
# ips_between("20.0.0.10", "20.0.1.0")  ==  246


def ips_between(start, end):
    a = start.split(".")
    b = end.split(".")
    ip = (int(b[0])-int(a[0])) * 256 ** 3 + (int(b[1])-int(a[1]))*256**2 \
         + (int(b[2])-int(a[2]))*256 + (int(b[3])-int(a[3]))
    return ip
