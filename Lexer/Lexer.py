# Lexical Analyzer, FortranIV Compiler
# Compiler Course, UTP 2017-2
# hfjimenez@utp.edu.co, kevin_utp24@utp.edu.co
from sly import Lexer
from sys import stdin, stdout


class FortranLexer(Lexer):
    '''
    Class Lexical Analyzer, FortranIV
    supported methods:

    supported attributes:

    '''
    # We inherit from Lexer
    # Reserved Keywords based on
    # http://www.math-cs.gordon.edu/courses/cs323/FORTRAN/fortran.html
    reserved = {'CALL', 'COMMON', 'CMPLX', 'CONTINUE',
                'DATA', 'DIMMENSION', 'DO', 'DOUBLE PRECCISION',
                'END', 'ELSE', 'EQ', 'EQUIVALENCE',
                'FIND', 'FORMAT', 'FUNCTION',
                'GO TO',
                'IF', 'INTEGER',
                'PROGRAM',
                'READ', 'REAL', 'RETURN', 'REWIND',
                'SUBROUTINE',
                'THEN'
                }

    logical = {'.TRUE', '.FALSE',
               '.NOT', '.AND', '.OR'
               }
    comparison = {'.GT.'
                  '.GE.'
                  '.LT.'
                  '.LE.'
                  '.EQ.'
                  '.NE.'
                  }
    # Set of token names.   This is always required
    tokens = {
        'ID',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'EXPONENT',
        'ASSIGN',
        'LPAREN',
        'RPAREN',
        *reserved,  # Extend the actual tokens
        *logical,
        *comparison
    }

    # String containing ignored characters between tokens
    ignore = ' \t'
    # Lines starting with C or c will be
    ignore_comment = r'^[cC]{1}\s[a-zA-Z\d ]*'

    # Set of valid characters
    literals = {'+', '-', '*', '/', '=', '(', ')', '.', ','}

    # Regular expression rules for tokens.
    # The idea is to match all the coincidences based on gordon-cs.
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    REAL = r'[-+]?(([\d]+\.[\d]*|[\d]*\.[\d]+)([eE][-+]?[\d]+)?|[\d]+[eE][-+]?[\d]+)'
    INTEGER = r'[+-]?[\d]+'
    #HEXA = r'[zZ][0-9a-fA-F]+'
    CMPLX = r'CMPLX\([-+]?(\d|[\d](([\d]*\.?)|([\d]*\.[\d]*))([dD][-+]?[\d]{1,2})|(([\d]+\.[\d]*|[\d]*\.[\d]+)([eE][-+]?[\d]+)?|[\d]+[eE][-+]?[\d]+))\,[-+]?(\d|[\d](([\d]*\.?)|([\d]*\.[\d]*))([dD][-+]?[\d]{1,2})|(([\d]+\.[\d]*|[\d]*\.[\d]+)([eE][-+]?[\d]+)?|[\d]+[eE][-+]?[\d]+))\)'
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    EXPONENT = r'\*\*'
    DIVIDE = r'/'
    ASSIGN = r'='
    LPAREN = r'\('
    RPAREN = r'\)'
    '''EQ      = r'=='
    ASSIGN  = r'='
    LE      = r'<='
    LT      = r'<'
    GE      = r'>='
    GT      = r'>'
    NE      = r'!='''

    # Triggered action
    # if the action is triggered you won't need the above expression, or I
    # guess.
    @_(r'[a-zA-Z_][a-zA-Z0-9_]*')
    def ID(self, t):
        if t.value in reserved:
            t.type = t.value.upper()
        return t

    @_(r'[-+]?(([\d]+\.[\d]*|[\d]*\.[\d]+)([eE][-+]?[\d]+)?|[\d]+[eE][-+]?[\d]+)')
    def REAL(self, t):
        t.value = float(t.value)   # Convert to a numeric value
        return t

    @_(r'[+-]?[\d]+')
    def INTEGER(self, t):
        t.value = int(t.value)   # Convert to a numeric value
        return t

    @_(r'')
    def CMPLX(self, t):
        t.value = complex(t.value[0], t.value[1]j)
        return t

if __name__ == '__main__':
    
    data = 'x = 3 + 42 * (s - t)'
    lexer = CalcLexer()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))
