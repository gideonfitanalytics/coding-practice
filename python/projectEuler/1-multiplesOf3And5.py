# Sum of all the natural numbers below limit that are multiples of 3 or 5

limit = 1000

n = 1
count = 0
while n <= limit - 1:
    if n % 3 == 0 or n % 5 == 0:
        count += 1
    n += 1
print "Sum of all the natural numbers below", limit, "that are multiples \
of 3 or 5:", count
