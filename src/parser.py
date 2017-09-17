# Lexical Analyzer, FortranIV Compiler
# Compiler Course, UTP 2017-2
# hfjimenez@utp.edu.co, kevin_utp24@utp.edu.co
from sly import Parser
from lexer import FortranLexer
'''
NOTES :
    *In order to achieve speed I've stablished section to made my life more easier
    using find, search and replace.

'''


class FortranParser(Parser):
    debugfile = 'parser.out'  # control de depuración

    def __init__(self):
        self.errorStatus = False
    tokens = FortranLexer.tokens
    start = 'program'

    precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),
    )
    '''
    See grammar.txt file for more details
    '''

    '''program Section'''
    @_('program statement')
    def program(self, p):
        pass

    @_('statement')
    def program(self, p):
        pass

    '''statement Section'''
    @_('INTEGER command')
    def statement(self, p):
        pass

    @_('command')
    def statement(self, p):
        pass

    '''command Section'''
    @_('variable ASSIGN expr')
    def command(self, p):
        pass

    @_('GOTO INTEGER')
    def command(self, p):
        pass

    @_('GOTO ID')
    def command(self, p):
        pass

    @_('GOTO LPAREN intlist RPAREN "," variable')
    def command(self, p):
        pass

    @_('IF LPAREN relexpr RPAREN INTEGER "," INTEGER "," INTEGER')
    def command(self, p):
        pass

    @_('DO INTEGER variable ASSIGN INTEGER "," INTEGER "," INTEGER')
    def command(self, p):
        pass

    @_('DO INTEGER variable ASSIGN INTEGER "," INTEGER')
    def command(self, p):
        pass

    @_('CONTINUE')
    def command(self, p):
        pass

    @_('PAUSE')
    def command(self, p):
        pass

    @_('PAUSE INTEGER')
    def command(self, p):
        pass

    @_('STOP')
    def command(self, p):
        pass

    @_('STOP INTEGER')
    def command(self, p):
        pass

    @_('RETURN')
    def command(self, p):
        pass

    @_('END')
    def command(self, p):
        pass

    @_('CALL ID LPAREN paramlist RPAREN')
    def command(self, p):
        pass

    @_('READ LPAREN optionsIO RPAREN varlist')
    def command(self, p):
        pass

    @_('READ LPAREN optionsIO RPAREN')
    def command(self, p):
        pass

    @_('WRITE LPAREN optionsIO RPAREN varlist')
    def command(self, p):
        pass

    @_('END FILE INTEGER')
    def command(self, p):
        pass

    @_('END FILE ID')
    def command(self, p):
        pass

    @_('INTEGER FORMAT LPAREN formatOptions RPAREN')
    def command(self, p):
        pass

    @_('INTEGER exprlist')
    def command(self, p):
        pass

    @_('REAL exprlist')
    def command(self, p):
        pass

    @_('DIMMENSION dimmensionOptions')
    def command(self, p):
        pass

    @_('DATA dataOptions')
    def command(self, p):
        pass

    @_('FUNCTION ID LPAREN varlist RPAREN')
    def command(self, p):
        pass

    @_('SUBROUTINE ID LPAREN varlist RPAREN')
    def command(self, p):
        pass

    '''expr Section'''
    @_('expr PLUS expr')
    def expr(self, p):
        pass

    @_('expr MINUS expr')
    def expr(self, p):
        pass

    @_('expr TIMES expr')
    def expr(self, p):
        pass

    @_('expr DIVIDE expr')
    def expr(self, p):
        pass

    @_('expr EXPONENT expr')
    def expr(self, p):
        pass

    '''
    @_('expr DS  expr')
    def expr(self, p):
        pass
    '''

    @_('MINUS expr')
    def expr(self, p):
        pass

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        pass

    @_('INTEGER')
    def expr(self, p):
        pass

    @_('REAL')
    def expr(self, p):
        pass

    @_('variable')
    def expr(self, p):
        pass

    '''  exprlist Section'''
    @_('exprlist "," expr')
    def exprlist(self, p):
        pass

    @_('expr')
    def exprlist(self, p):
        pass

    '''  relexpr Section'''
    @_('expr LT expr')
    def relexpr(self, p):
        pass

    @_('expr LE expr')
    def relexpr(self, p):
        pass

    @_('expr GT expr')
    def relexpr(self, p):
        pass

    @_('expr GE expr')
    def relexpr(self, p):
        pass

    @_('expr EQ expr')
    def relexpr(self, p):
        pass

    @_('expr NE expr')
    def relexpr(self, p):
        pass

    @_('relexpr AND relexpr')
    def relexpr(self, p):
        pass

    @_('relexpr OR  relexpr')
    def relexpr(self, p):
        pass

    @_('NOT relexpr')
    def relexpr(self, p):
        pass

    '''  variable Section'''
    @_('ID LPAREN expr "," expr RPAREN')
    def variable(self, p):
        pass

    @_('ID LPAREN expr RPAREN')
    def variable(self, p):
        pass

    @_('ID')
    def variable(self, p):
        pass

    '''  varlist Section'''
    @_(' varlist "," variable')
    def varlist(self, p):
        pass

    @_('variable')
    def varlist(self, p):
        pass

    '''  paramlist Section'''
    @_('ID "," paramlist')
    def paramlist(self, p):
        pass

    @_('ID')
    def paramlist(self, p):
        pass

    '''  number Section'''
    @_('INTEGER')
    def number(self, p):
        pass

    @_('REAL')
    def number(self, p):
        pass

    @_('MINUS INTEGER')
    def number(self, p):
        pass

    @_('MINUS REAL')
    def number(self, p):
        pass

    '''  numlist Section'''
    @_('numlist "," number')
    def numlist(self, p):
        pass

    @_('number')
    def numlist(self, p):
        pass

    '''  intlist Section'''
    @_('intlist "," INTEGER')
    def intlist(self, p):
        pass

    @_('INTEGER')
    def intlist(self, p):
        pass

    '''  optionsIO Section'''
    @_('INTEGER "," INTEGER')
    def optionsIO(self, p):
        pass

    @_('INTEGER "\'" INTEGER')
    def optionsIO(self, p):
        pass

    @_('ID "," INTEGER')
    def optionsIO(self, p):
        pass

    @_('ID "\'" INTEGER')
    def optionsIO(self, p):
        pass

    @_('INTEGER "," "*"')
    def optionsIO(self, p):
        pass

    @_('INTEGER "\'" "*"')
    def optionsIO(self, p):
        pass

    
    # revisar
    ''' formatOptions Section '''
    @_('formatOptions "," formatOptions')
    def formatOptions(self, p):
        pass

    @_('formatOptions "/" formatOptions')
    def formatOptions(self, p):
        pass

    @_('LPAREN formatOptions RPAREN')
    def formatOptions(self, p):
        pass

    @_('INTEGER conversion')
    def formatOptions(self, p):
        pass

    @_('conversion')
    def formatOptions(self, p):
        pass

    @_('string')
    def formatOptions(self, p):
        pass

    @_('empty')
    def formatOptions(self, p):
        pass

    # conversion Section
    @_('LPAREN conversion RPAREN')
    def conversion(self, p):
        pass

    @_('conversion "," typeconversion')
    def conversion(self, p):
        pass

    @_('typeconversion')
    def conversion(self, p):
        pass

    # typeconversion Section
    @_('INTEGER ID')
    def typeconversion(self, p):
        pass

    @_('ID INTEGER "." INTEGER')
    def typeconversion(self, p):
        pass

    @_('ID INTEGER')
    def typeconversion(self, p):
        pass

    @_('ID string')
    def typeconversion(self, p):
        pass
    ''' end formatOptions Section'''

    '''  dimmensionOptions Section'''
    @_('dimmensionOptions "," ID LPAREN intlist RPAREN')
    def dimmensionOptions(self, p):
        pass

    @_('ID LPAREN intlist RPAREN')
    def dimmensionOptions(self, p):
        pass
    
    '''  dataOptions Section'''
    @_('varlist "/" datalist "/" "," dataOptions')
    def dataOptions(self, p):
        pass

    @_('varlist "/" datalist "/"')
    def dataOptions(self, p):
        pass
    
    #revisar
    '''  datalist Section'''
    @_('datalist "," INTEGER "*" number')
    def datalist(self, p):
        pass

    @_('datalist "," number')
    def datalist(self, p):
        pass

    @_('INTEGER "*" number')
    def datalist(self, p):
        pass

    @_('number')
    def datalist(self, p):
        pass
    '''  datalist Section'''

    def error(self, p):
        '''
        #Trigger the  error if there is 
        '''
        print("There was an Error Reading the Grammar!.")
        if not p:
            print("End of File!")
            return
