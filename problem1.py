import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())
vowels = ["a", "e", "i", "o", "u"]

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

    word = ""
    x = 0
    while x < len(line) - 1:
        current = line[x]
        next = line[x+1]

        if current in vowels:
            word += next
            x += 2
        else:
            x += 1

    print(word)
