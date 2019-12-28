# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

import timeit

start = timeit.default_timer()

def Collatz(num, len):
    if (num == 1):
        return len
    elif (num % 2 == 0):
        return Collatz(num/2, len+1)
    else:
        return Collatz(3*num + 1, len+1)

maxLen = [0, 0]

for i in range(1,1000000):
    currentLen = Collatz(i, 1)
    if (currentLen > maxLen[1]):
        maxLen[0] = i
        maxLen[1] = currentLen

print(maxLen)

end = timeit.default_timer()
print("Time: {0:.2f}".format(end - start))