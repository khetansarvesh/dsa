There is a proof which shows that any problem can be solved via both iterative approach and recursive approach. But in some problems its easiler to think the iterative approach while in some problem it is easier to think the recursive approach !!

# $\color{cyan}{1.\ Iterative\}$
Use in those questions wherein we DONT need to find all possible cases.

- Pointer Based Questions 
    - Single Pointer
    - Two Pointer
    - Three Pointer

- Prefix Array
    - Prefix Sum Array
    - Prefix Max Array

- Sliding Window
    - Fixed Sliding Window
    - Variable Sliding Window

- Extra Space
    - Stack
    - Queue
    - Priority Queue
    - Hashing
    - Hashing + Priority Queue

- Greedy


<br><br><br>
<br><br><br>























# $\color{cyan}{2.\ Recursive\}$

Use in those questions wherein we need to find all possible cases. 

Now in recurssion we know that we reduce into equivalent smaller subproblem. Now there are two ways to reduce an array into a smaller array : 
1. Reduce from end (preferred and most of the below solution are done using this)
2. Reduce from start


## $\color{red}{2.1\ Recursion}$

- <ins> 1 Recursive Tree </ins> : 
these questions are just for learning and ideally iterative approach is the preferred solution here. Hence you might not find here questions wherein you need to deal with all possible cases and so its okay if you dont think of solving such questions using recurssion.
    - [Natural Decomposition Based Questions (leap of faith approach)]()

- <ins> 2 Recursive Tree </ins> : 
here you will find questions wherein you need to deal with all possible cases hence you should think of recursion to solve it.
    - [Natural Decomposition Based Questions (leap of faith approach)]()
        - Complete Recursion
        - Controlled Recursion
    - <ins> Choice Based Decomposition Questions (leap of faith approach) </ins>
        - [Complete Recursion](https://skhetan.substack.com/p/two-way-complete-recursion-choice)
        - [Controlled Recursion](https://skhetan.substack.com/p/two-way-controlled-recursion-choice)

- <ins> Variable Size Recursive Tree </ins> : 
    - [Natural Decomposition Based Questions (leap of faith approach)]()
        - Complete Recursion
        - Controlled Recursion
    - [Choice Based Decomposition Questions (leap of faith approach)]()
        - Complete Recursion
        - Controlled Recursion


## $\color{red}{2.2\ Dynamic\ Programming\ (DP)}$
Note that all the above recursive algorithm can be improved using [Dynamic Programming (DP)]() where there are overlapping subproblems !!