#!/bin/bash -e
#hfjimenez@utp.edu.co
#A small script to test the Lexer using virtualenv.
#It will create a virtualenv and install the requirement. 
#You can also test this code running: 
#python3.6 Lexer.py, an advice to check our lexer is 
#changing the dataset in the Lexer.py source code.
if [ -d "$venv" ]; then
  source venv/bin/activate 
else
	virtualenv -p /usr/bin/python3.6 venv
	source venv/bin/activate&&pip3.6 install sly
	python Lexer.py
fi
echo -e "\x1B[32m[✔]DONE\x1B[0m"
