###########
# Mobiles #
###########
def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root] + list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def mobile(left, right):
    """Construct a mobile from a left side and a right side."""
    return tree(None, [left, right])

def sides(m):
    """Select the sides of a mobile."""
    return branches(m)

def side(length, mobile_or_weight):
    """Construct a side: a length of rod with a mobile or weight at the end."""
    return tree(length, [mobile_or_weight])

def length(s):
    """Select the length of a side."""
    return root(s)

def end(s):
    """Select the mobile or weight hanging at the end of a side."""
    return branches(s)[0]

def weight(size):
    """Construct a weight of some size."""
    assert size > 0
    return [size]

def size(w):
    """Select the size of a weight."""
    return w[0]

def is_weight(w):
    """Whether w is a weight, not a mobile."""

    if is_leaf(w):
        return True
    return False

def examples():
    t = mobile(side(1, weight(2)),
               side(2, weight(1)))
    u = mobile(side(5, weight(1)),
               side(1, mobile(side(2, weight(3)),
                              side(3, weight(2)))))
    v = mobile(side(4, t), side(2, u))
    return (t, u, v)


def total_weight(m):
    """Return the total weight of m, a weight or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    >>> total_weight([1,[2]])
    2
    """
    if is_weight(m):
        return size(m)
    elif len(m)==2:
        return m[1][0]
    else:
        return sum([total_weight(end(s)) for s in sides(m)])

def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(side(3, t), side(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(side(1, v), side(1, w)))
    False
    >>> balanced(mobile(side(1, w), side(1, v)))
    False
    """
    def scale(m):
        if is_weight(m):
            return True, size(m)
        check = []
        for x in sides(m):
            check_side = scale(end(x))
            check += [[check_side[0], check_side[1], check_side[1] * length(x)]]
        if check[0][0] and check[1][0] and check[0][2] == check[1][2]:
           return True, check[0][1] + check[1][1]
        return False, -1
    return scale(m)[0]




def with_totals(m):
    """Return a mobile with total weights stored as the root of each mobile.

    >>> t, _, v = examples()
    >>> root(with_totals(t))
    3
    >>> print(root(t))                           # t should not change
    None
    >>> root(with_totals(v))
    9
    >>> [root(end(s)) for s in sides(with_totals(v))]
    [3, 6]
    >>> [root(end(s)) for s in sides(v)]         # v should not change
    [None, None]
    """
    if is_weight(m):
        return weight(size(m))
    if root(m)==None:
        total = total_weight(m)
    else:
        total = root(m)
    return tree(total, [side(length(s), with_totals(end(s))) for s in sides(m)])

############
# Mutation #
############

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> w(90, 'hax0r')
    'Insufficient funds'
    >>> w(25, 'hwat')
    'Incorrect password'
    >>> w(25, 'hax0r')
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    """


    lst = []
    pword = password
    def mc_afee(amount, new_password):
        def draw(amount):
            nonlocal balance
            if amount > balance:
               return 'Insufficient funds'
            balance = balance - amount
            return balance


        if len(lst)==3:
            return "Your account is locked. Attempts: " + str(lst)
        if new_password != pword:
            if new_password not in lst:
                lst.append(new_password)
                return 'Incorrect password'
            else:
                return 'Incorrect password'
            
        return draw(amount)

    return mc_afee

def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """

    passwords, wrong = [], []
    result = withdraw(0, old_password)
    if len(wrong)==3:
            return "Your account is locked. Attempts: " + str(wrong)
    def new_draw(amount, password):
        if password in passwords:
            return withdraw(amount, passwords[0])
        if result != 'Incorrect password':
            return withdraw(amount, password)
    if type(result) is str:
        wrong.append(old_password)
        return result
    else: 
        passwords.append(old_password)
        passwords.append(new_password)
        return new_draw
        
