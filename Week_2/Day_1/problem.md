# Implement Stack using Queues

## Problem Statement

Implement a **last-in-first-out (LIFO)** stack using only two queues. The implemented stack should support all the functions of a normal stack:

- `push(x)` — Pushes element `x` to the top of the stack.
- `pop()` — Removes the element on the top of the stack and returns it.
- `top()` — Returns the element on the top of the stack.
- `empty()` — Returns `true` if the stack is empty, `false` otherwise.

### Notes:

1. You must use **only standard operations of a queue**, which means:
   - Push to back
   - Peek/pop from front
   - Check size
   - Check if empty
2. Depending on your language, the queue may not be supported natively.  
   You can simulate a queue using a list or deque (double-ended queue) as long as you use only standard queue operations.

---

## Example

### Input:
```plaintext
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
```

### Output
[null, null, null, 2, 2, false]
```
MyStack myStack = new MyStack();
myStack.push(1);     // Push 1 onto the stack.
myStack.push(2);     // Push 2 onto the stack.
myStack.top();       // Returns 2.
myStack.pop();       // Removes and returns 2.
myStack.empty();     // Returns false (stack is not empty).

```
## Constraints:

1 <= x <= 9

At most  100  calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.

### Follow-up: Can you implement the stack using only one queue?

https://leetcode.com/problems/implement-stack-using-queues/description/ 1 / 1

