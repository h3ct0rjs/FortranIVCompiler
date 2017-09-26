# Lexical Analyzer, FortranIV Compiler
# Compiler Course, UTP 2017-2
# hfjimenez@utp.edu.co, kevin_utp24@utp.edu.co
from sly import Lexer
from decimal import Decimal as dp
import util
class FortranLexer(Lexer):
    reserved_words = {'CALL', 'CONTINUE', 'DATA', 'DIMMENSION', 'DO', 'END', 'EXIT',
                      'FORMAT', 'FUNCTION', 'GOTO', 'IF', 'INT', 'INTEGER', 'PAUSE',
                      'READ', 'REAL', 'RREAL', 'RETURN', 'SUBROUTINE', 'STOP', 'WRITE'}
    # DP','FALSE','FILE','FIND', 'ELSE','THEN', 'TRUE', 'PROGRAM'
    others = {'EQ', 'GT', 'LE', 'LT', 'GE', 'NE'}
    logicaloperator = {'NOT', 'AND', 'OR'}
    # Set of token names.
    tokens = {
        'ID',
        #'STRING',
        #'HSTRING',
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

    # Lines starting with C or c will be
    # String containing ignored characters between tokens
    ignore = ' \t\r'
    # Set of valid characters
    literals = {'+', '-', '*', '/', '=', '(', ')', '.', ',', "'"}
    # Regular expression rules for tokens.
    # The idea is to match all the coincidences based on 1130/1800 ibm manual.
    ASSIGN = r'='
    PLUS = r'\+'
    MINUS = r'-'
    EXPONENT = r'\*\*'
    TIMES = r'\*'
    DIVIDE = r'/'
    LPAREN = r'\('
    RPAREN = r'\)'
    NOT = r'\.NOT\.'
    AND = r'\.AND\.'
    OR = r'\.OR\.'
    EQ = r'\.EQ\.'
    GT = r'\.GT\.'
    LE = r'\.LE\.'
    LT = r'\.LT\.'
    GE = r'\.GE\.'
    NE = r'\.NE\.'


    # Triggered actions, First when tokenizer finds a word matching rule
    @_(r'CALL')
    def CALL(self, t):
        if t.value in self.reserved_words:
            t.type = t.value.upper()
        return t
    # ignore comments

    @_(r'(\n[Cc] *.*)| (^[Cc] *.*)')
    def ignore_comment(self, p):
        pass

    @_(r"^C[^a-zA-Z0-9_=]{1}.*")
    def t_comment(self, p):
        pass

    
    @_(r'FORMAT(\s)?\(.*\)')
    def FORMAT(self, t):
        if t.value in self.reserved_words:
            t.type = t.value.upper()
        return t
    
    '''
    @_(r'[\'][^\']*[\']')
    def STRING(self, t):
        if t.value in self.tokens:
            t.type = t.value.upper()
        return t

    @_(r'[1-9]{1,3}[H]([^),]+)')
    def HSTRING(self, t):
        if t.value in self.tokens:
            t.type = t.value.upper()
        return t
    '''   
    @_(r'(GOTO|GO\sTO)')
    def GOTO(self, t):
        if t.value in self.reserved_words:
            t.type = t.value.upper()
        return t
    @_(r'[a-zA-Z_][a-zA-Z0-9_]*')
    def ID(self, t):
        if t.value in self.reserved_words:
            t.type = t.value.upper()
        return t

    @_(r'[-+]?([\d]+\.[\d]*|[\d]*\.[\d]+)([eE][-+]?[\d]+)?|[\d]+[eE][-+]?[\d]+')
    def RREAL(self, t):
        t.value = float(t.value)   # Convert to a numeric value
        return t

    @_(r'[+-]?[\d]+')
    def INT(self, t):
        t.value = int(t.value)   # Convert to a numeric value
        return t
    

    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    # Triggers the error
    def error(self, value):
        print('{} Line {}: Bad character {}'.format(warning, self.lineno, value[0]))
        self.index += 1
