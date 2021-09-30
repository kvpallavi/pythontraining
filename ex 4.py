a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for a1 in a:
    for b1 in b:
        if a1 == b1:
            c.append(a1)
print c

set_a = set(a)
set_b = set(b)

set_c = list(set_a.intersection(set_b))
print set_c

import random

a_rand = random.sample(range(1, 100), 10)
print a_rand
b_rand = random.sample(range(1, 100), 10)
print b_rand

a_rand_set = set(a_rand)
b_rand_set = set(b_rand)

c_rand_set = list(a_rand_set.intersection(b_rand_set))
print c_rand_set