# Code Checker
Code checker is a python script that you can run on code files and get data on your files.  
It searches for some coding style problems (listed at the end of the file).
In addition to that, it prints data about your code.\
**Currently works only on c and c++ files.**  
  
*Originally made for course 89-110 Introduction to Computer Science, in Bar Ilan University.*

## Data printed in the end:
an example for a data summery looks like the following: 

```c
total number of lines: 545
number of comment lines: 251
number of code lines: 189
number of blank lines: 105
ratio of code/comments =  0.753
percentage of each from the total lines:
 - comments takes 46%
 - code takes 35%
 - blank lines takes 19%
```

## Coding style checked:
* 120 character limit in each row. (comments included)
* Not more than 2 blank lines between code lines.
* **Indentation**:  
  Can use only one method of indentaion from the following:
  * tabs
  * spaces: 4 spaces each indentaion.
* **Comments:**
  * cannot break *one-line comment* to more than one line.  
    Use *block comments* instead!
  * block comments (or multi line comments) shouldn't have any text in line with the opening and closing brackets.  
    :heavy_check_mark: valid:
    ```c
    /*
    comment_here
    */
    ```
    :x: not valid:
    ```c
    /* comment here
    */
    ```
```cmd
-------------------------------------
! WARNING!!
-------------------------------------
! found an empty space line in line:
-------------------------------------
! used less than 4 spaces as an indention in line:8
-------------------------------------
! found too many blank lines consecutively in line:15
-------------------------------------
! file uses both spaces and tabs as indention
-------------------------------------

total number of lines: 18
number of comment lines: 7
number of code lines: 5
number of blank lines: 6
ratio of code/comments =  0.714
percentage of each from the total lines:
 - comments takes 39%
 - code takes 28%
 - blank lines takes 33%
-------------------------------------
```
