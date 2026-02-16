@echo off
echo ========================================
echo    NEO TERMINAL - Version Python
echo    Con acceso real a archivos del PC
echo ========================================
echo.
echo Iniciando NEO Assistant...
echo.

python neo_assistant_v2.py

if errorlevel 1 (
    echo.
    echo ERROR: No se pudo iniciar NEO
    echo.
    echo Soluciones:
    echo 1. Instala Python desde python.org
    echo 2. Ejecuta: install_simple.bat
    echo 3. Verifica que Python este en PATH
    echo.
    pause
)
