::start

@echo off

::calls the currect drive letter
%~d0			

::searches for path of batch file
cd "%~dp0"		

::calls main.py from src
python -m src.main	

timeout.exe 1

::end