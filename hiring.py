import random
import math

def create_list_of_candidates(n):
    """
    This function creates a list of n candidates and randomly permutes it.

    Args:
    n (int): the number of candidates

    Returns:
    cand (list): A list of n candidates
    """
    cand = list(range(1, n + 1))
    random.shuffle(cand)
    return cand


def hire_assistant(cand):
    """
    This function simulates the hiring process of an assistant.

    Args:
    cand (list): A list of candidates.

    Returns:
    hired (int): The percentile rank of the hired candidate.
    """
    # Sample the first n/e candidates.
    n = len(cand)
    e = math.e
    m = int(n / e)
    sample = [cand[i] for i in range(m)]
    best_in_sample = max(sample)
    # Create a list of non sampled candidates.
    non_sample = [cand[i] for i in range(m, n)]
    # Hire the candidate which is better than all the sampled candidates.
    hired = 0
    for i in range(len(non_sample)):
        # If there are no more candidates to be interviewed, hire the last one.
        if i == len(non_sample)-1:
            hired = non_sample[i]
        # If the candidate is better than the best in the sample, hire him/her.
        elif non_sample[i] > best_in_sample:
            hired = non_sample[i]
            break
    return (100 * hired / n)



def simulate():
    """
    Main function to simulate the hiring process.
    """
    # Let number of candidates be 100
    n = 100
    # Simulate the experiment 100000 times.
    observation = []
    for i in range(100000):
        # Create a list of candidates and hire the best one.
        cand = create_list_of_candidates(n)
        # Hire the best candidate and record his/her percentile rank.
        best = hire_assistant(cand)
        # Record the percentile rank of the hired candidate.
        observation.append(best)
    print("The average percentile of the hired candidate is", sum(observation) /
          len(observation))


if __name__ == "__main__":
    simulate()


