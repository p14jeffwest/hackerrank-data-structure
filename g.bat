@echo off
setlocal

echo [1/5] Current git status
git status
if errorlevel 1 goto :error

echo.
set /p MSG=Commit message: 
if "%MSG%"=="" (
  echo Commit message cannot be empty.
  goto :end
)

echo.
echo [2/5] Staging all changes
git add -A
if errorlevel 1 goto :error

echo [3/5] Staged changes review
git status
if errorlevel 1 goto :error

echo.
set /p CONFIRM=Proceed with commit and push? (y/N): 
if /I not "%CONFIRM%"=="y" goto :end

echo [4/5] Commit
git commit -m "%MSG%"
if errorlevel 1 goto :error

echo [5/5] Push
git push
if errorlevel 1 goto :error

echo Done.
goto :end

:error
echo Error occurred. Check output above.

:end
endlocal
