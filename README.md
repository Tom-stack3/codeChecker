# Code Checker
---
**Disclaimer from future me**

<sup>07.05.2022</sup>
> I wrote this Python script a long time ago! As I read through these lines of code, I see that they are structured and written pretty poorly, and that the script is a bit buggy and doesn't really work well for regularly formatted files :(\
But it did serve its purpose for checking checkstyle errors at the time and was indeed pretty handy.\
So, I've decided to keep this repo for old times' sake 🙃

---

Code checker is a python script that you can run on code files and get data on your files.  
It searches for some coding style problems (listed at the end of the file).  
In addition to that, it prints data about your code.\
**Currently works only on C, C# and C++ files.**  

* If you don't know how to run python files, read this [Tutorial](https://github.com/Tom-stack3/codeChecker/blob/main/HOW_RUN_EXE.md) to run an .exe file.  
* If you know how to run python scripts, you are more than welcome to download the python script and run it.


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
## Run example:

![run example](https://raw.githubusercontent.com/Tom-stack3/codeChecker/main/images/run_with_warnings%20example.jpg)  
  
  
*Originally made for course "Introduction to Computer Science" 89-110, in Bar Ilan University.*
