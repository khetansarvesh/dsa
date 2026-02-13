There is a proof which shows that any problem can be solved via both iterative approach and recursive approach. But in some problems its easiler to think the iterative approach while in some problem it is easier to think the recursive approach !!

# $\color{cyan}{1.\ Iterative\}$
Use in those questions wherein we DONT need to find all possible cases.

## $\color{red}{1.1\ Brute\ Force\ (Pointers)}$
All iterative questions can be solved using pointer approach
- Single Pointer
- Two Pointer
- Three Pointer

## $\color{red}{1.2\ Prefix/\ Cummulative\ Array}$
This is an optimized way to solve subarray based problems. 
- Prefix Sum Array
- Prefix Max Array

## $\color{red}{1.3\ Extra\ Space}$
- Stack
- Queue
- Priority Queue
- Hashing
- Hashing + Priority Queue

## $\color{red}{1.4\ Sliding\ Window}$
This is an optimized way to solve subarry + min / max problems.
- Fixed Sliding Window
    - without extra space
    - with extra space 
- Variable Sliding Window : used to solve problems wherein window size is not directly mentioned in the question hence the question mentions about some condition to give you a hint about the window size. Hence use this for (subarry) + (min / max) + (some condition) problems
    - without extra space
    - with extra space 

## $\color{red}{1.5\ Decrease\ and\ Conquere}$
This is an optimized way to solve questions where you have sorted array

## $\color{red}{1.6\ Greedy}$


<br><br><br>
<br><br><br>























# $\color{cyan}{2.\ Recursive\}$

Use in those questions wherein we need to find all possible cases. If the question says phrases like 'all possible ways' / 'subset' / 'subsequence' then for sure you need to solve it using recursion.

Now in recurssion we know that we reduce into equivalent smaller subproblem. Now there are two ways to reduce an array into a smaller array : 
1. Reduce from end (preferred and most of the below solution are done using this)
2. Reduce from start


## $\color{red}{2.1\ Recursion}$

- <ins> 1 Recursive Tree </ins> : 
these questions are just for learning and ideally iterative approach is the preferred solution here. Hence you might not find here questions wherein you need to deal with all possible cases and so its okay if you dont think of solving such questions using recurssion.
    - [Natural Decomposition Based Questions (leap of faith approach)](https://skhetan.substack.com/p/single-recursive-tree-arrays)

- <ins> 2 Recursive Tree </ins> : 
here you will find questions wherein you need to deal with all possible cases hence you should think of recursion to solve it.
    - <ins> Natural Decomposition Based Questions (leap of faith approach) </ins>
        - [Complete Recursion](https://skhetan.substack.com/p/complete-recursion-in-dual-recursive)
        - Controlled Recursion
    - <ins> Choice Based Decomposition Questions (leap of faith approach) </ins>
        - [Complete Recursion](https://skhetan.substack.com/p/two-way-complete-recursion-choice)
        - Controlled Recursion
            - [Bounded](https://skhetan.substack.com/p/two-way-controlled-recursion-choice)
            - [Unbounded](https://skhetan.substack.com/p/unbounded-controlled-recursion) 

- <ins> Variable Size Recursive Tree </ins> : 
    - <ins> Natural Decomposition Based Questions (leap of faith approach) </ins>
        - Complete Recursion
        - Controlled Recursion
    - <ins> Choice Based Decomposition Questions (leap of faith approach) </ins> : Used for partititioning type of questions
        - [Complete Recursion](https://khetansarvesh.medium.com/uniform-recursion-in-arrays-a5a08d473378)
        - Controlled Recursion


## $\color{red}{2.2\ Dynamic\ Programming\ (DP)}$
Note that all the above recursive algorithm can be improved using [Dynamic Programming (DP)](https://skhetan.substack.com/p/array-dynamic-programming-dp) where there are overlapping subproblems !!
