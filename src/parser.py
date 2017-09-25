''' Parser, FortranIV Compiler
 Compiler Course, UTP 2017-2
 hfjimenez@utp.edu.co, kevin_utp24@utp.edu.co
'''
from sly import Parser
from lexer import *
from util import *
import sys
import os.path


class FortranParser(Parser):
    # Depuracion
    debugfile = '../debug/Parser.out'
    # def __init__(self):
    #    self.errorStatus = False
    tokens = FortranLexer.tokens
    start = 'program'  # start symbol

    precedence = (
        ('nonassoc', 'LT', 'GT', 'LE', 'GE', 'EQ', 'NE'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),
        ('left', 'EXPONENT'),
        ('left', '/', '*'),
        ('right', 'UMINUS'),
        ('right', 'UNOT'),
        ('left', 'AND', 'OR'),
        ('left', ','),
        ('left', 'RPAREN'),
    )

    '''
    See ../SyntaxParser/grammar.txt file for more details
    '''

    '''program Section'''
    @_('program statement')
    def program(self, p):
        pass

    @_('statement')
    def program(self, p):
        pass

    '''statement Section'''
    @_('INT command')
    def statement(self, p):
        pass

    @_('command')
    def statement(self, p):
        pass

    '''command Section'''
    @_('variable ASSIGN expr')
    def command(self, p):
        pass

    @_('CALL callOption')
    def command(self, p):
        pass

    @_('CONTINUE')
    def command(self, p):
        pass

    @_('DATA dataOption')
    def command(self, p):
        pass

    @_('DIMMENSION dimmensionOption')
    def command(self, p):
        pass

    @_('DO doOption')
    def command(self, p):
        pass

    @_('END')
    def command(self, p):
        pass

    @_('FORMAT LPAREN formatOption RPAREN')
    def command(self, p):
        pass

    @_('FUNCTION ID LPAREN varlist RPAREN')
    def command(self, p):
        pass

    @_('GOTO gotoOption')
    def command(self, p):
        pass

    @_('IF LPAREN relexpr RPAREN ifOption')
    def command(self, p):
        pass

    @_('INTEGER exprlist')
    def command(self, p):
        pass

    @_('PAUSE pauseOption')
    def command(self, p):
        pass

    @_('REAL exprlist')
    def command(self, p):
        pass

    @_('READ readOption')
    def command(self, p):
        pass

    @_('RETURN')
    def command(self, p):
        pass

    @_('STOP stopOption')
    def command(self, p):
        pass

    @_('SUBROUTINE ID LPAREN varlist RPAREN')
    def command(self, p):
        pass

    @_('WRITE LPAREN optionsIO RPAREN varlist')
    def command(self, p):
        pass

    ''' variable Section '''
    @_('ID LPAREN expr "," expr RPAREN')
    def variable(self, p):
        pass

    @_('ID LPAREN expr RPAREN')
    def variable(self, p):
        pass

    @_('ID')
    def variable(self, p):
        pass

    '''  varlist Section '''
    @_('varlist "," variable')
    def varlist(self, p):
        pass

    @_('variable')
    def varlist(self, p):
        pass

    '''  number Section  '''
    @_('INT')
    def number(self, p):
        pass

    @_('RREAL')
    def number(self, p):
        pass

    @_('MINUS INT %prec UMINUS')
    def number(self, p):
        pass

    @_('MINUS RREAL %prec UMINUS')
    def number(self, p):
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

    @_('MINUS expr %prec UMINUS')
    def expr(self, p):
        pass

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        pass

    @_('INT')
    def expr(self, p):
        pass

    @_('RREAL')
    def expr(self, p):
        pass

    @_('variable')
    def expr(self, p):
        pass

    ''' exprlist Section '''
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

    @_('NOT relexpr %prec UNOT')
    def relexpr(self, p):
        pass

    ''' callOption Section  '''
    @_('ID LPAREN idList RPAREN')
    def callOption(self, p):
        pass

    @_('EXIT callExit')
    def callOption(self, p):
        pass

    ''' callExit Section  '''
    @_('LPAREN INT RPAREN')
    def callExit(self, p):
        pass

    @_('empty')
    def callExit(self, p):
        pass

    '''  idList Section  '''
    @_('idList "," ID')
    def idList(self, p):
        pass

    @_('ID')
    def idList(self, p):
        pass

    ''' dataOptions Section  '''
    @_('dataOption "," varlist "/" datalist "/"')
    def dataOption(self, p):
        pass

    @_('varlist "/" datalist "/"')
    def dataOption(self, p):
        pass

    '''  datalist Section  '''
    @_('datalist "," INT "*" number')
    def datalist(self, p):
        pass

    @_('datalist "," number')
    def datalist(self, p):
        pass

    @_('INT "*" number')
    def datalist(self, p):
        pass

    @_('number')
    def datalist(self, p):
        pass

    '''  dimmensionOption Section  '''
    @_('dimmensionOption "," ID LPAREN intlist RPAREN')
    def dimmensionOption(self, p):
        pass

    @_('ID LPAREN intlist RPAREN')
    def dimmensionOption(self, p):
        pass

    '''  intlist Section'''
    @_('intlist "," INT')
    def intlist(self, p):
        pass

    @_('INT')
    def intlist(self, p):
        pass

    ''' doOption Section '''
    @_('INT variable ASSIGN INT "," INT "," INT')
    def doOption(self, p):
        pass

    @_('INT variable ASSIGN INT "," INT')
    def doOption(self, p):
        pass

    ''' formatOption Section '''
    @_('formatOption "," formatOption')
    def formatOption(self, p):
        pass

    @_('formatOption "/" formatOption')
    def formatOption(self, p):
        pass

    @_('INT LPAREN formatOption RPAREN')
    def formatOption(self, p):
        pass

    @_('LPAREN formatOption RPAREN')
    def formatOption(self, p):
        pass

    @_('conversion')
    def formatOption(self, p):
        pass

    @_('string')
    def formatOption(self, p):
        pass

    @_('empty')
    def formatOption(self, p):
        pass

    ''' conversion Section '''
    @_('INT ID')
    def conversion(self, p):
        pass

    @_('ID INT "." INT')
    def conversion(self, p):
        pass

    @_('ID INT')
    def conversion(self, p):
        pass

    @_('ID string')
    def conversion(self, p):
        pass

    ''' string Section '''
    @_('STRING')
    def string(self, p):
        pass

    @_('HSTRING')
    def string(self, p):
        pass

    ''' gotoOption Section '''
    @_('INT')
    def gotoOption(self, p):
        pass

    @_('ID')
    def gotoOption(self, p):
        pass

    @_('LPAREN intlist RPAREN "," variable')
    def gotoOption(self, p):
        pass

    ''' ifOption Section '''
    @_('ifValue "," ifValue "," ifValue')
    def ifOption(self, p):
        pass

    @_('INT')
    def ifValue(self, p):
        pass

    @_('ID')
    def ifValue(self, p):
        pass

    ''' pauseOption Section'''
    @_('INT')
    def pauseOption(self, p):
        pass

    @_('empty')  # error shift/reduce
    def pauseOption(self, p):
        pass

    ''' stopOption Section '''
    @_('INT')
    def stopOption(self, p):
        pass

    @_('empty')  # error shift/reduce
    def stopOption(self, p):
        pass

    ''' readOption Section '''
    @_('LPAREN optionsIO RPAREN varlist')
    def readOption(self, p):
        pass

    @_('LPAREN optionsIO RPAREN empty')  # error shift/reduce
    def readOption(self, p):
        pass

    '''  optionsIO Section'''
    @_('INT "," INT')
    def optionsIO(self, p):
        pass

    @_('INT "\'" INT')
    def optionsIO(self, p):
        pass

    @_('ID "," INT')
    def optionsIO(self, p):
        pass

    @_('ID "\'" INT')
    def optionsIO(self, p):
        pass

    @_('INT "," "*"')
    def optionsIO(self, p):
        pass

    @_('INT "\'" "*"')
    def optionsIO(self, p):
        pass

    @_('')  # empty
    def empty(self, p):
        pass

    def error(self, p):
        # Trigger the  error if there is
        print("There was an Error Reading the Grammar!.")
        print("{}info>> {}{}".format(yellow,p,reset))
        if not p:
            print("{} End of File!".format(warning))
            return

        '''while True:
            tok = next(self.tokens, None)
            if not tok or tok.type == 'RPAREN':
                break
            self.restart()
        elif p:
            print("{}Syntax error at token {}".format(warning, p.type))
            # Just discard the token and tell the parser it's okay.
            tok = next(self.tokens, None)
        else:
            print("{}Syntax error at EOF".format(warning))'''
