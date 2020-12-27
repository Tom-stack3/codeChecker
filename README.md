# codeChecker
Code checker is a python script that you can run on code files and get data on your files.  
It searches for some coding style problems (listed at the end of the file).
In addition to that, it prints data about your code.\
**Currently works only on c and c++ files.**

## data printed in the end:
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

## coding style checked:
* 120 character limit in each row. (comments included)
* can use only one method of indentaion from the following:
  * tabs
  * spaces: 4 spaces each indentaion.
* comments:
  * cannot break one-line comment to more than one line.  
    use block comments instead.
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
//for: 89-110 Introduction to Computer Science, Bar Ilan.
