import random
import numpy as np, numpy.random
import matplotlib.pyplot as plt

"""
Create three companies A, B, C and store the total money of each company.
"""
# Initial total money of A, B, C is 0.
total_money_A = 0
total_money_B = 0
total_money_C = 0

"""
Create variables to store the bank balance of 3 investors S, M, D.
"""
# Initial bank balance of S, M, D is 100000.
balance_S = 100000
balance_M = 100000
balance_D = 100000


# Create a function which invests the money of the investors 
# in each company A, B, C. The function returns the number of shares owned by
# each investor in each company as a list.
def invest():
    # Declare global variables.
    global total_money_A
    global total_money_B
    global total_money_C
    global balance_S
    global balance_M
    global balance_D
    # Create lists that store the percent share of S, M, D in A, B, C
    # respectively.
    shares_A = []
    shares_B = []
    shares_C = []

    # S invests 20% of his balance in A, 30% in B, 50% in C.
    m = np.random.dirichlet(np.ones(3),size=1) #
    x = 0.2 + m[0][0] * 0.01
    y = 0.3 + m[0][1] * 0.01
    z = 0.5 + m[0][2] * 0.01
    total_money_A += x * balance_S
    total_money_B += y * balance_S
    total_money_C += z * balance_S

    # M invests all the money in random percentage.
    # Take 3 random numbers which add to 1.
    l = np.random.dirichlet(np.ones(3),size=1) #
    p = l[0][0]
    q = l[0][1]
    r = l[0][2]
    total_money_A += p * balance_M
    total_money_B += q * balance_M
    total_money_C += r * balance_M

    # D invests 33.33% of his balance in A, 33.33% in B, 33.34% in C
    total_money_A += 0.3333 * balance_D
    total_money_B += 0.3333 * balance_D
    total_money_C += 0.3334 * balance_D

    # Calculate the number of shares owned by each investor in each company.
    # Append the shares of A to the list.
    shares_A.append(x * balance_S / total_money_A)
    shares_A.append(p * balance_M / total_money_A)
    shares_A.append(0.3333 * balance_D / total_money_A)

    # Append the shares of B to the list.
    shares_B.append(y * balance_S / total_money_B)
    shares_B.append(q * balance_M / total_money_B)
    shares_B.append(0.3333 * balance_D / total_money_B)

    # Append the shares of C to the list.
    shares_C.append(z * balance_S / total_money_C)
    shares_C.append(r * balance_M / total_money_C)
    shares_C.append(0.3334 * balance_D / total_money_C)

    # Reset the balance of S, M, D to 0.
    balance_S = 0
    balance_M = 0
    balance_D = 0

    return shares_A, shares_B, shares_C

def simulate():
    """This function simulates each round.
    """
    # Declare global variables.
    global total_money_A
    global total_money_B
    global total_money_C
    global balance_S
    global balance_M
    global balance_D

    # Choose a company A, B, C such that probability of A is 0.2, B is 0.3, C is 0.5.
    winner = random.choice(['A', 'B', 'C'])
    
    # Invest the money of the investors in each company.
    shares_A, shares_B, shares_C = invest()

    # Return the money to the investors.
    if winner == 'A':
        balance_S += 300000 * shares_A[0]
        balance_M += 300000 * shares_A[1]
        balance_D += 300000 * shares_A[2]
    elif winner == 'B':
        balance_S += 300000 * shares_B[0]
        balance_M += 300000 * shares_B[1]
        balance_D += 300000 * shares_B[2]
    else:
        balance_S += 300000 * shares_C[0]
        balance_M += 300000 * shares_C[1]
        balance_D += 300000 * shares_C[2]

    # Reset the total money of each company to 0.
    total_money_A = 0
    total_money_B = 0
    total_money_C = 0

def main():
    """This function simulates 1000 rounds.
    """
    # Simulate 1000 rounds and plot the variation in the bank balance of S, M,
    # D using matplotlib.
    # Create a list to store the bank balance of S, M, D after each round.
    global balance_S
    global balance_M
    global balance_D
    list_S = []
    list_M = []
    list_D = []

    for i in range(1000):
        simulate()
        list_S.append(balance_S)
        list_M.append(balance_M)
        list_D.append(balance_D)

    # Plot the variation in the bank balance of S, M, D using matplotlib.
    plt.plot(list_S, label='S')
    plt.plot(list_M, label='M')
    plt.plot(list_D, label='D')
    plt.xlabel('Number of rounds')
    plt.ylabel('Bank balance')
    plt.legend()
    plt.show()
    # Print the final bank balance of S, M, D.
    print("Final bank balance of S: ", balance_S)
    print("Final bank balance of M: ", balance_M)
    print("Final bank balance of D: ", balance_D)

if __name__ == '__main__':
    main()


