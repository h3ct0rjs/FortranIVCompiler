'''
Utilities for FortranIV Compiler
'''
reset = '\x1b[0m'    # reset all colors to white on black
bold = '\x1b[1m'     # enable bold text
uline = '\x1b[4m'    # enable underlined text
nobold = '\x1b[22m'  # disable bold text
nouline = '\x1b[24m' # disable underlined text
red = '\x1b[31m'     # red text
green = '\x1b[32m'   # green text
blue = '\x1b[34m'    # blue text
cyan = '\x1b[36m'    # cyan text
white = '\x1b[37m'   # white text (use reset unless it's only temporary)
yellow = '\x1b[33m'

tree = "{}{}".format(bold, white)
warning = "{}[✘✘✘]{}".format(red, reset)
info = "{}[! ***]{}".format(yellow, reset)
ok = "{}[OK ✓]{}".format(cyan, reset)
__version__="0.3v"
__author__='Hector F. Jimenez S, Kevin Moreno H.'
__email__='hfjimenez@utp.edu.co,kevin_utp24@utp.edu.co'