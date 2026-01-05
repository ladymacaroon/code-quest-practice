import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())

line = sys.stdin.readline().rstrip()

x = int(line.split(" ")[0])
y = int(line.split(" ")[1])


for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    systems = []
    working = []

    for i in range(x):
        systems.append(line)
    
        line = sys.stdin.readline().rstrip()

    for i in range(y):
        working.append(line)

        line = sys.stdin.readline().rstrip()

    for i in range(len(working)):
        if working[i] in systems:
            systems.remove(working[i])

    for i in range(len(systems)):
        print(systems[i])
