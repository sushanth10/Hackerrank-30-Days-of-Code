# Enter your code here. Read input from STDIN. Print output to STDOUT
def fact(n):
    if n==0: return 1
    return n*fact(n-1)

def comb(n,x):
    return fact(n)/fact(x)/fact(n-x)


boyRat, girlRat = map(float, input().split())
p = boyRat/(boyRat+girlRat)
q = 1-p
prob = 0
for i in range(3,7):
    prob += comb(6,i)*(p**i)*(q**(6-i))
        
print(round(prob,3))