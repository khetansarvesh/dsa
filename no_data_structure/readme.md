There is a proof which shows that any problem can be solved via both iterative approach and recursive approach. But in some problems its easiler to think the iterative approach while in some problem it is easier to think the recursive approach !!

# $\color{cyan}{1.\ Iterative\}$
Use in those questions wherein we DONT need to find all possible cases.



<br><br><br>
<br><br><br>



# $\color{cyan}{2.\ Recursive\}$
Use in those questions wherein we need to find all possible cases.


## $\color{red}{2.1\ Recursion}$

- <ins> 1 Recursive Tree </ins> : 
these questions are just for learning and ideally iterative approach is the preferred solution here. Hence you might not find here questions wherein you need to deal with all possible cases and so its okay if you dont think of solving such questions using recurssion.
    - [Natural Decomposition Based Questions (leap of faith approach)](https://skhetan.substack.com/p/single-tree-recursion-toy-problems)

- <ins> 2 Recursive Tree </ins> : 
here you will find questions wherein you need to deal with all possible cases hence you should think of recursion to solve it.
    - [Natural Decomposition Based Questions (leap of faith approach)](https://skhetan.substack.com/p/two-way-recursion?open=false#%C2%A7controlled-recursion)
    - [Choice Based Decomposition Questions (leap of faith approach)](https://skhetan.substack.com/p/two-way-recursion-choices)


- <ins> >2 Recursive Tree </ins> : 
here you will find questions wherein you need to deal with all possible cases hence you should think of recursion to solve it.
    - Natural Decomposition Based Questions (leap of faith approach)
    - [Choice Based Decomposition Questions (leap of faith approach)](https://skhetan.substack.com/p/k-way-recursion-choices)

- Variable Size Recursive Tree

Now in all the above problem we broke a bigger problem into a smaller problem (top-down approach) and solved it using recurssion. But there is this special 'rare' problem ([Tower Of Hanoi](https://skhetan.substack.com/p/tower-of-hanoi)) wherein we go from a smaller problem to a larger problem (bottom - up approach).


Refer this [pdf](https://github.com/khetansarvesh/dsa/blob/main/no_data_structure/recursive_time_complexity.pdf) to learn how to calculate time complexity for recursive algorithms.


## $\color{red}{2.2\ Dynamic\ Programming\ (DP)}$
Note that all the above recursive algorithm can be improved using [Dynamic Programming (DP)](https://skhetan.substack.com/p/dynamic-programming-dp) where there are overlapping subproblems !! It helps reduce exponential time complexity (eg 2^N) to polynomial time complexity (eg N^2)
