"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)
sum_lookup_table={}
diff_lookup_table={}


def f(x):
    return x * 4 + 6

def sum_f(x,y):
    return f(x) + f(y)

def diff_f(x,y):
    return f(x) - f(y)

# saving in lookup_table all results of sum_f and diff_f functions
for i in range(len(q)):
    for j in range(len(q)):
        if f"f({q[i]}) + f({q[j]})" not in sum_lookup_table:
            sum_lookup_table[f"f({q[i]}) + f({q[j]})"] = sum_f(q[i],q[j])
        if f"f({q[i]}) - f({q[j]})" not in diff_lookup_table:
            diff_lookup_table[f"f({q[i]}) - f({q[j]})"] = diff_f(q[i],q[j])

# printing results in expected format
for sum_el in sum_lookup_table.items():
    for diff_el in diff_lookup_table.items():
        if sum_el[1] == diff_el[1]:
            print(f"{sum_el[0]} = {diff_el[0]}    {f(int(sum_el[0][2:3]))} + {f(int(sum_el[0][9:10]))}  = {f(int(diff_el[0][2:4]))} - {f(int(diff_el[0][10:11]))}  ")
            
        