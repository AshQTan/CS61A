HW_SOURCE_FILE = 'hw04.py'

def g(n):
    """Return the value of G(n), computed recursively.
    G(n) = n,                                       if n <= 3
    G(n) = G(n - 1) + 2 * G(n - 2) + 3 * G(n - 3),  if n > 3
    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    if n<=3:
        return n
    return g(n-1)+2*g(n-2)+3*g(n-3)


def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    if n<=3:
        return n
    n1, n2, n3 = 1,2,3
    while n>3:
        n1, n2, n3 = n2, n3, 3*n1+2*n2+n3

        n-=1
    return n3

def pingpong(n):
    """Return the nth element of the ping-pong sequence.
    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    return pong_rec(n, 1, 1, 1)

def pong_rec(n, c, seq, direction):
    if c == n:
        return seq
    if (c+1)%7==0 or has_seven(c+1):
        return pong_rec(n, c+1, seq+direction, direction*-1)
    return pong_rec(n, c+1, seq+direction, direction)    
    

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    return count(1, amount)



def count(min, amount):
    if amount<0:
        return 0
    elif amount==0:
        return 1
    elif min > amount:
        return 0
    power = 0
    while 2**power<amount:
        power+=1
    else:
        return count(min, amount-min) + count(min*2, amount)

    """total = 0
    power=0
    if amount==0 or amount==1:
        return 1
    #return count_change(amount-1)+count_change(amount-2**power)
    total += count_change(amount-1)
    while amount-2**power>0:
        total+=count_change(amount-2**power)
        power+=1
    return total"""
 

###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'
