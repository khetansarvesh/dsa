
# 1. Iterative (1 String Input)
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




# 2. Recursive (1 String Input)
Use in those questions wherein we need to find all possible cases. Now in recurssion we know that we reduce into equivalent smaller subproblem. Now there are two ways to reduce a string into a smaller string : 
1. Reduce from end (preferred and all the below solution are done using this)
2. Reduce from start

- <ins> 1 Recursive Tree </ins> : 
these questions are just for learning and ideally iterative approach is the preferred solution here. Hence you might not find here questions wherein you need to deal with all possible cases and so its okay if you dont think of solution such questions using recurssion.
    - [Leap of Faith Based Questions]()

- <ins> >1 Recursive Tree </ins> : 
here you will find questions wherein you need to deal with all possible cases hence you should think of recursion to solve it.
    - [Leap of Faith Based Questions]() : use in questions wherein we don't need to print all cases.
    - [Choice / (Input-Output) Based Questions] : use in questions wherein you need to print all cases.
        - [2 Recursive Tree](https://khetansarvesh.medium.com/string-recursion-input-output-method-f5b8d9d00675)
        - [>2 Recursive Tree](https://khetansarvesh.medium.com/string-recursion-input-output-method-part-2-37b3aea401d4)



### Dynamic Programming (DP)
Note that all the above recursive algorithm can be improved using [Dynamic Programming (DP)]() where there are overlapping subproblems !!


### Backtracking
Note that in above resursive algorithms if instead of using pass by value we use pass by reference (done using lists in python) then we will have to use [backtracking]() to solve the problem.
- but why would someone use pass by reference? becuase it sometimes makes the problem easier to solve.


<br><br><br>
<br><br><br>



# 3. String Matching (2 String Input)
Use in those questions wherein we are given two strings in input.