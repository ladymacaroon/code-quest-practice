import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
   line = sys.stdin.readline().rstrip()
   
   volume = int(line.split(" ")[0])
   enter = int(line.split(" ")[1])
   exit = int(line.split(" ")[2])

   waste = (volume / (enter - exit)) * exit   
   
   print(int(round(waste, 0)))
