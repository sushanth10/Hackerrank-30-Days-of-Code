# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def cum_dis_fun(mean, std, x):
    return 0.5*(1+ math.erf((x-mean)/(std*(2**0.5))))

mean,sd = map(float, input().split())
m1 = int(input())
m2 = int(input())
#percentage of students => (probability for grade>80)*100
prob1 = (1 - cum_dis_fun(mean, sd, m1))*100
#percentage of students>=60 => (1 - probability for grade<60)*100
prob2 = (1 - cum_dis_fun(mean, sd, m2))*100
#percentage of students<60 => (probability for grade<60)*100
prob3 = cum_dis_fun(mean, sd, m2)*100

print(f"{round(prob1,2)}\n{round(prob2,2)}\n{round(prob3,2)}")