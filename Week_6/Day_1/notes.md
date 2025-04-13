# Linear Search

## What is Linear Search?
Linear search, also known as sequential search, is the simplest searching algorithm. It works by checking each element in a list or array one by one until it finds the target value.

## How it Works
1. Start from the first element of the array
2. Compare the current element with the target value
3. If they match, return the index
4. If they don't match, move to the next element
5. Repeat steps 2-4 until the element is found or the end of the array is reached

## Time Complexity
- Best Case: O(1) - When the target element is found at the first position
- Average Case: O(n/2) - When the target element is found in the middle
- Worst Case: O(n) - When the target element is at the last position or not present

## Space Complexity
- O(1) - It uses constant extra space

## Advantages
1. Simple to implement
2. Works on unsorted arrays
3. No additional memory required
4. Works well for small datasets

## Disadvantages
1. Inefficient for large datasets
2. Time complexity increases linearly with the size of the input
3. Not suitable for real-time applications with large data


## When to Use Linear Search?
1. When the list is small
2. When the list is unsorted
3. When you need to find all occurrences of an element
4. When memory is a constraint

## Real-world Applications
1. Finding a specific book in a small library
2. Searching for a contact in a phone's contact list
3. Looking up a word in a dictionary (though binary search is better for this)
4. Finding a specific item in a grocery list

## Tips for Implementation
1. Always check if the array is empty
2. Consider edge cases (first element, last element, not found)
3. Return appropriate values (index or -1)
4. Add comments for better code readability

## Common Mistakes to Avoid
1. Not handling empty arrays
2. Forgetting to return -1 when element is not found
3. Using complex data structures when simple array would suffice
4. Not considering the worst-case scenario

## Practice Problems
1. Find the first occurrence of a number in an array
2. Find the last occurrence of a number in an array
3. Count the number of occurrences of a number
4. Find the minimum and maximum elements in an array
