@echo off
echo ========================================
echo   CREANDO PAQUETE NEO TERMINAL v2.0
echo ========================================
echo.

REM Crear carpeta temporal para el paquete
if exist NEO-Terminal-Package rmdir /s /q NEO-Terminal-Package
mkdir NEO-Terminal-Package

echo [+] Copiando archivos necesarios...

REM Copiar archivos principales
copy python\neo_assistant_v2.py NEO-Terminal-Package\
copy python\requirements.txt NEO-Terminal-Package\
copy python\install_simple.bat NEO-Terminal-Package\
copy python\run_terminal.bat NEO-Terminal-Package\

REM Copiar archivos opcionales
copy python\neo.bat NEO-Terminal-Package\
copy python\neo.vbs NEO-Terminal-Package\
copy python\instalar_en_path.bat NEO-Terminal-Package\
copy python\desinstalar_del_path.bat NEO-Terminal-Package\

REM Copiar documentación
copy python\README_INSTALACION.md NEO-Terminal-Package\
copy python\ARCHIVOS_NECESARIOS.txt NEO-Terminal-Package\
copy python\INSTRUCCIONES_PATH.txt NEO-Terminal-Package\
copy python\CAMBIOS_RECIENTES.txt NEO-Terminal-Package\

echo.
echo [+] Archivos copiados exitosamente
echo.
echo ========================================
echo   PAQUETE CREADO EN:
echo   NEO-Terminal-Package\
echo ========================================
echo.
echo Ahora comprime esta carpeta en ZIP
echo y subela a GitHub Releases
echo.
pause
