# Find-Longest-Path-Brute-Force
## Summary
This program finds and highlights the longest path in a matrix of numbers. The longest path has to be the same number and can be from any direction adjacent to the matrix entry including corners.

<details>
<summary> Input </summary>
This program takes in a csv file of numbers. Numbers may be different. Above are some acceptable csv file examples.

Condition:  
- Every row must have the same amount of numbers
* Must be numbers
+ Letters, symbols, signs, etc. are unacceptable
</details>

<details>
  <summary> Output </summary>
  Longest path is highlighted in the GUI application. If there are 2 longest path, then the one that is found the earliest is highlighted.
  
  | Example 1 | Example 2 | Example 3 | Example 4 |
  | --------- | --------- | --------- | --------- |
  | ![Screen Shot 2023-01-07 at 3 25 24 PM](https://user-images.githubusercontent.com/115419534/211169426-ba24e008-9c2c-4fac-940b-b7d1767f1a9e.png) | ![Screen Shot 2023-01-07 at 3 28 43 PM](https://user-images.githubusercontent.com/115419534/211169431-90bf60ca-7dcd-45cf-a5cb-28b61a28b480.png) | ![Screen Shot 2023-01-07 at 3 29 03 PM](https://user-images.githubusercontent.com/115419534/211169433-6f478410-da0c-45ba-a1b6-1e4c2374e0d5.png) | ![Screen Shot 2023-01-07 at 3 29 19 PM](https://user-images.githubusercontent.com/115419534/211169435-f56d9af0-88ee-45c0-8ba7-9aa878f9b1bd.png) |



</details>

<details>
<summary> Implementation (GUI & Algorithm) </summary>
  <details>
    <summary> GUI </summary>
    This program uses PyQt to generate the GUI. It ultizes the QGridLayout Package to build the matrix. There are 2 GUI's in this complete program: An unsolved matrix and a solved matrix. The unsolved matrix displays the csv file in a matrix-like diagram with a user-interface button called "Solve." The solved matrix displays the same matrix but with the longest path highlighted and it is displayed when the button is clicked.  
    
    
  | Unsolved Matrix | Solved Matrix |
  | --------------- | ------------- |
  | ![Screen Shot 2023-01-07 at 4 03 54 PM](https://user-images.githubusercontent.com/115419534/211171062-3e4771d5-0fb6-49f5-aec4-47f5a3cd39f3.png) | ![Screen Shot 2023-01-07 at 3 25 24 PM](https://user-images.githubusercontent.com/115419534/211171067-5bdaeb2a-784b-49c0-a11b-18ef46f7e32a.png) |
  
  </details>
    
  <details>
    <summary> Algorithm </summary>
    The algoirthm uses a brute-force technique to calculate and find the longest path in the matrix. For every entry of the matrix going top-down and left-right, it calculates every path length and finds the largest among it. By the end of the algorithm, the list of coordinates of the entries of the longest path is obtained.
  </details>
</details>

