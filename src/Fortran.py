from lexer import FortranLexer
from  parser import FortranParser
import sys

def main():
    sys.argv.append('../Lexer/datasets/test1')
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: %s filename\n" % sys.argv[0])
        raise SystemExit(1)

    lexer = FortranLexer()
    parser = FortranParser()
    text = open(sys.argv[1]).read()
    lexer.test(test)

    while True:
        try:
            result = parser.parse(lexer.tokenize(text))
            print(result)
        except EOFError:
            break    
            
if __name__ == '__main__':
    main()
