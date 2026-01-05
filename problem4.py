import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    letters = []
    special = []

    for x in range(len(line)):
        letters.append(line[x])
        
    for x in range(len(letters)):
        try:
            int(letters[x]) or str(letters[x])
        except:
            special.append(letters[x])

    for x in range(len(special)):
        letters.remove(special[x])

    print(letters)
