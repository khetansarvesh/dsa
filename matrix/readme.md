# 1. Iterative

## $\color{red}{1.1\ Brute\ Force\ (Pointers)}$
All iterative questions can be solved using pointer approach
- [Two Pointer](https://skhetan.substack.com/p/two-pointers-matrix) : has O(n^2) or O(n^3) time complexity

## $\color{red}{1.2\ Extra\ Space}$
- [Stack](https://skhetan.substack.com/p/stacks-matrix)
- [Priority Queue / Heap](https://skhetan.substack.com/p/heap-matrix) : use when we need to find Kth something + (min/closest/smallest) problems
- Hashing :
  - [Arrays as Hashtables](https://skhetan.substack.com/p/hashing-arrays-matrix)
  - [Maps as Hashtables (Hashmaps)](https://skhetan.substack.com/p/hashing-maps-matrix)


## $\color{red}{1.3\ Decrease\ and\ Conquere}$
This is an optimized way to solve questions where you have sorted matrix. These questions can be solved via brute force approach (two pointers) in O(n^2) but since matrix is sorted we can use this information to reduce the time complexity.
- [Questions where 'sorted' word mentioned](https://skhetan.substack.com/p/decrease-and-conquer-matrix)
- [Questions where 'sorted' word not mentioned](https://skhetan.substack.com/p/decrease-and-conquer-matrix-d4c)











# 2. Recursive

## $\color{red}{2.1\ Dynamic\ Programming\ (DP)}$
Note that all the above recursive algorithm can be improved using [Dynamic Programming (DP)]() where there are overlapping subproblems !!



## $\color{red}{2.2\ Backtracking}$
In matrix we usually pass the matrix using call by reference hence here we use [backtracking]() aggressively to solve recursion !!
- Knight Attack Problem
- Rat in a maze : [Logic](https://www.youtube.com/watch?v=7AYJLrDxbBU&list=PL_z_8CaSLPWdbOTog8Jxk9XOjzUs3egMP&index=12) / [Code](https://www.youtube.com/watch?v=4Wc_QCxr_WQ&list=PL_z_8CaSLPWdbOTog8Jxk9XOjzUs3egMP&index=13)
- N Queens : [Logic](https://www.youtube.com/watch?v=UYF5Lzp9jH8&list=PL_z_8CaSLPWdbOTog8Jxk9XOjzUs3egMP&index=18) / [Code](https://www.youtube.com/watch?v=B_rT88Qstec&list=PL_z_8CaSLPWdbOTog8Jxk9XOjzUs3egMP&index=19)
- Sudoku Solver : [Logic](https://www.youtube.com/watch?v=r3QYHZ47O1A&list=PL_z_8CaSLPWdbOTog8Jxk9XOjzUs3egMP&index=20) / [Code](https://www.youtube.com/watch?v=MlZMrHZCtb8&list=PL_z_8CaSLPWdbOTog8Jxk9XOjzUs3egMP&index=21)
- Print all possible paths from start to end of a matrix
