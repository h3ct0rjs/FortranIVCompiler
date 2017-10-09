''' Parser, FortranIV Compiler
 Compiler Course, UTP 2017-2
 hfjimenez@utp.edu.co, kevin_utp24@utp.edu.co
'''
from sly import Parser
from lexer import *
from util import *
from astfortran import *
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
        #('left', 'RPAREN'),
    )

    '''
    See ../SyntaxParser/grammar.txt file for more details
    '''
    """
    @validate_fields(statements=list)
    class Program(ATS)
        _fields['statements']
        def append(self, statement):
            self.statements.append(statement)

    """
    '''program Section'''
    @_('program statement')
    def program(self, p):
        p[0].append(p[1])
        return p[0]

    @_('statement')
    def program(self, p):
        return Program([p[0]])

    '''statement Section'''
    @_('INT command')
    def statement(self, p):
        return Statement(p[0], p[1])

    @_('command')
    def statement(self, p):
        return Statement(None, p[0])

    '''command Section'''
    @_('variable ASSIGN expr')
    def command(self, p):
        return Assign(p[0], p[2])

    @_('CALL callOption')
    def command(self, p):
        return CommandCall(p[0])

    @_('CONTINUE')
    def command(self, p):
        return p[0]

    @_('DATA dataOption')
    def command(self, p):
        return CommandData(p[1])

    @_('DIMMENSION dimmensionOption')
    def command(self, p):
        return CommandDimmension(p[1])

    @_('DO doOption')
    def command(self, p):
        return CommandDo(p[1])

    @_('END')
    def command(self, p):
        return p[0]

    @_('FORMAT LPAREN formatOption RPAREN')
    def command(self, p):
        return CommandFormat(p[2])

    @_('FUNCTION ID LPAREN varlist RPAREN')
    def command(self, p):
        return CommandFunction(p[1], p[3])

    @_('GOTO gotoOption')
    def command(self, p):
        return CommandGoTo(p[1])

    @_('IF LPAREN relexpr RPAREN ifOption')
    def command(self, p):
        return CommandIf(p[2], p[4])

    @_('INTEGER exprlist')
    def command(self, p):
        return CommandInteger(p[1])

    @_('PAUSE pauseOption')
    def command(self, p):
        return CommandPause(p[1])

    @_('REAL exprlist')
    def command(self, p):
        return CommandReal(p[1])

    @_('READ readOption')
    def command(self, p):
        return CommandRead(p[1])

    @_('RETURN')
    def command(self, p):
        return p[0]

    @_('STOP stopOption')
    def command(self, p):
        return CommandStop(p[1])

    @_('SUBROUTINE ID LPAREN varlist RPAREN')
    def command(self, p):
        return CommandSubroutine(p[1], p[3])

    @_('WRITE writeOption')
    def command(self, p):
        return CommandWrite(p[1])

    """
    class Idexpresiob(AST):
        _fields=['ID', 'expr', 'expr']
    """
    ''' variable Section '''
    @_('ID LPAREN expr "," expr RPAREN')
    def variable(self, p):
        return Variable(p[0], p[2], p[4])

    @_('ID LPAREN expr RPAREN')
    def variable(self, p):
        return Variable(p[0], p[2], None)

    @_('ID')
    def variable(self, p):
        return Variable(p[0], None, None)

    '''  varlist Section '''
    @_('varlist "," variable')
    def varlist(self, p):
        p[0].append(p[2])
        return p[0]

    @_('variable')
    def varlist(self, p):
        return Varlist([p[0]])

    '''  number Section  '''
    @_('INT')
    def number(self, p):
        return Number(None, p[0], None)

    @_('RREAL')
    def number(self, p):
        return Number(None, None, p[0])

    @_('MINUS INT %prec UMINUS')
    def number(self, p):
        return Number(p[0], p[1], None)

    @_('MINUS RREAL %prec UMINUS')
    def number(self, p):
        return Number(p[0], None, p[1])

    '''expr Section'''
    @_('expr PLUS expr',
       'expr MINUS expr',
       'expr TIMES expr',
       'expr DIVIDE expr',
       'expr EXPONENT expr')
    def expr(self, p):
        return Expr(p[0], p[1], p[2])

    @_('MINUS expr %prec UMINUS')
    def expr(self, p):
        return ExprMinus(p[0], p[1])

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return ExprParen(p[1])

    @_('INT')
    def expr(self, p):
        return ExprSingle(p[0], None, None)

    @_('RREAL')
    def expr(self, p):
        return ExprSingle(None, p[0], None)

    @_('variable')
    def expr(self, p):
        return ExprSingle(None, None, p[0])

    ''' exprlist Section '''
    @_('exprlist "," expr')
    def exprlist(self, p):
        p[0].append(p[2])
        return p[0]

    @_('expr')
    def exprlist(self, p):
        return ExprList([p[0]])

    '''  relexpr Section'''
    @_('expr LT expr',
        'expr LE expr',
        'expr GT expr',
        'expr GE expr',
        'expr EQ expr',
        'expr NE expr'
       )
    def relexpr(self, p):
        return RelExpr(p[0], p[1], p[2])

    @_('relexpr AND relexpr',
        'relexpr OR  relexpr')
    def relexpr(self, p):
        return LogicaRelExpr(p[0], p[1], p[2])

    @_('NOT relexpr %prec UNOT')
    def relexpr(self, p):
        return NotRelExpr(p[0], p[1])

    @_('expr')
    def relexpr(self, p):
        return RelexprSingle(p[0])

    ''' callOption Section  '''
    @_('ID LPAREN idList RPAREN')
    def callOption(self, p):
        return CallOption(p[0], p[2])

    @_('EXIT callExit')
    def callOption(self, p):
        return CallOption(p[1])

    ''' callExit Section  '''
    @_('LPAREN INT RPAREN')
    def callExit(self, p):
        return CallOptionExit(p[1])

    @_('empty')
    def callExit(self, p):
        return None

    '''  idList Section  '''
    @_('idList "," ID')
    def idList(self, p):
        p[0].append(p[2])
        return IdList(p[0])

    @_('ID')
    def idList(self, p):
        return IdList([p[0]])

    ''' dataOptions Section  '''
    @_('dataOption "," varlist "/" datalist "/"')
    def dataOption(self, p):
        p[0].append(p[2], p[4])
        return p[0]

    @_('varlist "/" datalist "/"')
    def dataOption(self, p):
        return DataOption([p[0]], [p[2]])

    ''' ***datalist Section***  '''
    @_('datalist "," INT "*" number')
    def datalist(self, p):
        p[0].append(p[2], p[4])
        return p[0]

    @_('datalist "," number')
    def datalist(self, p):
        p[0].append(None, p[2])
        return p[0]

    @_('INT "*" number')
    def datalist(self, p):
        return DataList([p[0]], [p[2]])

    @_('number')
    def datalist(self, p):
        return DataList([None], [p[0]])

    '''  dimmensionOption Section  '''
    @_('dimmensionOption "," ID LPAREN intlist RPAREN')
    def dimmensionOption(self, p):
        p[0].append(p[2], p[4])
        return p[0]

    @_('ID LPAREN intlist RPAREN')
    def dimmensionOption(self, p):
        return DimmensionOption([p[0]], [p[2]])

    '''  intlist Section'''
    @_('intlist "," INT')
    def intlist(self, p):
        p[0].append(p[2])
        return p[0]

    @_('INT')
    def intlist(self, p):
        return Intlist([p[0]])

    ''' doOption Section '''
    @_('INT variable ASSIGN INT "," INT "," INT')
    def doOption(self, p):
        return DoOption(p[0], p[1], p[3], p[5], p[7])

    @_('INT variable ASSIGN INT "," INT')
    def doOption(self, p):
        return DoOption(p[0], p[1], p[3], p[5], None)

    ''' formatOption Section '''
    @_('formatOption "," CONVERSION',
        'formatOption "/" CONVERSION')
    def formatOption(self, p):
        p[0].append(p[2], None, None, None, None)
        return p[0]
    
    @_('formatOption "," STRING',
        'formatOption "/" STRING')
    def formatOption(self, p):
        p[0].append(None, p[2], None, None, None)
        return p[0]

    @_('formatOption "," HSTRING',
        'formatOption "/" HSTRING')
    def formatOption(self, p):
        p[0].append(None, None, p[2], None, None)
        return p[0]

    @_('formatOption "," INT LPAREN formatOption RPAREN',
        'formatOption "/" INT LPAREN formatOption RPAREN')
    def formatOption(self, p):
        p[0].append(None, None, None, p[2], p[4])
        return p[0]

    @_('CONVERSION')
    def formatOption(self, p):
        return FormatOptList([p[0]], [None], [None], [None], [None])

    @_('STRING')
    def formatOption(self, p):
        return FormatOptList([None], [p[0]], [None], [None], [None])

    @_('HSTRING')
    def formatOption(self, p):
        return FormatOptList([None], [None], [p[0]], [None], [None])

    @_('INT LPAREN formatOption RPAREN')
    def formatOption(self, p):
        return FormatOptList([None], [None], [None], [p[0]], [p[2]])

    @_('DIVIDE formatOption')
    def formatOption(self, p):
        return p[1]

    @_('empty')
    def formatOption(self, p):
        return None

    ''' gotoOption Section '''
    @_('INT')
    def gotoOption(self, p):
        return GotoOptionInt(p[0])

    @_('LPAREN intlist RPAREN "," variable')
    def gotoOption(self, p):
        return GotoOptionIntList(p[1], p[4])

    ''' ifOption Section '''
    @_('INT "," INT "," INT')
    def ifOption(self, p):
        return IfOption(p[0], p[2], p[4])

    ''' pauseOption Section'''
    @_('INT')
    def pauseOption(self, p):
        return PauseOption(p[0])

    @_('empty')  # error shift/reduce
    def pauseOption(self, p):
        return None

    ''' stopOption Section '''
    @_('INT')
    def stopOption(self, p):
        return StopOption(p[0])

    @_('empty')  # error shift/reduce
    def stopOption(self, p):
        return None

    ''' readOption Section '''
    @_('LPAREN optionsIO RPAREN idList')  # error shift/reduce
    def readOption(self, p):
        return WriteRead(p[1], p[3])

    @_('LPAREN optionsIO RPAREN')  # error shift/reduce
    def readOption(self, p):
        return WriteRead(p[1], None)

    ''' writeOption Section '''
    @_('LPAREN optionsIO RPAREN idList')  # error shift/reduce
    def writeOption(self, p):
        return WriteRead(p[1], p[3])

    @_('LPAREN optionsIO RPAREN')  # error shift/reduce
    def writeOption(self, p):
        return WriteRead(p[1], None)

    '''  optionsIO Section'''
    @_('INT "," INT')
    def optionsIO(self, p):
        return OptionsIOInt(p[0], p[2])

    @_('INT')
    def optionsIO(self, p):
        return OptionsIOInt(p[0], None)

    @_('ID "," INT')
    def optionsIO(self, p):
        return OptionsIOID(p[0], p[2])
        
    @_('ID')
    def optionsIO(self, p):
        return OptionsIOID(p[0], None)

    @_('')  # empty
    def empty(self, p):
        pass

    def error(self, p):
        # Trigger the  error if there is
        print("There was an Error Reading the Grammar!.")
        print("{}info>> {}{}".format(yellow, p, reset))
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
