
# $\color{cyan}{1.\ Iterative\}$

Use in those questions wherein we dont need to find all possible cases
- Pointer
    - Single Pointer
    - Two Pointer
    - Three Pointer
- Sliding Window
    - Fixed Sized
    - Variable Sized
- Extra Space
    - Stack
    - Hashing



<br><br><br>
<br><br><br>



# $\color{cyan}{2.\ Recursive\}$
Use in those questions wherein we need to find all possible cases. Now in recurssion we know that we reduce into equivalent smaller subproblem. Now there are two ways to reduce a string into a smaller string : 
1. Reduce from end (preferred and most of the below solution are done using this)
2. Reduce from start (usually not preferred but sometimes is the only option and you cant reduce from the end, why? this is usually true in questions wherein forward information presented by a string is important for the question !!)


## $\color{red}{2.1\ Recursion}$

- <ins> 1 Recursive Tree </ins> : 
these questions are just for learning and ideally iterative approach is the preferred solution here. Hence you might not find here questions wherein you need to deal with all possible cases and so its okay if you dont think of solution such questions using recurssion.
    - [Leap of Faith Based Questions](https://khetansarvesh.medium.com/string-recursion-toy-problems-1343a06e5957)
    - [Input-Ouput Based Questions](https://khetansarvesh.medium.com/string-recursion-input-output-method-toy-problems-6b8e4d1cb5e7)




- <ins> 2 Recursive Tree </ins> : 
here you will find questions wherein you need to deal with all possible cases hence you should think of recursion to solve it.
    - [Leap of Faith Based Questions]() : use in questions wherein we don't need to print all cases.
    - [Choice / (Input-Output) Based Questions](https://khetansarvesh.medium.com/string-recursion-input-output-method-f5b8d9d00675) : use in questions wherein you need to print all cases.




- <ins> Variable Size Recursive Tree </ins> : 
    - [Leap of Faith Based Questions]() : use in questions wherein we don't need to print all cases.
    - [Choice / (Input-Output) Based Questions](https://khetansarvesh.medium.com/string-recursion-input-output-method-part-2-37b3aea401d4) : use in questions wherein you need to print all cases.




## $\color{red}{2.2\ Dynamic\ Programming\ (DP)}$
Note that all the above recursive algorithm can be improved using [Dynamic Programming (DP)]() where there are overlapping subproblems !!


## $\color{red}{2.3\ Backtracking}$
Note that in above resursive algorithms if instead of using pass by value we use pass by reference (done using lists in python) then we will have to use [backtracking](https://khetansarvesh.medium.com/backtracking-in-strings-1e2461e2856f) to solve the problem.
- but why would someone use pass by reference? becuase it sometimes makes the problem easier to solve.
- Mostly Backtracking is found to be used in those questions wherein we have variable size recursion tree.


<br><br><br>
<br><br><br>