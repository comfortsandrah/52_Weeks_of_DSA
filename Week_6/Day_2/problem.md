
## Problem: Convert B to A with Operations

You are given an array `A` of length `N`.  
You also have an array `B` of length `N` such that initially `B[i] = 0` for all `1 <= i <= N`.

You can apply the following operation on array `B` any number of times:

> Choose **(N - 1)** distinct indices and add **1** to each of those indices.

### Task

Find the **minimum number of operations** required to convert array `B` into array `A` by applying the given operation.  
If it is **impossible**, return `-1`.

---

### Function Signature

```python
def solve():
    # Your code here
```

The function will read input and output the results for each test case.

---

### Input Format

- The first line contains an integer `T`, the number of test cases.
- For each test case:
  - The first line contains an integer `N`, the size of the array `A`.
  - The second line contains `N` space-separated integers representing the array `A`.

---

### Output Format

- For each test case, print a single line containing:
  - The number of operations required to convert `B` into `A`, or
  - `-1` if it's impossible.

---

### Constraints

```
1 ≤ T ≤ 10^4  
2 ≤ N ≤ 10^5  
0 ≤ A[i] ≤ 10^9  
Sum of N over all test cases does not exceed 2 * 10^5
```

---

### Sample Input

```
2
3
3 1 0
2
0 2
```

### Sample Output

```
-1
2
```

---

### Explanation

#### Test Case 1:
```
N = 3, A = [3, 1, 0]
Initial B = [0, 0, 0]
No number of valid operations can convert B into A → Answer: -1
```

#### Test Case 2:
```
N = 2, A = [0, 2]
Initial B = [0, 0]
Apply operation on index 2 → B = [0, 1]  
Apply operation on index 2 → B = [0, 2]  
Now B = A → Answer: 2
```
[HackerEarth:-Make an array](https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/make-an-array-85abd7ad/?purpose=login&source=problem-page&update=github)
