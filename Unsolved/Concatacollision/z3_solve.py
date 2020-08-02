#!/usr/bin/env python3
# export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:~/Downloads/z3-4.8.0.99339798ee98-x64-osx-10.11.6/bin
# export PYTHONPATH=~/Downloads/z3-4.8.0.99339798ee98-x64-osx-10.11.6/bin/python
from z3 import *

# create integer variables for flag
x0 = Int("red")
x1 = Int("black")

concat_exp = Int("exp")
concat_numb = Int("numb")
K = Int("K")
L = Int("L")

# add solver constraints
s = Solver()
s.add(x0 == 222950984970414803209146829527994389589)
s.add(x1 == 199111234895517335053481970219062834774)


# int(str(int(str(x1) + s) % x0) + s) % x1 == 1
# int(str(              A1 % x0) + s) % x1 == 1
# int(                     A2    + s) % x1 == 1
#                                 A3  % x1 == 1

A1 = (x1 * (10**concat_exp)) + concat_numb
A2 = A1 % x0
A3 = (A2 * (10**concat_exp)) + concat_numb
Final = A3 % x1

#s.add(Final == 1)
#s.add(10**concat_exp >= concat_numb)

s.add(1 + L*x1 == A3)
s.add(A2 + K*x0 == A1)
s.add(Final == 1)




# check if there is a solution
if s.check() != sat:
    print("No solution")
    quit()

m = s.model()
print(m)

# convert to int array
for name in m:
    value = m[name]
    print(f"{name} == {value}")

'''

    index = int(str(name).split('__')[1])

    flag[index] = int(str(value))
    ch = chr(flag[index])
    print(f"{name} at {hex(index)} = {value} {ch}")

# convert to char array or string
flag = ''.join(list(map(lambda x: chr(x) if x else '\x00', flag)))
print('flag =', flag)
print('flag (hex) =', flag.encode().hex())
'''
