# 🚀 NEO Terminal v2.0 - Guía de Instalación

## 📦 Contenido del Paquete

Este paquete incluye todo lo necesario para ejecutar NEO Terminal:

```
python/
├── neo_assistant_v2.py          # Programa principal
├── requirements.txt             # Dependencias de Python
├── install_simple.bat          # Instalador automático
├── run_terminal.bat            # Ejecutar terminal
├── neo.bat                     # Comando global 'neo'
├── neo.vbs                     # Launcher silencioso
├── instalar_en_path.bat        # Agregar al PATH (opcional)
├── desinstalar_del_path.bat    # Quitar del PATH (opcional)
└── README_INSTALACION.md       # Este archivo
```

## ⚡ Instalación Rápida (3 pasos)

### 1️⃣ Instalar Dependencias
Doble clic en:
```
install_simple.bat
```
Esto instalará automáticamente:
- PyQt6 (interfaz gráfica)
- pyttsx3 (síntesis de voz)
- psutil (información del sistema)
- requests (peticiones web)

### 2️⃣ Ejecutar NEO Terminal
Doble clic en:
```
run_terminal.bat
```

### 3️⃣ ¡Listo! 🎉
La terminal flotante aparecerá con animación épica.

---

## 🔧 Instalación Avanzada (Opcional)

### Agregar comando 'neo' global
Si quieres ejecutar NEO desde cualquier carpeta:

1. Doble clic en: `instalar_en_path.bat`
2. Ahora puedes abrir CMD y escribir: `neo`

### Desinstalar comando global
```
desinstalar_del_path.bat
```

---

## 📋 Requisitos del Sistema

- ✅ Windows 10/11
- ✅ Python 3.8 o superior
- ✅ 50 MB de espacio libre
- ✅ 2 GB RAM mínimo

---

## 🎮 Comandos Disponibles

Una vez abierta la terminal, prueba estos comandos:

### Comandos del Sistema
```bash
ayuda          # Ver todos los comandos
info           # Información completa del sistema
cpu            # Info del procesador
ram            # Info de memoria RAM
disk           # Info del disco
monitor        # Monitor en tiempo real
stop           # Detener monitor
```

### Comandos de Archivos
```bash
ls             # Listar archivos
cd carpeta     # Cambiar directorio
pwd            # Directorio actual
```

### Comandos de Windows
```bash
ipconfig       # Configuración de red
tasklist       # Procesos activos
systeminfo     # Info del sistema
ping google.com # Hacer ping
```

---

## ❓ Solución de Problemas

### Error: "Python no encontrado"
**Solución:** Instala Python desde https://www.python.org/downloads/
- ✅ Marca la opción "Add Python to PATH"

### Error: "No module named 'PyQt6'"
**Solución:** Ejecuta `install_simple.bat` de nuevo

### La terminal no abre
**Solución:** 
1. Abre CMD en esta carpeta
2. Ejecuta: `python neo_assistant_v2.py`
3. Lee el error que aparece

### Error de permisos
**Solución:** Ejecuta como Administrador

---

## 🎨 Características

✨ **Terminal Flotante**
- Ventana sin bordes
- Animaciones épicas de apertura/cierre
- Efecto elástico extremo

🎨 **Estilo Hacker**
- Colores verde Matrix
- Logo ASCII "NEO TERM"
- Prompt estilo Kali Linux

🔊 **Sonidos**
- Beeps sutiles al ejecutar comandos
- Sonidos de éxito/error
- Sonido especial al iniciar monitor

⌨️ **Historial**
- Navega comandos anteriores con ↑ ↓
- Autocompletado de rutas

---

## 📞 Soporte

¿Problemas? Revisa los archivos:
- `DEBUG.txt` - Información de depuración
- `CAMBIOS_RECIENTES.txt` - Últimas actualizaciones
- `INSTRUCCIONES_PATH.txt` - Ayuda con PATH

---

## 🌟 Disfruta NEO Terminal!

Creado con 💚 para exploradores del sistema

**Versión:** 2.0  
**Fecha:** 2024  
**Licencia:** Uso libre
