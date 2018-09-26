# Sum of all the natural numbers below limit that are multiples of 3 or 5

limit = 1000

sumn = 0
n = 0
while n < limit - 3:
    n += 3
    sumn += n
n = 0
while n < limit - 5:
    n += 5
    if n % 3 != 0:
        sumn += n
print "Sum of all the natural numbers below", limit, "that are multiples \
of 3 or 5:", sumn
