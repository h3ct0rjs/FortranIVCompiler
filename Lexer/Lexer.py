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
    reserved_words = {'CALL', 'COMMON', 'CONTINUE',           #'CALL_LINK',
                'DATA', 'DIMMENSION', 'DO', 'DP',
                'END', 'ELSE', 'EQ', 'EQUIVALENCE',
                'FALSE', 'FIND', 'FORMAT', 'FUNCTION',
                'GOTO',
                'IF', 'INTEGER',
                'PROGRAM', 'PAUSE',
                'READ', 'REAL', 'RETURN', 'REWIND',
                'SUBROUTINE','STOP',
                'THEN', 'TRUE',
                'LOGICVALUE', 'LOGICOPERATOR', 'COMPARATOR'
                }

    others = {'EQ',
              'GT',
              'LE',
              'LT',
              'GE',
              'NE'
              }

    logicaloperator = {'NOT',
                       'AND',
                       'OR'
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
        *reserved_words,  # Extend the actual tokens
        *logicaloperator,
        *others,
    }

    # String containing ignored characters between tokens
    ignore = ' \t\r'
    # Lines star1ting with C or c will be
    ignore_comment = r'^[cC]{1}\s[a-zA-Z\d ]*'
    # Set of valid characters
    literals = {'+', '-', '*', '/', '=', '(', ')', '.', ','}

    # Regular expression rules for tokens.
    # The idea is to match all the coincidences based on 1130/1800 ibm manual.
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    REAL = r'[-+]?(([\d]+\.[\d]*|[\d]*\.[\d]+)([eE][-+]?[\d]+)?|[\d]+[eE][-+]?[\d]+)'
    INTEGER = r'[+-]?[\d]+'
    #HEXA = r'[zZ][0-9a-fA-F]+'
    #CMPLX = r'CMPLX\([-+]?(\d|[\d](([\d]*\.?)|([\d]*\.[\d]*))([dD][-+]?[\d]{1,2})|(([\d]+\.[\d]*|[\d]*\.[\d]+)([eE][-+]?[\d]+)?|[\d]+[eE][-+]?[\d]+))\,[-+]?(\d|[\d](([\d]*\.?)|([\d]*\.[\d]*))([dD][-+]?[\d]{1,2})|(([\d]+\.[\d]*|[\d]*\.[\d]+)([eE][-+]?[\d]+)?|[\d]+[eE][-+]?[\d]+))\)'
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    EXPONENT = r'\*\*'
    DIVIDE = r'/'
    ASSIGN = r'='
    LPAREN = r'\('
    RPAREN = r'\)'

    TRUE = r'\.TRUE\.',
    FALSE = r'\.FALSE\.',

    NOT=r'\.NOT\.'
    AND=r'\.AND\.'  
    OR=r'\.OR\.'
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
    @_(r'^[cC]{1}\s[a-zA-Z\d ]*')
    def t_comment(self, t):
        pass

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    @_(r'[a-zA-Z_][a-zA-Z0-9_]*')
    def ID(self, t):
        if t.value in self.reserved_words:
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

    '''
    @_(r'CMPLX\([-+]?(\d|[\d](([\d]*\.?)|([\d]*\.[\d]*))([dD][-+]?[\d]{1,2})|(([\d]+\.[\d]*|[\d]*\.[\d]+)([eE][-+]?[\d]+)?|[\d]+[eE][-+]?[\d]+))\,[-+]?(\d|[\d](([\d]*\.?)|([\d]*\.[\d]*))([dD][-+]?[\d]{1,2})|(([\d]+\.[\d]*|[\d]*\.[\d]+)([eE][-+]?[\d]+)?|[\d]+[eE][-+]?[\d]+))\)')
    def CMPLX(self, t):
        t.value = complex(t.value[0], t.value[1]j)
        return t
        '''

    @_(r"DOUBLE PRECISION")
    def DP(self, t):
        t.value = dp(t.value)
        return t
    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, value):
        print('Line %d: Bad character %r' % (self.lineno, value[0]))
        self.index += 1

    def test(self, data):
        """
        Unitary test
        """
        for tok in lexer.tokenize(data):
            print('type={}, value={}'.format(tok.type, tok.value))
        print("DONE")


if __name__ == '__main__':
    sys.argv.append('datasets/integers.fiv')    #Change this line for your dataset
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: %s filename\n" % sys.argv[0])
        raise SystemExit(1)
    lexer = FortranLexer()
    lexer.test(open(sys.argv[1]).read())