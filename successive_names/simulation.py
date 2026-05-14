from random import randint

SIMULATIONS=100_000_000

N=26
l=4

def is_successive(dp):
    rtn=True
    for i in range(l-1):
        if dp[i+1]-dp[i]!=1: rtn = False 
    return rtn

data=[sorted([randint(1,N) for j in range(l)]) for i in range(SIMULATIONS)]

print(sum([is_successive(dp) for dp in data])/SIMULATIONS)
