# Lexical Analyzer, FortranIV Compiler
# Compiler Course, UTP 2017-2
# hfjimenez@utp.edu.co, kevin_utp24@utp.edu.co
# Lexical Analyzer, FortranIV Compiler
# Compiler Course, UTP 2017-2
# hfjimenez@utp.edu.co, kevin_utp24@utp.edu.co
from sly import Lexer
import sys
from decimal import Decimal as dp
# We inherit from Lexer
# Reserved Keywords based on
class FortranLexer(Lexer):
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
    reserved_words = {'CALL', 'CONTINUE', 'DATA', 'DIMMENSION', 'DO', 'DP', 'END', 'ELSE', 'FALSE', 'FIND', 'FORMAT',
                      'FUNCTION', 'GOTO', 'IF', 'INTEGER', 'PROGRAM', 'PAUSE', 'READ', 'REAL', 'RETURN', 'SUBROUTINE', 'STOP', 'THEN', 'TRUE'}
    others = {'EQ', 'GT', 'LE', 'LT', 'GE', 'NE'}
    logicaloperator = {'NOT', 'AND', 'OR'}
    # Set of token names.
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
        *reserved_words,  # Extend the actual tokens
        *logicaloperator,
        *others,
    }
    # Lines star1ting with C or c will be
    # String containing ignored characters between tokens
    ignore = ' \t\r'
    # Set of valid characters
    literals = {'+', '-', '*', '/', '=', '(', ')', '.', ','}
    # Regular expression rules for tokens.
    # The idea is to match all the coincidences based on 1130/1800 ibm manual.
    #HEXA = r'(0[xX])?[0-9a-fA-F]+'
    # Ignores
    #ignore_comment = r'^C.*'
    PLUS = r'\+'
    MINUS = r'-'
    EXPONENT = r'\*\*'
    TIMES = r'\*'
    DIVIDE = r'/'
    ASSIGN = r'='
    LPAREN = r'\('
    RPAREN = r'\)'
    TRUE = r'\.TRUE\.',
    FALSE = r'\.FALSE\.',
    NOT = r'\.NOT\.'
    AND = r'\.AND\.'
    OR = r'\.OR\.'
    EQ = r'\.EQ\.'
    GT = r'\.GT\.'
    LE = r'\.LE\.'
    LT = r'\.LT\.'
    GE = r'\.GE\.'
    NE = r'\.NE\.'
    DP = r'DOUBLE\sPRECISION'
    # Triggered action
    # if the action is triggered you won't need the above expression, or I
    # guess.
    # Ignore sNew Lines
    @_(r'CALL')
    def CALL(self, t):
        if t.value in self.reserved_words:
            t.type = t.value.upper()
        return t 
    
    @_(r'(\n[Cc] *.*)| (^[Cc] *.*)')
    #@_(r"[cC] *.*")
    def ignore_comment(self, p):
        pass

    @_(r"^C[^a-zA-Z0-9_=]{1}.*")
    def t_comment(self, p):
        pass

    @_(r'[a-zA-Z_][a-zA-Z0-9_]*')
    def ID(self, t):
        if t.value in self.reserved_words:
            t.type = t.value.upper()
        return t

    @_(r'[-+]?([\d]+\.[\d]*|[\d]*\.[\d]+)([eE][-+]?[\d]+)?|[\d]+[eE][-+]?[\d]+')
    def REAL(self, t):
        t.value = float(t.value)   # Convert to a numeric value
        return t

    @_(r'[+-]?[\d]+')
    def INTEGER(self, t):
        t.value = int(t.value)   # Convert to a numeric value
        return t

    # Sets Dp as double precission instance
    @_(r"DOUBLE\sPRECISION")
    def DP(self, t):
        t.value = dp(t.value)
        return t

    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')
    


    # Triggers the error
    def error(self, value):
        print('Line {}: Bad character {}'.format(self.lineno, value[0]))
        self.index += 1

    def test(self, data):
        """
        Unitary test
        """
        for tok in lexer.tokenize(data):
            print('type={} value={}'.format(tok.type, tok.value))
        print("DONE")