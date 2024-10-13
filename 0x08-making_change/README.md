i# 0x08. Making Change

### Tasks

### [0. Change comes from within](./0-making_change.py)

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount `total`.

- [x] Prototype: def makeChange(coins, `total`)
- [x] Return: fewest number of coins needed to meet `total`
  - [x] If `total` is `0` or less, return `0`
  - [x] If `total` cannot be met by any number of coins you have, return `-1`
- [x] `coins` is a list of the values of the coins in your possession
- [x] The value of a coin will always be an integer greater than `0`
- [x] You can assume you have an infinite number of each denomination of coin in the list
- [x] Your solution’s runtime will be evaluated in this task

```sh
carrie@ubuntu:~/0x08-making_change$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

carrie@ubuntu:~/0x08-making_change$
```

```sh
carrie@ubuntu:~/0x08-making_change$ ./0-main.py
7
-1
carrie@ubuntu:~/0x08-making_change$
```
Solution
Approach
The dynamic programming approach is efficient for this problem because it builds the solution incrementally while reusing previously computed results to avoid redundant calculations.

Here's how the algorithm will work:

Initialization:

If the total is 0 or less, return 0 because no coins are needed.
Create an array dp of size total + 1, where each index i represents the minimum number of coins required to make a total of i. Initialize all elements of dp to infinity (float('inf')), except dp[0] which should be 0 (since zero coins are needed to make a total of 0).
Dynamic Programming Transition:

Iterate through each coin denomination and update the dp array. For each coin coin and each possible amount i (from coin to total), update dp[i] as:
𝑑
𝑝
[
𝑖
]
=
min
⁡
(
𝑑
𝑝
[
𝑖
]
,
𝑑
𝑝
[
𝑖
−
𝑐
𝑜
𝑖
𝑛
]
+
1
)
dp[i]=min(dp[i],dp[i−coin]+1)
This formula says: if we include this coin, the minimum number of coins to make i is the minimum of the current value dp[i] or the value of dp[i - coin] + 1.
Final Check:

If dp[total] is still infinity, it means it's impossible to make the total with the given coins, so return -1. Otherwise, return dp[total], which is the minimum number of coins needed.
Complexity
Time Complexity: 
𝑂
(
𝑛
×
𝑚
)
O(n×m), where 
𝑛
n is the total and 
𝑚
m is the number of coins. This is efficient for moderate values of total and small to medium-sized coin lists.
Space Complexity: 
𝑂
(
𝑛
)
O(n) for storing the dp array.
