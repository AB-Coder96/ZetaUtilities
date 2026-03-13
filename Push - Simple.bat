setlocal enabledelayedexpansion
for /f "tokens=*" %%a in ('hostname') do set "computer_name=%%a"
Git rm -r --cached .
Git add .
Git commit -m "reg updates"
Git push
endlocal
pause