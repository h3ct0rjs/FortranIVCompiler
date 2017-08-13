# Lexical Analyzer, FortranIV Compiler
# Compiler Course, UTP 2017-2
# hfjimenez@utp.edu.co, kevin@utp.edu.co
from sly import Lexer

class FortranLexer(Lexer):
    # Reserved Keywords based on http://www.math-cs.gordon.edu/courses/cs323/FORTRAN/fortran.html
    reserved = {'CALL','CMPLX', 'CONTINUE',
                'DATA', 'DIMMENSION', 'DO','DOUBLE PRECCISION',
                'END','EQ',
                'FALSE', 'FORMAT', 'FUNCTION',
                'GO',
                'IF','INTEGER',
                'NE',
                'PROGRAM',
                'READ','REAL', 'RETURN', 
                'SUBROUTINE', 
                'THEN', 'TO', 'TRUE',
                }


    logical = { 'MAYOR', 'MAYOROIGUAL',
                'MENOR', 'MENOROIGUAL',
                'IGUAL', 'DIFERENTE',
                'NOT', 'AND', 'OR'
                }


    # Set of token names.   This is always required
    tokens = {
        'ID',
        'NUMBER',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'ASSIGN',
        'LPAREN',
        'RPAREN',
        *reserved,
        *logical
        }


    # String containing ignored characters between tokens
    ignore = ' \t'
    # Set of valid characters
    literals = { '+', '-', '*', '/', '=', '(', ')', '.', ','}

    # Regular expression rules for tokens
    ID      = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER  = r'\d+'
    PLUS    = r'\+'
    MINUS   = r'-'
    TIMES   = r'\*'
    DIVIDE  = r'/'
    ASSIGN  = r'='
    LPAREN  = r'\('
    RPAREN  = r'\)'

if __name__ == '__main__':
    data = 'x = 3 + 42 * (s - t)'
    lexer = CalcLexer()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))