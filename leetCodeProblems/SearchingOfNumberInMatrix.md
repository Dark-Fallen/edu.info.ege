# Finding number in the matrix with size N x M
Let we have an matrix with N rows and M columns:
$$
\begin{bmatrix}
a_{11} & a_{12} & a_{13} & \cdots & a_{1m} \\
a_{21} & a_{22} & 2_{23} & \cdots & a_{2m} \\
a_{31} & a_{32} & 2_{33} & \cdots & a_{3m} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & a_{n3} & \cdots & a_{nm}
\end{bmatrix}
$$
With specified filling pattern: each row and column represents an increasing sequence.
Example of specified matrix:
$$
\begin{bmatrix}
1 & 2 & 3 & 4 \\
5 & 6 & 7 & 8 \\
9 & 10 & 11 & 12
\end{bmatrix}
$$
Task: write the function which finds position of specified number K in matrix:
- 1 point - using algorythm with any completing time
- 2 points - using algorythm with completing time lower than $O(n\cdot m)$
- 3 points - using algorythm with completing time lower that $O(m\log{n})$ or $O(n\log{m})$

Example input:
```
1 2 3 4
5 6 7 8

6
```
Output:
```
2 2
```
