# adds up only the even fibonacci numbers below the given limit

limit = 4000000

fib = 1
log = 1
total = 0
while fib + log <= limit:
    oldLog = log
    log = fib
    fib = fib + oldLog
    if (total + fib) % 2 == 0:
        total = total + fib
print "Total:", total
