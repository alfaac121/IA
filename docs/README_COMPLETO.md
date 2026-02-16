# 🚀 NEO Intelligence System

Sistema de asistente de IA con terminal avanzada y acceso real a archivos del sistema.

## 📋 Estructura del Proyecto

Este proyecto tiene **DOS versiones**:

### 🌐 Versión Web (Demo)
- **Archivo principal**: `index.html`
- **Landing page**: `landing.html`
- **Características**:
  - ✅ Funciona en el navegador
  - ✅ Interfaz JARVIS completa
  - ✅ Reconocimiento y síntesis de voz
  - ✅ Clima en tiempo real
  - ⚠️ Terminal simulada (archivos falsos)

### 🐍 Versión Python (Completa)
- **Archivo principal**: `neo_assistant_v2.py`
- **Características**:
  - ✅ Acceso REAL a archivos de tu PC
  - ✅ Terminal flotante con PyQt6
  - ✅ Comandos del sistema Windows
  - ✅ Búsqueda de archivos reales
  - ✅ Crear/eliminar archivos
  - ✅ Síntesis de voz

## 🎯 ¿Qué Versión Usar?

### Usa la Versión Web si:
- Quieres probar NEO sin instalar nada
- Solo necesitas la interfaz visual
- Quieres subirlo a un hosting web
- No necesitas acceso a archivos reales

### Usa la Versión Python si:
- Necesitas acceso REAL a archivos
- Quieres ejecutar comandos del sistema
- Necesitas buscar/crear/eliminar archivos
- Quieres una terminal completa

## 🚀 Inicio Rápido

### Opción 1: Probar Demo Web
1. Abre `landing.html` en tu navegador
2. Haz clic en "Probar Demo Web"
3. O abre directamente `index.html`

### Opción 2: Usar Versión Python
1. Ejecuta `install_simple.bat`
2. Ejecuta `run_terminal.bat`
3. Haz clic en "💻 ABRIR TERMINAL"

## 📁 Archivos del Proyecto

### Versión Web
```
landing.html          - Página de inicio
landing.css           - Estilos de la landing
landing.js            - Funcionalidad de la landing
index.html            - Demo web de NEO
script.js             - Lógica principal web
style.css             - Estilos de la interfaz
terminal_windows.js   - Terminal simulada
bg.png                - Imagen de fondo
```

### Versión Python
```
neo_assistant_v2.py      - Programa principal
run_terminal.bat         - Ejecutar NEO
install_simple.bat       - Instalador
requirements.txt         - Dependencias Python
README_TERMINAL.md       - Documentación Python
INSTRUCCIONES_USO.txt    - Guía rápida
```

### Archivos Antiguos (Opcional)
```
neo_assistant.py      - Versión antigua (no usar)
run.bat               - Ejecutor antiguo (no usar)
run_v2.bat            - Ejecutor antiguo (no usar)
install.bat           - Instalador antiguo (no usar)
README_PYTHON.md      - Documentación antigua (no usar)
```

## 🌐 Subir a un Dominio Web

### Para la Landing Page + Demo:
1. Sube estos archivos a tu hosting:
   - `landing.html` (renombrar a `index.html`)
   - `landing.css`
   - `landing.js`
   - `index.html` (renombrar a `demo.html`)
   - `script.js`
   - `style.css`
   - `terminal_windows.js`
   - `bg.png`

2. Los usuarios podrán:
   - Ver la landing page
   - Probar el demo web
   - Descargar la versión Python

### Para Solo el Demo:
1. Sube solo:
   - `index.html`
   - `script.js`
   - `style.css`
   - `terminal_windows.js`
   - `bg.png`

## 💻 Comandos de la Terminal Python

```bash
# Sistema
ayuda          - Ver todos los comandos
neofetch       - Info del sistema
whoami         - Usuario actual

# Archivos (Acceso Real)
dir / ls       - Listar archivos
cd [carpeta]   - Cambiar directorio
pwd            - Directorio actual
cat [archivo]  - Ver contenido
find [nombre]  - Buscar archivos
tree           - Árbol de directorios
mkdir [nombre] - Crear carpeta
touch [nombre] - Crear archivo
rm [archivo]   - Eliminar archivo

# Sistema Windows
tasklist       - Procesos activos
systeminfo     - Info del sistema
ipconfig       - Configuración de red
ping [host]    - Ping a servidor

# NEO
decir [texto]  - NEO habla
abrir [url]    - Abrir navegador
buscar [texto] - Buscar en Google
```

## 📦 Requisitos

### Versión Web:
- Navegador moderno (Chrome, Firefox, Edge)
- Conexión a internet (para APIs)

### Versión Python:
- Windows 10/11
- Python 3.8 o superior
- 50 MB de espacio
- 2 GB RAM mínimo

## 🔧 Instalación Python

### Automática (Recomendada):
```bash
install_simple.bat
```

### Manual:
```bash
pip install PyQt6 pyttsx3 requests
```

## 🎨 Características

### Versión Web:
- ✅ Interfaz estilo JARVIS
- ✅ Reconocimiento de voz
- ✅ Síntesis de voz
- ✅ Clima en tiempo real
- ✅ Gestión de contactos
- ✅ Modos visuales (Normal, Combate, Descanso)
- ✅ Terminal simulada

### Versión Python:
- ✅ Todo lo de la versión web
- ✅ Acceso real a archivos
- ✅ Terminal flotante
- ✅ Comandos del sistema
- ✅ Búsqueda de archivos
- ✅ Historial de comandos

## 🐛 Solución de Problemas

### "Python no se reconoce"
- Instala Python desde python.org
- Marca "Add Python to PATH"

### "No module named PyQt6"
```bash
pip install PyQt6
```

### La voz no funciona
```bash
pip install pyttsx3
```

### El demo web no funciona
- Usa un navegador moderno
- Permite permisos de micrófono
- Verifica conexión a internet

## 📝 Licencia

Proyecto educativo - Uso libre

## 👨‍💻 Autor

Creado para exploradores del sistema 🚀

---

## 🎯 Próximos Pasos

1. **Probar Demo Web**: Abre `landing.html`
2. **Instalar Python**: Ejecuta `install_simple.bat`
3. **Usar NEO**: Ejecuta `run_terminal.bat`
4. **Leer Docs**: Abre `README_TERMINAL.md`

¡Disfruta de NEO! 💚
