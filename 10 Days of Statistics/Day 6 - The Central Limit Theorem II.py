# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

x = float(input())
n = float(input())
mu = float(input())
sigma = float(input())

def cdf(x, mean, sd):
    return 0.5*(1+math.erf((x-mean)/(sd*(2**0.5))))

mu_new = n*mu
sigma_new = sigma*(n**0.5)
prob = cdf(x, mu_new, sigma_new)
print(round(prob,4))
