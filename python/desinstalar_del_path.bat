@echo off
echo ========================================
echo NEO Terminal - Desinstalador del PATH
echo ========================================
echo.

REM Obtener la ruta actual
set "NEO_PATH=%~dp0"

echo [*] Removiendo NEO del PATH...
echo.

REM Nota: Este script solo muestra instrucciones
echo Para remover NEO del PATH manualmente:
echo.
echo 1. Presiona Win + R
echo 2. Escribe: sysdm.cpl
echo 3. Ve a "Opciones avanzadas"
echo 4. Click en "Variables de entorno"
echo 5. En "Variables de usuario", selecciona "Path"
echo 6. Click en "Editar"
echo 7. Busca y elimina: %NEO_PATH%
echo 8. Click en "Aceptar" en todas las ventanas
echo.

REM Eliminar neo.bat
if exist "%NEO_PATH%neo.bat" (
    del "%NEO_PATH%neo.bat"
    echo [+] Archivo neo.bat eliminado
) else (
    echo [!] Archivo neo.bat no encontrado
)

echo.
echo ========================================
pause
