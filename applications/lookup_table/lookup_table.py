import math
import random
# Your code here

lookup_table = {}
def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

# def build_lookup_table():
#     for i in range(1,1000):
#         loo

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    v = math.pow(x,y)
    if v not in lookup_table:
        lookup_table[v] = math.factorial(v)
        lookup_table[v] //= (x+y)
        lookup_table[v] %= 982451653
    return lookup_table[v]



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
