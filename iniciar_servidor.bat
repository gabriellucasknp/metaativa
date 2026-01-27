@echo off
REM Script para iniciar o servidor Django METAATIVA
REM Execute este arquivo para rodar a aplicação

echo.
echo ====================================================
echo   METAATIVA - Servidor Django
echo ====================================================
echo.

cd /d C:\Users\lixei\Downloads\metaativa-main

REM Ativar ambiente virtual
call .venv\Scripts\activate.bat

REM Rodar servidor
echo.
echo Iniciando servidor Django...
echo Acesse: http://127.0.0.1:8000/
echo Admin:  http://127.0.0.1:8000/admin/ (user: admin, senha: admin123)
echo.
python manage.py runserver

pause
