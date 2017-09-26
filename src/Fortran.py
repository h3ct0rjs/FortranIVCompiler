from lexer import FortranLexer
from parser import FortranParser
from util import *
import sys

def main():
    sys.argv.append('../datasets/fact.fiv')
    print("{} Opening Fortran inputFile".format(ok))
    if len(sys.argv) != 2:
        sys.stderr.write('{}usage: {} filename\n'.format(warning,sys.argv[0]))
        raise SystemExit(1)
    else:
        lexer = FortranLexer()
        parser = FortranParser()
        data = open(sys.argv[1]).read()
        #print('{}'.format(data))                   #Debug the tokens
        rtok = []
        print("{} Starting Tokenization Phase\n".format(ok))
        for tok in lexer.tokenize(data):
                #print('{}'.format(tok))            #Debug the tokens
                rtok.append(tok)
        print("{} Writing list of Tokens into the filename: ../debug/Tokens.out".format(ok))
        f = open('../debug/Tokens.out', 'w')
        for i in rtok:
            f.write(str(i) + '\n')
        f.close()
        del rtok
        print("{} Tokenization Complete and saved.".format(ok))
        try:
            print("\n{} Starting Parsing phase.".format(ok))
            result = parser.parse(lexer.tokenize(data))
            print("{} The Parsing Process is Complete and saved in ../debug/Parser.out".format(ok))
        except EOFError:
            print('{}Bye'.format(ok))

if __name__ == '__main__':
    main()
