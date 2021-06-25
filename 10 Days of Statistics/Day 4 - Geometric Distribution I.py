# Enter your code here. Read input from STDIN. Print output to STDOUT
s, tot = map(int , input().split())
p = s/tot
q = 1-p
num_suc = int(input())
print(f"{round((q**(num_suc-1))*p, 3)}")