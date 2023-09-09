import random

A = random.sample(range(100), 5)
print("Unsorted: ", A)

step = 0
swap = 0

for i in range(len(A)):
    for j in range(len(A)):
        step += 1
        if A[i] < A[j]:
            swap += 1
            A[i], A[j] = A[j], A[i]
            print(A)

print("\n\nThe sorted array:")
print(f"{A} with {swap} swaps in {step} steps.")
