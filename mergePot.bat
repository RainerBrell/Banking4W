@echo off
cls
rem 2026.03.18 
Echo POT Datei erstellen:
scons pot 
Echo POT-Datei mit bestehenden PO-Dateien verschmelzen:
For /R addon\locale\ %%f In (*.po) Do msgmerge -U --backup=none %%f banking4w.pot 
pause 