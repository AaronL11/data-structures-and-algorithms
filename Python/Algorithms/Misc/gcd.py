
"""
These are python implementations of the Euclidean Algorithm to
find the Greatest Common Divisor between two integers a and b

The Euclidean Algorithm takes two numbers a and b and divides them

a  = q₀b  + r₀
b  = q₁r₀ + r₁
r₀ = q₂r₁ + r₂
⋮	 ⋮	   ⋮
rₙ₋₂ = qₙrₙ₋₁ + rₙ

if a is less than b we simply swap the order.

There are two approaches used, the Recursive approach, and an iterative approach

"""

# Recursive

def gcd_rec(a,b):
    '''
        Due to the recursive nature of the Euclidean Algorithm,
        recursion is a great fit for this problem.
        
        We only need a check to see if the remainder is non-zero,
        and pass in the the last divisor with the remainder.
        
        If the remainder is zero; we just return the last divisor, which was 'b'.

        We also need to provide a swap if 'a' happens to be smaller than 'b'.
    '''
    if a < b: a,b = b,a
    return gcd_rec(b, r) if (r := a % b) else b


# Iterative

def gcd_iter(a,b):
    '''
        s
    '''
    if a < b: a,b = b,a
    while (r := a % b) :
        a,b = b,r
    return b

# Testing

def main(iterations):
    '''
        We are simply testing both algorithms against themselves
        this is just to see if they map the same values to each other.
    '''
    from random import randint
    for _ in range(iterations):
        a,b = randint(1,256), randint(1,256)
        assert gcd_iter(a,b) == gcd_rec(a,b)

if __name__ == '__main__':
    import sys
    main(int(sys.argv[1]))
    # This is just to test the algorithm with some already known values
    assert gcd_iter(1071,462) == 21
    assert gcd_rec(1071,462) == 21
    assert gcd_iter(98,274) == 2
    assert gcd_rec(98,274) == 2
    assert gcd_iter(56,243) == 1
    assert gcd_rec(56,243) == 1
    assert gcd_iter(93876,2174) == 2
    assert gcd_rec(93876,2174) == 2