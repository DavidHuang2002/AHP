# Understanding AHP

![Understanding%20AHP%2070eef49c33084b9297c530754b573216/Untitled.png](Understanding%20AHP%2070eef49c33084b9297c530754b573216/Untitled.png)

## Overall idea

- Think of the hierarchy as a **recursive process.**
    - For example, for the hierarchy in the above picture, it can be seen as a order 2 tree, consists of 4 order 1 subtree (Ex: Factor A along with Choices XYZ can be viewed as order 1 tree )
    - For each factor on level 1, it can be seen as the goal of a subtree. Treating it as a goal, you can compute the relative importance(weight) of each choice relative to that factor.
        - For each subtree, repeat the recursive process to compute the weight of each choice
    - Then, you can compute the priority vector for level 1 as a level, which gives you the relative importance between the factors in that level
    - To get the final priority between choices, you simply calculate the weighted average of each choice's importance across the factors, namely
        - Weight of choice X = weight of choice X for factor A*weight of factor A + weight of choice X for factor B*weight of factor B + ......
        - It's best represented by matrix multiplication $\vec{W}=(\vec{W_A}, \vec{W_B},...) \cdot \vec{W_{level1}}$

## Comparison matrix

- make paired comparison between every two choices/factors with this scale (even numbers are in between)

![Understanding%20AHP%2070eef49c33084b9297c530754b573216/Screen_Shot_2021-07-03_at_10.25.09_PM.png](Understanding%20AHP%2070eef49c33084b9297c530754b573216/Screen_Shot_2021-07-03_at_10.25.09_PM.png)

- now for paired comparisons, you can make a reciprocal matrix
- For example, if john prefers banana to apple for score of 3, apple to cherry for 5, banana to cherry for 7, then the matrix looks like this

![Understanding%20AHP%2070eef49c33084b9297c530754b573216/Untitled%201.png](Understanding%20AHP%2070eef49c33084b9297c530754b573216/Untitled%201.png)

where if you prefer a to b for score of x, you prefer b to a with 1/x

### Priority Vector

- Priority vector of a comparison matrix is the normalized principal eigenvector of that matrix (?Question, here the normalize means that all terms sum to one, not the square of all terms sum to one?)
    - principal eigenvec is the eigenvec that corresponds to the largest eigenval
    - to normalize(?) it, you simply make sure that all terms sum to 1
- A easy way to approximate (for small size comparison matrix with n≤3)
    - Divide each element with the sum of its column to get the normalized relative weight
    - The normalized eigenvec will simply be the vector with the average of each row

### Consistency

-