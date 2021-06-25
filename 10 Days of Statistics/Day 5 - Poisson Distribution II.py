# Enter your code here. Read input from STDIN. Print output to STDOUT

def fact(n):
    if n==1: return 1
    return n*fact(n-1)

    
m1,m2 = map(float, input().split())
# Expected value of X^2 = E[X^2] = Mean + (Mean^2)
# Expected costs are as given below
e1 = m1 + m1**2
e2 = m2 + m2**2
C1 = round(160 + 40*(e1), 3)
C2 = round(128 + 40*(e2), 3)
print(f"{C1}\n{C2}")

