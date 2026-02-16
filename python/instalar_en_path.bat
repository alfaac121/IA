@echo off
echo ========================================
echo NEO Terminal - Instalador en PATH
echo ========================================
echo.

REM Obtener la ruta actual
set "NEO_PATH=%~dp0"

echo [*] Ruta de NEO: %NEO_PATH%
echo.

REM Crear archivo neo.bat en la carpeta de NEO que ejecuta el VBS
echo @echo off > "%NEO_PATH%neo.bat"
echo wscript "%NEO_PATH%neo.vbs" >> "%NEO_PATH%neo.bat"
echo exit >> "%NEO_PATH%neo.bat"

echo [+] Archivo neo.bat creado
echo.

REM Agregar al PATH del usuario
echo [*] Agregando al PATH del usuario...
setx PATH "%PATH%;%NEO_PATH%"

echo.
echo ========================================
echo [OK] Instalacion completada!
echo.
echo Ahora puedes usar NEO desde cualquier lugar:
echo.
echo   1. Abre CMD o PowerShell
echo   2. Escribe: neo
echo   3. Presiona Enter
echo.
echo NOTA: Cierra y vuelve a abrir CMD/PowerShell
echo       para que los cambios surtan efecto
echo ========================================
pause
