# Bogo Sort

- Algorithm used to sort the elements of an array by randomly generating different permutations of array and then checking whether is sorted or not 🥲.
- Based on generate and test paradigm.
- Also known as Permutation Sort, Shuffle Short, etc.

## How it works?

Let array be,
`arr = <23, 31, 17, 23, 45>`

1. First we check, if the array is already sorted.
2. If not, then we generate a random permutation of the array and check again, if the array is sorted or not.
3. This is repeated until we get a sorted array.

So, in our example,

Given array:            `arr = <23, 31, 17, 23, 45>`

1st random permutation:  `arr = <23, 23, 31, 17, 45>`

2nd random permutation:  `arr = <23, 31, 17, 23, 45>`

.

.

.

nth random permutation:  `arr = <17, 23, 23, 31, 45>`

So after say n, permutation we got the sorted array. The number of steps or permutations, can be between one to infinity 😬.

There is no guarantee 😶 that we will get the sorted array after shuffling the array a certain number of times. However, the probability of it running infinitely is very low 😉. Given time, bogo sort will eventually return the sorted array 🤷‍♂️.

## Pseudo Code

Just 3 lines...✌️

```python
while is_sorted(arr) is false do
    random_shuffle(arr)
return arr
```

## Complexities

### Time Complexity

- **Worst Case:** _O(♾️)_
- **Average Case:** _O(n!*n)_
  - Only one of n! permutations, is sorted. So, we expect to get correct answer about after _O(n!)_ iterations. And each shuffle/check operation takes _O(n)_ in itself.
- **Best Case:** _O(n)_

### Space Complexity

Does not requires any extra space for sorting input so _O(1)_.

## Observations

- Not a stable algorithm;
- Is an in-place sorting algorithm;
- No practical usage 🙄😐😑.
