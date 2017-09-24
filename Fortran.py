from src.lexer import FortranLexer
from src.parser import FortranParser
import sys


def main():
    sys.argv.append('../datasets/fact.fiv')
    if len(sys.argv) != 2:
        sys.stderr.write('usage: {} filename\n'.format(sys.argv[0]))
        raise SystemExit(1)

    lexer = FortranLexer()
    parser = FortranParser()
    data = open(sys.argv[1]).read()
    print('{}'.format(data))
    rtok = []
    for tok in lexer.tokenize(data):
            print('{}'.format(tok))
            rtok.append(tok)
    f=open('../debug/Tokens.out','w')
    for i  in rtok:
        f.write(str(i)+'\n')
    f.close()
    del rtok
    print("Tokenization Complete and saved in ../debug/Tokens.out")
    # print(parser.error)
    debug = 0
    p = parser.parse(lexer.tokenize(data))
    print("Parser Done, We need to add a rule for \$\n")


    '''while True:
        try:
            result = parser.parse(lexer.tokenize(text))
            print(result)
        except EOFError:
            break    '''
            
if __name__ == '__main__':
    main()
