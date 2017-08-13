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
                'GO TO',
                'IF','INTEGER',
                'PROGRAM',
                'READ','REAL', 'RETURN', 
                'SUBROUTINE', 
                'THEN', 'TRUE',
                }

    logical = { 'MAYOR', 'MAYOROIGUAL',
                'MENOR', 'MENOROIGUAL',
                'IGUAL', 'DIFERENTE',
                'NOT', 'AND', 'OR'
                }

    # Set of token names.   This is always required
    tokens = {
        'ID',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'ASSIGN',
        'LPAREN',
        'RPAREN',
        *reserved,          #Extend the actual tokens
        *logical
        }

    # String containing ignored characters between tokens
    ignore = ' \t'
    # Set of valid characters
    literals = { '+', '-', '*', '/', '=', '(', ')', '.', ','}

    # Regular expression rules for tokens.
    # The idea is to match all the coincidences based on gordon-cs.
    ID      = r'[a-zA-Z_][a-zA-Z0-9_]*'
    REAL = r'[+-]?([\d]+\.[\d]*|[\d]*\.[0-9]+)?([eE][+-]?[\d]+)?'
    INTEGER  = r'[+-]?[\d]+'
    CMPLX = r'CMPLX\([+-]?([+-]?[\d]*([eE]?[\d]*)|[+-]?[\d]*.[\d]+)\,[+-]?([+-]?[\d]*([eE]?[\d]*)|[+-]?[\d]*.[\d]+)\xxx)'
    PLUS    = r'\+'
    MINUS   = r'-'
    TIMES   = r'\*'
    DIVIDE  = r'/'
    ASSIGN  = r'='
    LPAREN  = r'\('
    RPAREN  = r'\)'
 
    #Triggered action 
    #if the action is triggered you won't need the above expression, or I guess.
    def ID(self, t):
    if t.value in reserved:
         t.type = t.value.upper()
    return t

    @_(r'[+-]?([\d]+\.[\d]*|[\d]*\.[0-9]+)?([eE][+-]?[\d]+)?')
    def REAL(self, t):
    t.value = float(t.value)   # Convert to a numeric value
    return t

    @_(r'\d+')
    def INTEGER(self, t):
    t.value = int(t.value)   # Convert to a numeric value
    return t

if __name__ == '__main__':
    data = 'x = 3 + 42 * (s - t)'
    lexer = CalcLexer()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))