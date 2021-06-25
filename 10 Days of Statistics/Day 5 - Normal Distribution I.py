# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

mean, sd = map(float, input().split())
def cum_dis_fun(mean, std, x):
        return 0.5 + 0.5 * math.erf((x-mean)/(std* 2**0.5))

# probability that car is assembled in less than 19.5 hrs
prob1 = cum_dis_fun(mean, sd, 19.5)
prob2 = cum_dis_fun(mean, sd, 22)-cum_dis_fun(mean, sd, 20)
print(f"{prob1}\n{prob2}")
