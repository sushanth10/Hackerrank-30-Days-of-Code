# Enter your code here. Read input from STDIN. Print output to STDOUT
s, tot = map(int , input().split())
p = s/tot
q = 1-p
num_trial = int(input())
prob = 0
for i in range(num_trial):
    prob += (q**i)*p

print(f"{round(prob, 3)}")
