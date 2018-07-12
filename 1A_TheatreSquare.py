import math

long, wide, flagstone = map (float, raw_input().split(" "))

def square(n, m, a):
    q = math.ceil(n / a)
    q1 = math.ceil(m / a)
    return q*q1

print int(square(long, wide, flagstone))
