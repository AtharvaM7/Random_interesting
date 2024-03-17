import random
import matplotlib.pyplot as plt

def estimate_num_tanks(serial_nums):
    """
    This function estimates the number of tanks produced based on the serial
    numbers.

    Args:
    serial_nums (list): A list of serial numbers.

    Returns:
    est_tanks (int): The estimated number of tanks produced.
    """
    # # Removing all the duplicates from the list to convert this problem into the
    # # 'repetition not allowed' version, but on running the simulation, not
    # # doing this yields in better results. 
    # serial_nums = list(set(serial_nums))

    m = len(serial_nums)
    max_serial = max(serial_nums) # The maximum serial number

    # Making the prediction by dividing the numbers in m parts.
    est_tanks = m * (max_serial)/(m-1)

    # Return the number of tanks.
    return est_tanks


def capture_tanks(n_true, k):
    """
    This function creates a list of captured tanks.

    Args:
    n_true (int): Actual number of tanks.
    k (int): Number of tanks sampled

    Returns:
    serial_nums (list): List of serial numbers of tanks captured with repition
    allowed.
    """
    # Sample the tanks using for loop
    serial_nums = []
    for i in range(k):
        serial_nums.append(random.randint(1, n_true))

    # Return the list.
    return serial_nums

def simulate():
    # Let n_true = 1000
    n_true = 1000
    # Let k = 100
    k = 500

    # Simulate this 1000 times and observe the result
    observations = [estimate_num_tanks(capture_tanks(n_true, k)) for i in
                    range(1000)]

    # Print the average of the observations and compare the result with n_ture.
    print(sum(observations)/len(observations))
    print("Percent error: ", 100*(abs(n_true - sum(observations)/len(observations))/n_true))


if __name__ == "__main__":
    simulate()
