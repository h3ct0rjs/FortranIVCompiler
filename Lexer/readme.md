# Lexical Analyzer 

This is the Lexical Analyzer for our *mini**Fortran***,we base all our research in the 1330/1800 Ibm Manual, 
we try to keep this code as simple as possible and used the minimun python tricks, 
we just use the small trick for unpacking sets. 

We use the Sly tutorial in order to implement this code. 

    '''
    Lexical Analyzer for our miniFortranIV(Formula Translation 1130/1800)
    compiler, the elements identified for the Fortran Language in the documents
    are :
     -constants
     -variables
     -arrays
     -arithmetic operators
     -statements

     Fortran statements are written in a line of width 80 maximun,
     for our Fortran Compiler we use as follow :
        1..5: min range 1, max range 99999
        6:must be zero or blank
        7-72: your statements
        73-80: not used
    Notes:
    *Comments start with cC.
    REAL: With maximun 15 digits after the period
    GO TO:
        GO TO Number label: Goto to the line
        GO TO (nl1, nl2, nl3), i where i indicate where label to jump.
    IF :
        IF expr, nl1,nl2,nl3
    '''

## Running Code

You will need to have **python3.6** and sly library, we've created a bash script to automate this:

```sh
user@host:~$ git clone  https://github.com/h3ct0rjs/FortranIVCompiler
user@host:~$ cd FortranIVCompiler/Lexer/
user@host:~$ ./run.sh
```



## contact details

*hfjimenez@utp.edu.co, kevin_utp24@utp.edu.co*
