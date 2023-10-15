''' This program implements the Newton-Rhapson method for finding the roots of a function. '''

def math_func(x):
    '''This is the function which we want to find the roots of.'''
    return (x+1)*(x-2)*(x-3)


def derivative(p):
    '''This is the derivative of the functiion math_func at the point x = p.'''
    # Using the definition of derivative
    h = 0.00001 #10^-5, h can be adjusted for better accuracy
    return (math_func(p+h) - math_func(p))/h

def find_root(p):
    '''This function finds the root of the function math_func.
    It takes an initial guess n.
    Then it moves towards the next closest approximation by n = n - f(n)/f'(n).
    It does this for 10000 iterations and returns the final value of p.
    The root of the function math_func lies at x = p.'''

    for i in range(10000):
        p = p - math_func(p)/derivative(p)
    return p

def main():
    '''This is the main function.'''
    # All initial guesses dont give a correct root.

    # Define a tolerance eps
    eps = 0.00001 #10^-5, eps can be adjusted for better accuracy

    # If f(calaulated_root) is within eps of 0, then we have found the root.
    # If not, then we have to try a different initial guess.

    # Try initial guesses from 0 to 99
    for i in range(100):
        if abs(math_func(i) - 0) < eps:
            # Root found 
            return 'The root of the function is ' + str(i) + '.'

        else:
            # Try a different initial guess
            continue
   
   # If no root is found, then try for 0 to -99
    for i in range(100):
        if abs(math_func(-i) - 0) < eps:
            # Root found 
            return 'The root of the function is ' + str(-i) + '.'

        else:
            # Try a different initial guess
            continue

    # If no root is found, then return error
    return 'No root found.'

print(main())
