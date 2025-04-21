@echo off
cls
rem 21. April  2025 - Create a new NVDA Add-On 
Echo stepp 1:
rem del addon\*.html /s 
del addon\*.mo /s 
echo stepp 2:
copy addon\doc\en\readme.md readme.md 
pause 
echo stepp 3:
scons
pause 