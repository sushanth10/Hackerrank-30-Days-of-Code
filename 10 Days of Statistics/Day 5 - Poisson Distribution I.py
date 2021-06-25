# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def fact(n):
    if n==1: return 1
    return n*fact(n-1)

m = float(input())
x = int(input())
prob = (m**x)*(math.exp(-m))/fact(x)
print(round(prob,3))