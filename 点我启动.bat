@echo off
:start
echo ==���׵Ĳ˵�==
echo 0��dos��
echo 1��wx���
echo 2��qt5��

set /p input=����ѡ��

if %input% == 0 (
cls
.\python\python.exe ���������_nogui.py
)

if %input% == 1 (
start /min cmd /c .\python\python.exe ���������_wxpython��.py
)

if %input% == 2 (


)