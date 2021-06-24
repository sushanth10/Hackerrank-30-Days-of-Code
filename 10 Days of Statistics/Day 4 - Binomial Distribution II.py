# Enter your code here. Read input from STDIN. Print output to STDOUT
def fact(n):
    if n==0: return 1
    return n*fact(n-1)

def comb(n,x):
    return fact(n)/fact(x)/fact(n-x)

p, n = map(int, input().split())
p = p/100
q = 1-p
prob = [0,0]

for i in range(0,3):
    prob[0] += comb(n, i)*(p**i)*(q**(n-i))
    
for i in range(2,n+1):
    prob[1] += comb(n,i)*(p**i)*(q**(n-i))
    
prob = [round(num,3) for num in prob]
print(f"{prob[0]}\n{prob[1]}")