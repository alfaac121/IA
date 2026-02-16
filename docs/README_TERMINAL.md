# 🚀 NEO TERMINAL - Versión Python con Acceso Real

## 📋 Descripción

NEO Terminal es una terminal avanzada con interfaz gráfica que te permite:
- ✅ **Acceso REAL a los archivos de tu PC**
- ✅ Navegar por carpetas y archivos
- ✅ Buscar archivos en todo el sistema
- ✅ Ejecutar comandos de Windows
- ✅ Síntesis de voz (NEO habla)
- ✅ Interfaz estilo hacker con colores Matrix

## 🔧 Instalación

### Opción 1: Instalación Simple (Recomendada)
```bash
install_simple.bat
```

### Opción 2: Instalación Manual
```bash
pip install PyQt6 pyttsx3 requests
```

## ▶️ Ejecutar NEO Terminal

Doble clic en:
```
run_terminal.bat
```

O desde la terminal:
```bash
python neo_assistant_v2.py
```

## 📚 Comandos Disponibles

### Sistema
- `ayuda` / `help` - Muestra todos los comandos
- `limpiar` / `clear` - Limpia la terminal
- `hora` - Muestra la hora actual
- `fecha` - Muestra la fecha
- `neofetch` - Info del sistema con logo NEO
- `whoami` - Usuario actual

### Archivos (Acceso Real a tu PC)
- `dir` / `ls` - Lista archivos y carpetas
- `cd [carpeta]` - Cambia de directorio
  - `cd ..` - Volver atrás
  - `cd ~` - Ir a home
- `pwd` - Muestra directorio actual
- `cat [archivo]` - Muestra contenido de archivo
- `type [archivo]` - Igual que cat (estilo Windows)
- `find [nombre]` - Busca archivos por nombre
- `tree` - Muestra árbol de directorios
- `mkdir [nombre]` - Crea una carpeta
- `touch [archivo]` - Crea un archivo vacío
- `rm [archivo]` - Elimina un archivo

### Monitoreo
- `tasklist` - Lista procesos de Windows
- `systeminfo` - Info completa del sistema
- `wmic cpu` - Info del CPU
- `wmic memorychip` - Info de RAM

### Red
- `ping [host]` - Ping a un servidor
- `ipconfig` - Configuración de red
- `netstat` - Conexiones activas

### NEO
- `decir [texto]` - NEO dice el texto en voz alta
- `abrir [url]` - Abre una URL en el navegador
- `buscar [texto]` - Busca en Google

### Windows
Cualquier comando de CMD funciona:
- `ipconfig`
- `dir`
- `tasklist`
- `netstat`
- etc.

## 💡 Ejemplos de Uso

```bash
# Ver archivos del directorio actual
dir

# Ir a Documentos
cd C:\Users\TuUsuario\Documentos

# Buscar todos los archivos .txt
find .txt

# Ver contenido de un archivo
cat archivo.txt

# Crear una carpeta
mkdir mi_carpeta

# Ver árbol de directorios
tree

# Info del sistema
neofetch

# Que NEO hable
decir Hola, soy NEO

# Buscar en Google
buscar python tutorial
```

## 🎨 Características

- **Terminal flotante** - Puedes moverla arrastrando
- **Historial de comandos** - Usa ↑ y ↓ para navegar
- **Colores Matrix** - Verde fosforescente y azul cyan
- **Iconos** - 📁 para carpetas, 📄 para archivos
- **Síntesis de voz** - NEO puede hablar
- **Acceso real** - Navega por TODO tu PC

## ⚠️ Notas Importantes

1. **Permisos**: Algunos comandos pueden requerir permisos de administrador
2. **Seguridad**: Ten cuidado con `rm` - elimina archivos permanentemente
3. **Rutas**: Puedes usar rutas absolutas o relativas
4. **Windows**: Esta versión está optimizada para Windows

## 🐛 Solución de Problemas

### "Python no se reconoce"
- Instala Python desde python.org
- Marca la opción "Add Python to PATH"

### "No module named PyQt6"
```bash
pip install PyQt6
```

### La voz no funciona
```bash
pip install pyttsx3
```

## 📝 Versión

**NEO Terminal v2.0** - Python Edition
- Acceso real a archivos del sistema
- Terminal flotante con PyQt6
- Síntesis de voz integrada

---

Creado para explorar tu PC con estilo 🚀
