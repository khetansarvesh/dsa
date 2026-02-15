
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
- <ins> Fixed Sliding Window </ins> :
    - without extra space
    - with extra space 
- <ins> Variable Sliding Window </ins> : 
    - without extra space
    - [with extra space]() 


## $\color{red}{1.5\ Decrease\ and\ Conquere}$
This is an optimized way to solve questions where you have sorted array

## $\color{red}{1.6\ Greedy}$








<br><br><br>
<br><br><br>



# $\color{cyan}{2.\ Recursive\}$
Use in those questions wherein we need to find all possible cases. 

Now in recurssion we know that we reduce into equivalent smaller subproblem. Now there are two ways to reduce a string into a smaller string : 
1. Reduce from end (preferred and most of the below solution are done using this)
2. Reduce from start (usually not preferred but sometimes is the only option and you cant reduce from the end, why? this is usually true in questions wherein forward information presented by a string is important for the question !!)


## $\color{red}{2.1\ Recursion}$

- <ins> 1 Recursive Tree </ins> : 
these questions are just for learning and ideally iterative approach is the preferred solution here. Hence you might not find here questions wherein you need to deal with all possible cases and so its okay if you dont think of solving such questions using recurssion.
    - [Natural Decomposition Based Questions (leap of faith approach)](https://khetansarvesh.medium.com/string-recursion-toy-problems-1343a06e5957)




- <ins> 2 Recursive Tree </ins> : 
here you will find questions wherein you need to deal with all possible cases hence you should think of recursion to solve it.
    - Natural Decomposition Based Questions (leap of faith approach)
    - Choice Based Decomposition (Leap of Faith) : use in questions wherein you have two input strings
        - Complete Recursion
        - [Controlled Recursion](https://skhetan.substack.com/p/controlled-recursion-in-strings)
    - Input - Output Based Decomposition : use in questions wherein you need to print all cases
        - [Complete Recursion](https://khetansarvesh.medium.com/string-recursion-input-output-method-f5b8d9d00675)
        - [Controlled Recursion](https://khetansarvesh.medium.com/input-output-string-controlled-recursion-b9eaba0bd813) 






- <ins> Variable Size Recursive Tree </ins> : 
    - Natural Decomposition Based Questions (leap of faith approach) :
        - Complete Recursion
        - [Controlled Recursion](https://medium.com/p/9eca7a3e2bff?postPublishedType=initial) 
    - Choice Based Decomposition (Leap of Faith) : Used for partititioning type of questions
        - [Complete Recursion](https://medium.com/@khetansarvesh/variable-size-recursion-strings-23fa9fca5193)
        - Controlled Recursion 
    - Input - Output Based Decomposition : use in questions wherein you need to print all cases.
        - [Complete Recursion](https://khetansarvesh.medium.com/string-recursion-input-output-method-part-2-37b3aea401d4)
        - Controlled Recursion 




## $\color{red}{2.2\ Dynamic\ Programming\ (DP)}$
Note that all the above recursive algorithm can be improved using [Dynamic Programming (DP)](https://khetansarvesh.medium.com/strings-dp-b0135bd81379) where there are overlapping subproblems !!


## $\color{red}{2.3\ Backtracking}$
Note that in above resursive algorithms if instead of using pass by value we use pass by reference then we will have to use backtracking to solve the problem. We will see [String Permutations](https://www.youtube.com/watch?v=EnRciMd08_g) problem to understand the difference. We saw this problem [here](https://khetansarvesh.medium.com/string-recursion-input-output-method-part-2-37b3aea401d4) but here we solved it without backtracking becuase we did not pass the string using pass by reference hence we did not require backtracking but now we will use pass by reference and hence we will need backtracking !!


