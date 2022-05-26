def fibonacci(n):
    '''
    Returns the nth fibonacci number in the series.\n
    Requires an integer input representing the index in the series.\n
    Index starts at 0: [0, 1, 1, 2, 3, 5, ...]
    '''
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    '''
    Returns the nth lucas number in the series.\n
    Requires an integer input representing the index in the series.\n
    Index starts at 0: [2, 1, 3, 4, 7, ...]
    '''
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n-1) + lucas(n-2)

def sum_series(n, first = 0, second = 1):
    '''
    Returns the nth number in the series created by summing the previous two numbers in the series.\n
    Requires an integer input representing the index in the series.\n
    Optionally accepts two additional parameters representing first two numbers in the series.
    Default values for optional parameters correspond to the first two numbers in the fibonacci sequence.\n
    Index starts at 0: first=0, second=1, ..., [n-1] + [n-2]
    '''
    if n == 0:
        return first
    if n == 1:
        return second
    return sum_series(n-1, first, second) + sum_series(n-2, first, second)

def sum_series_iteration(n, first = 0, second = 1):
    '''
    Returns the nth number in the series created by summing the previous two numbers in the series.\n
    Requires an integer input representing the index in the series.\n
    Optionally accepts two additional parameters representing first two numbers in the series.
    Default values for optional parameters correspond to the first two numbers in the fibonacci sequence.\n
    Index starts at 0: first=0, second=1, ..., [n-1] + [n-2]\n
    Uses iteration to find solution. Suitable for large n.
    '''
    prev1 = second
    prev2 = first
    for i in range(n):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    return current