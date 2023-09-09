# I can't believe it sorts

- Python Implementation for: https://arxiv.org/abs/2110.01111
- Stanley P. Y. Fung presents an incredibly simple sorting algorithm.
- Quote from the paper

```txt
There is nothing good about this algorithm. It is slow – the algorithm obviously
runs in Θ(n2) time, whether worst-case, average-case or best-case. It unnecessarily
compares all pairs of positions, twice. It is not stable, does not work well for
external sorting, cannot sort inputs arriving online, and does not benefit from
partially sorted inputs. Its only appeal may be its simplicity, in terms of lines
of code and the “symmetry” of the two loops.
```

## Pseudo Code

```code
for i = 1 to n do
    for j = 1 to n do
        if A[i] < A[j] then
            swap A[i] and A[j]
```

## Example

`A = <5, 9, 3, 7>`

```code
i   j   A[i] < A[j]     swap        A
0   0   5 < 5           F       5, 9, 3, 7
0   1   5 < 9           T       9, 5, 3, 7
.                       F
.                       F
1   0   5 < 9           T       5, 9, 3, 7
1   1   9 < 9           F       5, 9, 3, 7
.
.
2   0   3 < 5           T       3, 9, 5, 7
2   1   5 < 9           T       3, 5, 9, 7
.
.
3   2   7 < 9           T       3, 5, 7, 9
3   3   9 < 9           F       3, 5, 7, 9

Sorted Array: <3, 5, 7, 9>
```

## Complexities

### Time complexity: _O(n2)_

### Space complexity: _O(1)_
