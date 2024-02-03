import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

t = int(input())
todo = list()
for i in range(t):
    todo.append(input())
n = int(input())
do = list()
for i in range(n):
    do.append(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
for i in sorted(list(set(todo) - set(do))):
    print(i)

