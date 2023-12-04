"""
This is to simulate the German tank problem and reverse engineer a solution.
"""

import random
import math

def capture_tank(n):
    """
    This function captures n German tanks, and returns the number on the tank,
    """
    # Choose n unique integers from 1 to 100 and add into a list.
    captured_tanks = random.sample(range(1, 10001), n)
    return captured_tanks

"""
When we have a tank of number 52 we are sure that tanks 1 to 51 exist.
"""

def guess_total_tanks(captured_tanks):
    """
    This function estimates the total number of tanks Germany manufactured on
    the basis of the number of tanks captured.
    """
    # Sort the captured tanks
    captured_tanks.sort()
    # Find the median of the captured tanks
    median = captured_tanks[int(len(captured_tanks)/2)]
    # Find the average of the captured tanks
    avg_captured_tanks = sum(captured_tanks)/len(captured_tanks)
    # Return a list of estimated tanks
    return [median * 2, avg_captured_tanks * 2]

def main():
    # Set number of captured tanks
    n = 100
    # Print which of median or average is closer to 10000
    med_avg = {}
    med_avg[ 'Median' ] = 0
    med_avg[ 'Average' ] = 0
    for i in range(10000):
        l = guess_total_tanks(capture_tank(n))
        if abs(l[0]-10000)<abs(l[1]-10000):
            med_avg[ 'Median' ] += 1
        else:
            med_avg[ 'Average' ] += 1
    print(med_avg)
    print(l)


if __name__ == '__main__':
    main()









