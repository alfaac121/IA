// TERMINAL FLOTANTE ESTILO KALI LINUX CON DELFÍN
// Sistema de archivos simulado para demo web

// Variables de terminal (usar las globales de script.js si existen)
if (typeof floatingTerminalOpen === 'undefined') {
    var floatingTerminalOpen = false;
}
if (typeof terminalHistory === 'undefined') {
    var terminalHistory = [];
}
if (typeof historyIndex === 'undefined') {
    var historyIndex = 0;
}

let currentDirectory = '/home/neo';

// Sistema de archivos simulado
const fileSystem = {
    '/': {
        type: 'dir',
        contents: {
            'home': { type: 'dir', contents: {
                'neo': { type: 'dir', contents: {
                    'documentos': { type: 'dir', contents: {
                        'notas.txt': { type: 'file', content: 'Notas del sistema NEO\nVersión 2.0\nTodo funcionando correctamente.' },
                        'tareas.txt': { type: 'file', content: 'Lista de tareas:\n- Actualizar sistema\n- Revisar contactos\n- Configurar clima' }
                    }},
                    'descargas': { type: 'dir', contents: {
                        'archivo.zip': { type: 'file', content: '[Archivo comprimido]' }
                    }},
                    'proyectos': { type: 'dir', contents: {
                        'neo-ai': { type: 'dir', contents: {
                            'main.py': { type: 'file', content: '# NEO AI Core\nimport neural_engine\n\nif __name__ == "__main__":\n    neo.start()' },
                            'config.json': { type: 'file', content: '{\n  "version": "2.0",\n  "mode": "active"\n}' }
                        }}
                    }},
                    'README.md': { type: 'file', content: '# Sistema NEO\nAsistente de inteligencia artificial\nVersión 2.0' }
                }}
            }},
            'etc': { type: 'dir', contents: {
                'config.conf': { type: 'file', content: 'NEO_VERSION=2.0\nMODE=active' }
            }},
            'var': { type: 'dir', contents: {
                'log': { type: 'dir', contents: {
                    'system.log': { type: 'file', content: '[2024-02-15 10:30:00] Sistema iniciado\n[2024-02-15 10:30:05] NEO AI cargado' }
                }}
            }}
        }
    }
};

function getDirectoryContents(path) {
    const parts = path.split('/').filter(p => p);
    let current = fileSystem['/'];
    
    for (let part of parts) {
        if (current.contents && current.contents[part]) {
            current = current.contents[part];
        } else {
            return null;
        }
    }
    return current;
}

function resolvePath(path) {
    if (path.startsWith('/')) {
        return path;
    } else if (path === '..') {
        const parts = currentDirectory.split('/').filter(p => p);
        parts.pop();
        return '/' + parts.join('/');
    } else if (path === '.') {
        return currentDirectory;
    } else {
        return currentDirectory === '/' ? '/' + path : currentDirectory + '/' + path;
    }
}

// Sonido retro de tecla
function playKeySound() {
    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    const oscillator = audioContext.createOscillator();
    const gainNode = audioContext.createGain();
    
    oscillator.connect(gainNode);
    gainNode.connect(audioContext.destination);
    
    oscillator.frequency.value = 800;
    oscillator.type = 'square';
    
    gainNode.gain.setValueAtTime(0.1, audioContext.currentTime);
    gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.05);
    
    oscillator.start(audioContext.currentTime);
    oscillator.stop(audioContext.currentTime + 0.05);
}

function openFloatingTerminal() {
    // Cerrar terminal anterior si existe
    if (floatingTerminalOpen) {
        const oldOverlay = document.getElementById('floatingTerminalOverlay');
        if (oldOverlay) oldOverlay.remove();
        floatingTerminalOpen = false;
    }
    
    // Crear overlay
    const overlay = document.createElement('div');
    overlay.id = 'floatingTerminalOverlay';
    overlay.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0);
        z-index: 9998;
        display: flex;
        justify-content: center;
        align-items: center;
        transition: background 0.3s ease;
    `;
    
    // Crear terminal
    const terminal = document.createElement('div');
    terminal.id = 'floatingTerminal';
    terminal.style.cssText = `
        width: 900px;
        height: 550px;
        background: #0C0C0C;
        border: none;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.8);
        display: flex;
        flex-direction: column;
        font-family: 'Consolas', 'Courier New', monospace;
        position: relative;
        opacity: 0;
        transform: scale(0.8);
        transition: all 1.5s cubic-bezier(0.34, 1.56, 0.64, 1);
    `;
    
    // Header estilo Windows
    const header = document.createElement('div');
    header.style.cssText = `
        background: #1F1F1F;
        padding: 8px 12px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        cursor: move;
        user-select: none;
    `;
    
    const titleArea = document.createElement('div');
    titleArea.style.cssText = 'display: flex; align-items: center; gap: 8px;';
    titleArea.innerHTML = `
        <svg width="16" height="16" viewBox="0 0 16 16" style="opacity: 0.8;">
            <rect width="16" height="16" fill="#0C0C0C"/>
            <text x="2" y="12" font-family="Consolas" font-size="10" fill="#00ff00">C:</text>
        </svg>
        <span style="color: #00ff00; font-size: 12px; font-weight: normal;">Terminal NEO</span>
    `;
    
    const controls = document.createElement('div');
    controls.style.cssText = 'display: flex; gap: 10px;';
    controls.innerHTML = `
        <button id="minimizeTerminalBtn" style="
            background: transparent;
            border: none;
            color: #00ff00;
            width: 45px;
            height: 30px;
            cursor: pointer;
            font-size: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
        " title="Minimizar">─</button>
        <button id="maximizeTerminalBtn" style="
            background: transparent;
            border: none;
            color: #00ff00;
            width: 45px;
            height: 30px;
            cursor: pointer;
            font-size: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
        " title="Maximizar">□</button>
        <button id="closeTerminalBtn" style="
            background: transparent;
            border: none;
            color: #00ff00;
            width: 45px;
            height: 30px;
            cursor: pointer;
            font-size: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
        " title="Cerrar">✕</button>
    `;
    
    header.appendChild(titleArea);
    header.appendChild(controls);
    
    // Output con delfín
    const output = document.createElement('div');
    output.id = 'terminalOutput';
    output.style.cssText = `
        flex: 1;
        padding: 20px;
        overflow-y: auto;
        overflow-x: hidden;
        color: #00ff00;
        font-size: 14px;
        line-height: 1.4;
        background: #0C0C0C;
        font-family: 'Consolas', 'Courier New', monospace;
        white-space: pre;
    `;
    
    // Ocultar scrollbar
    output.style.setProperty('scrollbar-width', 'none');
    const style = document.createElement('style');
    style.textContent = `
        #terminalOutput::-webkit-scrollbar {
            display: none;
        }
    `;
    document.head.appendChild(style);
    
    const neoAscii = `<span style="color: #00d4ff;">                                    __
                               _.-~  )
                    _..--~~~~,'   ,-/     _
                 .-'. . . .'   ,-','    ,' )
               ,'. . . _   ,--~,-'__..-'  ,'
             ,'. . .  (@)' ---~~~~      ,'
            /. . . . '~~             ,-'
           /. . . . .             ,-'
          ; . . . .  - .        ,'
         : . . . .       _     /
        . . . . .          \`-.:
       . . . ./  - .          )
      .  . . |  _____..---.._/ 
     ~---~~~~---~~~</span>

<span style="color: #00ff00;">    ███╗   ██╗███████╗ ██████╗ 
    ████╗  ██║██╔════╝██╔═══██╗
    ██╔██╗ ██║█████╗  ██║   ██║
    ██║╚██╗██║██╔══╝  ██║   ██║
    ██║ ╚████║███████╗╚██████╔╝
    ╚═╝  ╚═══╝╚══════╝ ╚═════╝</span>
    
<span style="color: #888888;">    Intelligence System v2.0 - Demo Web</span>
<span style="color: #ff8800;">    ⚠️  Archivos simulados - Descarga versión Python para acceso real</span>

<span style="color: #00d4ff;">┌──(</span><span style="color: #00ff00;">neo㉿system</span><span style="color: #00d4ff;">)-[~]</span>
<span style="color: #00d4ff;">└─$</span> `;
    
    output.innerHTML = neoAscii;
    
    // Input area
    const inputArea = document.createElement('div');
    inputArea.style.cssText = `
        padding: 10px 20px;
        display: flex;
        align-items: flex-start;
        background: #0C0C0C;
    `;
    
    const prompt = document.createElement('div');
    prompt.id = 'terminalPrompt';
    prompt.style.cssText = 'display: flex; flex-direction: column; margin-right: 5px; font-size: 14px;';
    prompt.innerHTML = '<span style="color: #00d4ff;">┌──(</span><span style="color: #00ff00;">neo㉿system</span><span style="color: #00d4ff;">)-[~]</span><br><span style="color: #00d4ff;">└─</span><span style="color: #00ff00;">$</span> ';
    
    const input = document.createElement('input');
    input.id = 'terminalInput';
    input.type = 'text';
    input.style.cssText = `
        flex: 1;
        background: transparent;
        border: none;
        color: #ffffff;
        font-family: 'Consolas', 'Courier New', monospace;
        font-size: 14px;
        outline: none;
        caret-color: #00ff00;
        margin-left: 5px;
        align-self: flex-end;
    `;
    
    inputArea.appendChild(prompt);
    inputArea.appendChild(input);
    
    terminal.appendChild(header);
    terminal.appendChild(output);
    terminal.appendChild(inputArea);
    overlay.appendChild(terminal);
    document.body.appendChild(overlay);
    
    // Animación de entrada
    requestAnimationFrame(() => {
        overlay.style.background = 'rgba(0, 0, 0, 0.85)';
        terminal.style.opacity = '1';
        terminal.style.transform = 'scale(1)';
    });
    
    floatingTerminalOpen = true;
    
    // Focus en input
    setTimeout(() => input.focus(), 1500);
    
    // Event listeners
    document.getElementById('closeTerminalBtn').onclick = closeFloatingTerminal;
    document.getElementById('minimizeTerminalBtn').onclick = () => {
        terminal.style.transform = 'scale(0.95)';
        setTimeout(() => terminal.style.transform = 'scale(1)' , 100);
    };
    document.getElementById('maximizeTerminalBtn').onclick = () => {
        if (terminal.style.width === '100vw') {
            terminal.style.width = '900px';
            terminal.style.height = '550px';
        } else {
            terminal.style.width = '100vw';
            terminal.style.height = '100vh';
        }
    };
    
    // Hover effects
    const buttons = [
        document.getElementById('minimizeTerminalBtn'),
        document.getElementById('maximizeTerminalBtn'),
        document.getElementById('closeTerminalBtn')
    ];
    
    buttons.forEach((btn, index) => {
        btn.addEventListener('mouseenter', () => {
            if (index === 2) {
                btn.style.background = '#E81123';
                btn.style.color = '#FFFFFF';
            } else {
                btn.style.background = '#3A3A3A';
                btn.style.color = '#00ff00';
            }
        });
        btn.addEventListener('mouseleave', () => {
            btn.style.background = 'transparent';
            btn.style.color = '#00ff00';
        });
    });
    
    overlay.onclick = (e) => {
        if (e.target === overlay) closeFloatingTerminal();
    };
    
    // Sonido al escribir
    input.addEventListener('keydown', (e) => {
        if (e.key.length === 1 || e.key === 'Backspace') {
            playKeySound();
        }
        
        if (e.key === 'Enter') {
            const cmd = input.value.trim();
            if (cmd) {
                executeFloatingCommand(cmd);
                input.value = '';
            }
        } else if (e.key === 'ArrowUp') {
            e.preventDefault();
            if (terminalHistory.length > 0 && historyIndex > 0) {
                historyIndex--;
                input.value = terminalHistory[historyIndex];
            }
        } else if (e.key === 'ArrowDown') {
            e.preventDefault();
            if (historyIndex < terminalHistory.length - 1) {
                historyIndex++;
                input.value = terminalHistory[historyIndex];
            } else {
                historyIndex = terminalHistory.length;
                input.value = '';
            }
        }
    });
    
    // Hacer arrastrable
    let isDragging = false;
    let currentX, currentY, initialX, initialY;
    
    header.addEventListener('mousedown', (e) => {
        if (!e.target.closest('button')) {
            isDragging = true;
            initialX = e.clientX - terminal.offsetLeft;
            initialY = e.clientY - terminal.offsetTop;
            terminal.style.transition = 'none';
        }
    });
    
    document.addEventListener('mousemove', (e) => {
        if (isDragging) {
            e.preventDefault();
            currentX = e.clientX - initialX;
            currentY = e.clientY - initialY;
            terminal.style.position = 'absolute';
            terminal.style.left = currentX + 'px';
            terminal.style.top = currentY + 'px';
        }
    });
    
    document.addEventListener('mouseup', () => {
        if (isDragging) {
            isDragging = false;
            terminal.style.transition = 'all 1.5s cubic-bezier(0.34, 1.56, 0.64, 1)';
        }
    });
}

function closeFloatingTerminal() {
    const overlay = document.getElementById('floatingTerminalOverlay');
    const terminal = document.getElementById('floatingTerminal');
    
    if (overlay && terminal) {
        overlay.style.background = 'rgba(0, 0, 0, 0)';
        terminal.style.opacity = '0';
        terminal.style.transform = 'scale(0.8)';
        
        setTimeout(() => {
            overlay.remove();
            floatingTerminalOpen = false;
        }, 1500);
    }
}

function addTerminalOutput(text) {
    const output = document.getElementById('terminalOutput');
    if (output) {
        const line = document.createElement('div');
        line.innerHTML = text;
        output.appendChild(line);
        output.scrollTop = output.scrollHeight;
    }
}

function executeFloatingCommand(cmd) {
    terminalHistory.push(cmd);
    historyIndex = terminalHistory.length;
    
    const output = document.getElementById('terminalOutput');
    
    // Mostrar comando ejecutado
    const cmdLine = document.createElement('div');
    cmdLine.innerHTML = `<span style="color: #00d4ff;">┌──(</span><span style="color: #00ff00;">neo㉿system</span><span style="color: #00d4ff;">)-[~]</span><br><span style="color: #00d4ff;">└─</span><span style="color: #00ff00;">$</span> <span style="color: #ffffff;">${cmd}</span>`;
    output.appendChild(cmdLine);
    
    const parts = cmd.toLowerCase().trim().split(' ');
    const command = parts[0];
    const args = parts.slice(1);
    
    // Comandos
    if (command === 'ayuda' || command === 'help') {
        addTerminalOutput('<span style="color: #00d4ff;">[*]</span> Comandos disponibles:');
        addTerminalOutput('');
        addTerminalOutput('<span style="color: #888888;">Sistema:</span>');
        addTerminalOutput('  help/ayuda       Muestra esta ayuda');
        addTerminalOutput('  clear/cls        Limpia la pantalla');
        addTerminalOutput('  neofetch         Info del sistema con logo');
        addTerminalOutput('  whoami           Usuario actual');
        addTerminalOutput('  exit/salir       Cierra la terminal');
        addTerminalOutput('');
        addTerminalOutput('<span style="color: #888888;">Archivos (Simulados):</span>');
        addTerminalOutput('  ls/dir           Lista archivos');
        addTerminalOutput('  cd [carpeta]     Cambia de directorio');
        addTerminalOutput('  pwd              Directorio actual');
        addTerminalOutput('  cat [archivo]    Muestra contenido');
        addTerminalOutput('  find [nombre]    Busca archivos');
        addTerminalOutput('  tree             Árbol de directorios');
        addTerminalOutput('');
        addTerminalOutput('<span style="color: #ff8800;">⚠️  NOTA: Esta es una demo web con archivos simulados</span>');
        addTerminalOutput('<span style="color: #ff8800;">   Para acceso REAL a archivos, descarga la versión Python</span>');
    } else if (command === 'cls' || command === 'clear' || command === 'limpiar') {
        output.innerHTML = '';
    } else if (command === 'neofetch') {
        const uptime = Math.floor((Date.now() - (window.bootTime || Date.now())) / 1000);
        addTerminalOutput('');
        const neofetch = `<span style="color: #00d4ff;">███╗   ██╗███████╗ ██████╗ </span>     <span style="color: #00ff00;">neo</span><span style="color: #ffffff;">@</span><span style="color: #00ff00;">demo-web</span>
<span style="color: #00d4ff;">████╗  ██║██╔════╝██╔═══██╗</span>     <span style="color: #888888;">--------------</span>
<span style="color: #00d4ff;">██╔██╗ ██║█████╗  ██║   ██║</span>     <span style="color: #00ff00;">OS:</span> NEO Intelligence v2.0
<span style="color: #00d4ff;">██║╚██╗██║██╔══╝  ██║   ██║</span>     <span style="color: #00ff00;">Tipo:</span> Demo Web (Simulado)
<span style="color: #00d4ff;">██║ ╚████║███████╗╚██████╔╝</span>     <span style="color: #00ff00;">Uptime:</span> ${uptime}s
<span style="color: #00d4ff;">╚═╝  ╚═══╝╚══════╝ ╚═════╝</span>     <span style="color: #00ff00;">Shell:</span> NEO Terminal
                                    <span style="color: #00ff00;">Directorio:</span> ${currentDirectory}`;
        const neofetchDiv = document.createElement('div');
        neofetchDiv.innerHTML = neofetch;
        output.appendChild(neofetchDiv);
        addTerminalOutput('');
    } else if (command === 'whoami') {
        addTerminalOutput('neo');
    } else if (command === 'ls' || command === 'dir') {
        const dir = getDirectoryContents(currentDirectory);
        if (dir && dir.type === 'dir' && dir.contents) {
            addTerminalOutput(`<span style="color: #00d4ff;">Contenido de ${currentDirectory}:</span>`);
            addTerminalOutput('');
            for (let name in dir.contents) {
                const item = dir.contents[name];
                if (item.type === 'dir') {
                    addTerminalOutput(`<span style="color: #00d4ff;">📁 ${name}/</span>`);
                } else {
                    addTerminalOutput(`<span style="color: #00ff00;">📄 ${name}</span>`);
                }
            }
        } else {
            addTerminalOutput('<span style="color: #ff4444;">[!]</span> Error al leer directorio');
        }
    } else if (command === 'cd') {
        if (args.length === 0) {
            currentDirectory = '/home/neo';
            addTerminalOutput('');
        } else {
            const newPath = resolvePath(args[0]);
            const dir = getDirectoryContents(newPath);
            if (dir && dir.type === 'dir') {
                currentDirectory = newPath;
                addTerminalOutput('');
            } else {
                addTerminalOutput(`<span style="color: #ff4444;">bash:</span> cd: ${args[0]}: No existe el directorio`);
            }
        }
    } else if (command === 'pwd') {
        addTerminalOutput(currentDirectory);
    } else if (command === 'cat') {
        if (args.length === 0) {
            addTerminalOutput('<span style="color: #ff4444;">[!]</span> Uso: cat [archivo]');
        } else {
            const filePath = resolvePath(args[0]);
            const parts = filePath.split('/').filter(p => p);
            const fileName = parts.pop();
            const dirPath = '/' + parts.join('/');
            const dir = getDirectoryContents(dirPath);
            
            if (dir && dir.contents && dir.contents[fileName]) {
                const file = dir.contents[fileName];
                if (file.type === 'file') {
                    addTerminalOutput('');
                    file.content.split('\n').forEach(line => addTerminalOutput(line));
                    addTerminalOutput('');
                } else {
                    addTerminalOutput(`<span style="color: #ff4444;">cat:</span> ${args[0]}: Es un directorio`);
                }
            } else {
                addTerminalOutput(`<span style="color: #ff4444;">cat:</span> ${args[0]}: No existe el archivo`);
            }
        }
    } else if (command === 'find') {
        if (args.length === 0) {
            addTerminalOutput('<span style="color: #ff4444;">[!]</span> Uso: find [nombre]');
        } else {
            const searchTerm = args[0].toLowerCase();
            addTerminalOutput(`<span style="color: #00d4ff;">[*]</span> Buscando archivos con "${searchTerm}"...`);
            addTerminalOutput('');
            
            function searchInDir(path, dir) {
                if (!dir.contents) return;
                for (let name in dir.contents) {
                    const fullPath = path === '/' ? '/' + name : path + '/' + name;
                    if (name.toLowerCase().includes(searchTerm)) {
                        const item = dir.contents[name];
                        if (item.type === 'dir') {
                            addTerminalOutput(`<span style="color: #00d4ff;">📁 ${fullPath}/</span>`);
                        } else {
                            addTerminalOutput(`<span style="color: #00ff00;">📄 ${fullPath}</span>`);
                        }
                    }
                    if (dir.contents[name].type === 'dir') {
                        searchInDir(fullPath, dir.contents[name]);
                    }
                }
            }
            
            searchInDir('', fileSystem['/']);
            addTerminalOutput('');
        }
    } else if (command === 'tree') {
        addTerminalOutput(`<span style="color: #00d4ff;">${currentDirectory}</span>`);
        
        function printTree(dir, prefix = '', isLast = true) {
            if (!dir.contents) return;
            const entries = Object.entries(dir.contents);
            entries.forEach(([name, item], index) => {
                const isLastEntry = index === entries.length - 1;
                const connector = isLastEntry ? '└── ' : '├── ';
                const color = item.type === 'dir' ? '#00d4ff' : '#00ff00';
                const icon = item.type === 'dir' ? '📁' : '📄';
                addTerminalOutput(`${prefix}${connector}<span style="color: ${color};">${icon} ${name}${item.type === 'dir' ? '/' : ''}</span>`);
                
                if (item.type === 'dir') {
                    const newPrefix = prefix + (isLastEntry ? '    ' : '│   ');
                    printTree(item, newPrefix, isLastEntry);
                }
            });
        }
        
        const dir = getDirectoryContents(currentDirectory);
        if (dir && dir.type === 'dir') {
            printTree(dir);
        }
    } else if (command === 'exit' || command === 'salir') {
        closeFloatingTerminal();
    } else if (command === '') {
        // No hacer nada
    } else {
        addTerminalOutput(`<span style="color: #ff4444;">bash:</span> ${cmd}: comando no encontrado`);
        addTerminalOutput(`<span style="color: #888;">Escribe 'ayuda' para ver comandos disponibles</span>`);
    }
    
    output.scrollTop = output.scrollHeight;
}

// Agregar al sistema de reconocimiento de voz
if (typeof processCommand !== 'undefined') {
    const originalProcessCommand = processCommand;
    processCommand = function(command) {
        if (command.includes('terminal') || command.includes('consola')) {
            openFloatingTerminal();
            speak('Terminal activada');
        } else if (command.includes('cierra terminal') || command.includes('oculta terminal')) {
            closeFloatingTerminal();
            speak('Terminal cerrada');
        } else {
            originalProcessCommand(command);
        }
    };
}
