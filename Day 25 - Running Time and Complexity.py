# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

def isPrime(number) -> bool:
    i=2
    while(i*i<=number):
        if(number%i==0):
            return False
        i+=1
    return True

for _ in range(n):
    num = int(input()) 
    if num==1:
        print("Not prime")
    else:
        if isPrime(num):
            print("Prime")
        else:
            print("Not prime")
    
    
