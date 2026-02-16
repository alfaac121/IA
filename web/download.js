// Script para descargar el paquete NEO Terminal
function downloadNEO() {
    // Crear un enlace temporal para descargar desde GitHub
    const downloadUrl = 'https://github.com/alfaac121/IA/archive/refs/heads/main.zip';
    
    // Crear elemento de enlace temporal
    const link = document.createElement('a');
    link.href = downloadUrl;
    link.download = 'NEO-Terminal-v2.0.zip';
    
    // Simular click
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    
    // Mostrar mensaje de descarga
    showDownloadMessage();
}

function showDownloadMessage() {
    // Crear mensaje de descarga
    const message = document.createElement('div');
    message.className = 'download-message';
    message.innerHTML = `
        <div class="download-content">
            <div class="download-icon">✅</div>
            <h3>¡Descarga iniciada!</h3>
            <p>El paquete NEO Terminal se está descargando...</p>
            <div class="download-steps">
                <h4>Próximos pasos:</h4>
                <ol>
                    <li>Extrae el archivo ZIP descargado</li>
                    <li>Abre la carpeta <code>IA-main/python</code></li>
                    <li>Ejecuta <code>install_simple.bat</code></li>
                    <li>Luego ejecuta <code>run_terminal.bat</code></li>
                </ol>
            </div>
            <button onclick="closeDownloadMessage()" class="btn-close">Entendido</button>
        </div>
    `;
    
    document.body.appendChild(message);
    
    // Auto cerrar después de 15 segundos
    setTimeout(() => {
        closeDownloadMessage();
    }, 15000);
}

function closeDownloadMessage() {
    const message = document.querySelector('.download-message');
    if (message) {
        message.style.opacity = '0';
        setTimeout(() => {
            message.remove();
        }, 300);
    }
}

// Agregar estilos para el mensaje
const style = document.createElement('style');
style.textContent = `
    .download-message {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.9);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 10000;
        animation: fadeIn 0.3s ease;
    }
    
    .download-content {
        background: #0a0a0a;
        border: 2px solid #00ff00;
        border-radius: 10px;
        padding: 40px;
        max-width: 500px;
        text-align: center;
        box-shadow: 0 0 30px rgba(0, 255, 0, 0.3);
    }
    
    .download-icon {
        font-size: 60px;
        margin-bottom: 20px;
        animation: bounce 0.5s ease;
    }
    
    .download-content h3 {
        color: #00ff00;
        margin-bottom: 10px;
        font-size: 24px;
    }
    
    .download-content p {
        color: #00d4ff;
        margin-bottom: 20px;
    }
    
    .download-steps {
        background: rgba(0, 255, 0, 0.05);
        border: 1px solid #00ff00;
        border-radius: 5px;
        padding: 20px;
        margin: 20px 0;
        text-align: left;
    }
    
    .download-steps h4 {
        color: #00ff00;
        margin-bottom: 10px;
        font-size: 16px;
    }
    
    .download-steps ol {
        color: #fff;
        padding-left: 20px;
        line-height: 1.8;
    }
    
    .download-steps code {
        background: rgba(0, 212, 255, 0.2);
        color: #00d4ff;
        padding: 2px 6px;
        border-radius: 3px;
        font-family: 'Courier New', monospace;
    }
    
    .btn-close {
        background: #00ff00;
        color: #000;
        border: none;
        padding: 12px 30px;
        border-radius: 5px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        margin-top: 20px;
        transition: all 0.3s ease;
    }
    
    .btn-close:hover {
        background: #00d4ff;
        transform: scale(1.05);
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
`;
document.head.appendChild(style);
