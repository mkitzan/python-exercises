@echo off
title Book Statistics
:start
cls
set /p ARG="Program input: "
py book_statistics.py %ARG%
pause >nul
if NOT "%ARG%" == "books.csv" goto start