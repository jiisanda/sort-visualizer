import random
import matplotlib.pyplot as plt

from typing import List


def bogo_sort(numbers: List[int]):
    """Bogo sort algorithm."""
    step = 0
    while numbers != sorted(numbers):
        random.shuffle(numbers)
        step += 1
        plt.bar(range(len(numbers)), numbers)
        plt.title(f"Step: {step}")
        plt.pause(0.1)
        plt.cla()

    return numbers, step


if __name__ == '__main__':
    n = int(input("Enter the number of elements: "))
    rang = int(input("Enter the range of elements: "))

    # Create a list of n random numbers
    numbers = random.sample(range(rang), n)

    # Print the unsorted list
    print(f"Unsorted list: {numbers}")
    plt.figure()
    plt.bar(range(len(numbers)), numbers)
    plt.title("Unsorted list")
    plt.show(block=False)
    plt.pause(1)

    # Sort the list
    numbers, steps = bogo_sort(numbers)

    # Print the sorted list
    print(f"Sorted list: {numbers}")
    plt.figure()
    plt.bar(range(len(numbers)), numbers)
    plt.title(f"Sorted list, with {steps} steps.")
    plt.show()
    plt.pause(5)
