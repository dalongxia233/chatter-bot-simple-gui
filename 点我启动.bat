@echo off
:start
echo ==简易的菜单==
echo 0、dos版
echo 1、wx库版
echo 2、qt5版

set /p input=您的选择：

if %input% == 0 (
cls
.\python\python.exe 聊天机器人_nogui.py
)

if %input% == 1 (
start /min cmd /c .\python\python.exe 聊天机器人_wxpython版.py
)

if %input% == 2 (


)