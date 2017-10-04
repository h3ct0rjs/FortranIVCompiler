from util import *
from lexer import FortranLexer
print("{} Shift Reduce Number::".format(warning))
from parser import FortranParser
import sys


def parsex(data):
    lexer = FortranLexer()
    parser = FortranParser()
    return parser.parse(lexer.tokenize(data))


def main():
    sys.argv.append('../datasets/fact.fiv')
    print("{} Opening Fortran Instruction File".format(ok))
    if len(sys.argv) != 2:
        sys.stderr.write('{}usage: {} filename\n'.format(warning, sys.argv[0]))
        raise SystemExit(1)
    else:
        lexer = FortranLexer()

        parser = FortranParser()
        data = open(sys.argv[1]).read()
        # print('{}'.format(data))                   #Debug the tokens
        rtok = []
        print("{} Starting Tokenization Phase..".format(ok))
        for tok in lexer.tokenize(data):
            # print('{}'.format(tok))            #Debug the tokens
            rtok.append(tok)
        print("{} Writing the list of Tokens to the filename:../debug/Tokens.out".format(ok))
        f = open('../debug/Tokens.out', 'w')
        for i in rtok:
            f.write(str(i) + '\n')
        f.close()
        del rtok
        print("{} Tokenization Complete and saved.".format(ok))
        try:
            print("\n{} Starting Parsing phase.".format(ok))
            result = parsex((data))
            print("{} Creating the Abstract Syntax Tree :".format(ok))
            result.pprint()
            print(
                "{} The Parsing Process is Complete and saved in ../debug/Parser.out".format(ok))
            print("{}DONE.".format(ok))
        except EOFError:
            print('{}Bye'.format(ok))

if __name__ == '__main__':
    main()
