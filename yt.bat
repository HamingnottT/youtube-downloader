::start

@echo off

%~d0			::calls the currect drive letter

cd "%~dp0"		::searches for path of batch file

python -m src.main	::calls main.py from src

timeout.exe 1

::end