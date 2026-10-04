# project0b.py
#
# ICS H32 Fall 2026
# Project 0B: Square One
#
# Implement your solution here.

n = input()
n = int(n)

print("+-+")

for i in range(n - 1):
    print(i * "  " + "| |")
    print(i * "  " + "+-+-+")

print((n - 1) * "  " + "| |")
print((n - 1) * "  " + "+-+")