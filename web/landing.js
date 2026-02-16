// Efecto Matrix en el fondo
const canvas = document.getElementById('matrixBg');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const matrix = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789@#$%^&*()*&^%+-/~{[|`]}";
const matrixArray = matrix.split("");

const fontSize = 16;
const columns = canvas.width / fontSize;

const drops = [];
for (let x = 0; x < columns; x++) {
    drops[x] = 1;
}

function drawMatrix() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.04)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    ctx.fillStyle = '#00ff00';
    ctx.font = fontSize + 'px monospace';
    
    for (let i = 0; i < drops.length; i++) {
        const text = matrixArray[Math.floor(Math.random() * matrixArray.length)];
        ctx.fillText(text, i * fontSize, drops[i] * fontSize);
        
        if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
            drops[i] = 0;
        }
        
        drops[i]++;
    }
}

setInterval(drawMatrix, 35);

// Redimensionar canvas
window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});

// Función de descarga
function downloadNEO() {
    // Crear un archivo ZIP virtual con instrucciones
    const message = `
═══════════════════════════════════════════════════════════════
    DESCARGA DE NEO TERMINAL - INSTRUCCIONES
═══════════════════════════════════════════════════════════════

¡Gracias por descargar NEO Terminal!

ARCHIVOS NECESARIOS:
Los archivos ya están en tu carpeta del proyecto:

1. neo_assistant_v2.py       - Programa principal
2. install_simple.bat         - Instalador automático
3. run_terminal.bat           - Ejecutar NEO
4. requirements.txt           - Dependencias
5. README_TERMINAL.md         - Documentación completa
6. INSTRUCCIONES_USO.txt      - Guía rápida

═══════════════════════════════════════════════════════════════
INSTALACIÓN:
═══════════════════════════════════════════════════════════════

PASO 1: Instalar Python
   - Descarga Python desde: https://www.python.org/downloads/
   - Durante la instalación, marca "Add Python to PATH"

PASO 2: Instalar Dependencias
   - Doble clic en: install_simple.bat
   - Espera a que termine la instalación

PASO 3: Ejecutar NEO
   - Doble clic en: run_terminal.bat
   - ¡Disfruta de NEO Terminal!

═══════════════════════════════════════════════════════════════
COMANDOS PRINCIPALES:
═══════════════════════════════════════════════════════════════

ayuda          - Ver todos los comandos
dir / ls       - Listar archivos
cd [carpeta]   - Cambiar directorio
cat [archivo]  - Ver contenido de archivo
find [nombre]  - Buscar archivos
tree           - Árbol de directorios
neofetch       - Info del sistema

═══════════════════════════════════════════════════════════════
SOPORTE:
═══════════════════════════════════════════════════════════════

Si tienes problemas:
1. Lee README_TERMINAL.md
2. Lee INSTRUCCIONES_USO.txt
3. Verifica que Python esté instalado correctamente

═══════════════════════════════════════════════════════════════
¡Disfruta explorando tu PC con NEO Terminal! 🚀
═══════════════════════════════════════════════════════════════
    `;
    
    // Crear y descargar archivo de texto
    const blob = new Blob([message], { type: 'text/plain' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'NEO_INSTRUCCIONES_DESCARGA.txt';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
    
    // Mostrar mensaje
    alert(`
📦 DESCARGA INICIADA

Los archivos de NEO Terminal ya están en tu carpeta del proyecto.

Se ha descargado un archivo con instrucciones detalladas.

ARCHIVOS PRINCIPALES:
✓ neo_assistant_v2.py
✓ install_simple.bat
✓ run_terminal.bat

PRÓXIMOS PASOS:
1. Instala Python (si no lo tienes)
2. Ejecuta install_simple.bat
3. Ejecuta run_terminal.bat

¡Listo para usar! 🚀
    `);
}

// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Animación de entrada para las cards
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observar todas las cards
document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.version-card, .feature-card, .download-card');
    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = 'all 0.6s ease-out';
        observer.observe(card);
    });
});
