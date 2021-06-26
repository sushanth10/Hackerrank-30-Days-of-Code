# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def cum_df(mean, sd, x):
    return 0.5 + 0.5 * math.erf((x-mean)/(sd*(2**0.5)))

x = int(input())
n = int(input())
mu = int(input())
sigma = int(input())

mu_new = n*mu
sigma_new = (n**0.5)*sigma
prob = cum_df(mu_new, sigma_new, x)
print(round(prob,4))
