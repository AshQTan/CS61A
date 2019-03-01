def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    "*** YOUR CODE HERE ***"
    if a > b:
        x = a
    else:
        x = b

    while (True):
        if ((x % a == 0) and (x % b ==0)):
            return x
        x += 1

                


def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    s = []
    while n>0:
        s.append(n%10)
        n=n//10
        set(s)
    return len(set(s))

    """Bonus Code that counts how many repeating digits in a number
    ud=0
    while n>0:
        x=1
        #print ("n:",n)
        nc = n//10
        while x<len(str(n)):
            #print ("nc:", nc)
            print("n",n%10)
            print( "nc",nc%10)
            if ((n%10) == (nc%10)):
                print("worng")
                ud += 1
            nc = nc // 10
            x += 1
            print ("x:", x)
        n = n // 10
    return ud
    """

