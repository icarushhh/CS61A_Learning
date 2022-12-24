def make_keeper(n):
    def f(cond):
        for i in range(n):
            if cond(i+1):
                print(i+1)

    return f

make_keeper(6)(lambda x: x%2 == 0)

def f1():
    """
    >>> f1()
    3
    """
    return 3

def f2():
    """
    >>> f2()()
    3
    """
    return lambda : 3

def f3():
    """
    >>> f3()(3)
    3
    """
    return lambda x: x

def f4():
    """
    >>> f4()()(3)()
    3
    """
    return lambda :lambda x:lambda : x

print(f4()()(3)())