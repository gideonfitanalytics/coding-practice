testcomponent = int(raw_input("Choose An Option\n\n\
1) check for a given number whether or not it is prime\n\
2) test option 2\n\
: "))
if testcomponent == 1:
    isprime = 0
    number = int(raw_input("enter a number you would like to check\
    \n: "))
    if number >= 1:
        if number == 2:
            isprime = 1
        elif number % 2 != 0:
            if number == 3:
                isprime = 1
            elif number % 3 != 0:
                isprime = 1
                for n in range(4, number / 2 + 1):
                    if number % n == 0:
                        isprime = 0
            else:
                print "error: unexpected else"
    else:
        isprime = 0
    if isprime == 0:
        print "the given number is not prime"
    else:
        print "the given number is prime"
elif testcomponent == 2:
    print "option 2"
else:
    print "not a valid option"
raw_input("press ENTER to close program")
