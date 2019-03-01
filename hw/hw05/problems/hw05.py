def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    def move(d, top, mid, bot):
        if d>0:
            move(d-1, top, bot, mid)
            if top[0]:
                c = top[0].pop()
                print_move(top[1], bot[1])
                bot[0].append(c)
            move(d-1, mid, top, bot)
        
    strt = ([n-x for x in range(n)], 1)
    md = [[], 2]
    nd = [[], 3]
    return move(n, strt, md, nd)

def interval(a, b):
    """Construct an interval from a to b."""
    return [a, b]

def lower_bound(x):
    """Return the lower bound of interval x."""
    best = x[0]
    for c in x:
        if c < best:
            best = c
    return best


def upper_bound(x):
    """Return the upper bound of interval x."""
    best = x[0]
    for c in x:
        if c > best:
            best = c
    return best

def str_interval(x):
    """Return a string representation of interval x."""
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y."""
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y."""
    lowx, lowy, highx, highy = lower_bound(x), lower_bound(y), upper_bound(x), upper_bound(y)
    if lowx >= 0and lowy >=0:
        return interval(lowx*lowy, highx*highy)
    if lowx<0 and lowy >=0:
        if highx < 0:
            return(interval(lowx*highy, highx*lowy))
        return interval(lowx*highy, highx*highy)
    if lowx>=0 and lowy<0:
        if highy < 0:
            return(interval(highx*lowy, highx*lowy))
        return interval(highx*lowy, lowx*highy)
    if highx < 0 and highy < 0:
        return interval(lowx*highy, lowx*lowy)
    if highx<0 and highy>=0:
        return interval(highx*highy, lowx*lowy)
    if highx>=0 and highy<0:
        return interval(highx*lowy, lowx*lowy)
    else:
        return interval(lower_bound(lowx*highy, highx*lowy), upper_bound(lowx*lowy, highx*highy))

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y."""

    lowx, lowy, highx, highy = lower_bound(x), lower_bound(y), upper_bound(x), upper_bound(y)
    if lowx < 0 and highy >= 0:
        if highx >= 0 and highy<0:
            return interval(lowx-highy, highx-highy)
        return interval(lowx-highy, highx - lowy)



def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided by
    any value in y. Division is implemented as the multiplication of x by the
    reciprocal of y."""
    assert lower_bound(y) >= 0, "Div by 0 error"
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

def check_par():
    """Return two intervals that give different results for parallel resistors.

    >>> r1, r2 = check_par()
    >>> x = par1(r1, r2)
    >>> y = par2(r1, r2)
    >>> lower_bound(x) != lower_bound(y) or upper_bound(x) != upper_bound(y)
    True
    """
    r1 = interval(1, 4) # Replace this line!
    r2 = interval(1, 2) # Replace this line!
    return r1, r2

def multiple_references_explanation():
    return """Eva is right. Par1's use of nested functions can lead to wrong 
    values for intervals (i.e. squaring using mul_interval can give a negative value
    for the range if the given interval's lower bound is also negative, which is false)

    """

def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    xtreme = -1 * b/(2*a)


    xinterval = [lower_bound(x), upper_bound(x)]

    def eq(var):
        return ((a*var**2)+(b*var)+c)

    f = [eq(x) for x in xinterval]
    if lower_bound(x)<=xtreme<=upper_bound(x):
        return interval(min(f+[eq(xtreme)]), max(f+[eq(xtreme)]))
    return interval(min(f), max(f))
    

def polynomial(x, c):
    """Return the interval that is the range of the polynomial defined by
    coefficients c, for domain interval x.

    >>> str_interval(polynomial(interval(0, 2), [-1, 3, -2]))
    '-3 to 0.125'
    >>> str_interval(polynomial(interval(1, 3), [1, -3, 2]))
    '0 to 10'
    >>> str_interval(polynomial(interval(0.5, 2.25), [10, 24, -6, -8, 3]))
    '18.0 to 23.0'
    """
    "*** YOUR CODE HERE ***"

