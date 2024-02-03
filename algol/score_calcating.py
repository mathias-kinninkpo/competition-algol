import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
l = 0
isfail =  False
for i in range(n):
    score = int(input())
    if score < 50:
        isfail = True
        break
    l = l + score * 0.0075

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("{:.2f}".format(math.floor(l * 100) / 100) if not isfail else "Student failed the curriculum")

