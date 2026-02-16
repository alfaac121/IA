"""
NEO - Asistente de IA con Terminal Flotante
Versión Python con PyQt6 (SIN PyAudio)
Estilo Hacker Profesional - Sin emojis, con sonidos
"""

import sys
import json
import subprocess
import os
import time
import psutil
import winsound
from datetime import datetime
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QTextEdit, QLineEdit, QPushButton, QLabel, QGraphicsOpacityEffect)
from PyQt6.QtCore import Qt, QTimer, QThread, pyqtSignal, QSize, QPropertyAnimation, QEasingCurve, QPoint, QRect
from PyQt6.QtGui import QFont, QColor, QPalette, QIcon
import pyttsx3
import requests

class FloatingTerminal(QWidget):
    """Terminal flotante independiente"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_app = parent
        self.init_ui()
        self.command_history = []
        self.history_index = -1
        self.monitor_active = False
        self.monitor_timer = None
    
    def play_sound(self, sound_type):
        """Reproducir sonidos según la acción"""
        try:
            if sound_type == "command":
                # Sonido sutil al ejecutar comando
                winsound.Beep(600, 30)
            elif sound_type == "success":
                # Sonido de éxito (dos tonos rápidos)
                winsound.Beep(800, 40)
                winsound.Beep(1000, 40)
            elif sound_type == "error":
                # Sonido de error (tono bajo y corto)
                winsound.Beep(200, 80)
            elif sound_type == "monitor":
                # Sonido al iniciar monitor (tono único)
                winsound.Beep(1200, 60)
        except:
            pass  # Si falla el sonido, continuar sin él
        
    def init_ui(self):
        # Ventana flotante estilo Kali Linux - SIN BORDES
        self.setWindowFlags(
            Qt.WindowType.WindowStaysOnTopHint | 
            Qt.WindowType.FramelessWindowHint
        )
        
        # Layout principal
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Container con fondo marrón oscuro cálido
        container = QWidget()
        container.setStyleSheet("""
            QWidget {
                background-color: #1a1410;
                border: none;
            }
        """)
        
        container_layout = QVBoxLayout()
        container_layout.setContentsMargins(0, 0, 0, 0)
        
        # Header estilo Kali
        header = QHBoxLayout()
        header.setContentsMargins(10, 5, 10, 5)
        
        title = QLabel("neo@terminal")
        title.setStyleSheet("""
            QLabel {
                color: #d4a574;
                font-family: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;
                font-size: 12px;
                font-weight: normal;
                background: transparent;
                border: none;
            }
        """)
        
        # Botón minimizar
        minimize_btn = QPushButton("─")
        minimize_btn.setFixedSize(30, 30)
        minimize_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #d4a574;
                border: none;
                font-size: 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #d4a574;
                color: #1a1410;
            }
        """)
        minimize_btn.clicked.connect(self.showMinimized)
        
        close_btn = QPushButton("✕")
        close_btn.setFixedSize(30, 30)
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #d4a574;
                border: none;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #ff6b6b;
                color: #fff;
            }
        """)
        close_btn.clicked.connect(self.close_terminal)
        
        header.addWidget(title)
        header.addStretch()
        header.addWidget(minimize_btn)
        header.addWidget(close_btn)
        
        # Output area - Fondo marrón oscuro cálido
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setStyleSheet("""
            QTextEdit {
                background-color: #1a1410;
                color: #d4a574;
                font-family: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;
                font-size: 14px;
                border: none;
                padding: 20px;
            }
            QScrollBar:vertical {
                width: 0px;
            }
        """)
        self.output.setMinimumHeight(500)

        
        # Banner minimalista estilo Linux rice
        import platform
        cpu_info = f"{psutil.cpu_count(logical=False)} cores @ {psutil.cpu_freq().current:.0f}MHz" if psutil.cpu_freq() else f"{psutil.cpu_count(logical=False)} cores"
        mem = psutil.virtual_memory()
        mem_info = f"{mem.used / (1024**3):.1f}GB / {mem.total / (1024**3):.1f}GB"
        disk = psutil.disk_usage('/')
        
        self.output.setHtml(f"""
<pre style='line-height: 1.3; font-family: "JetBrains Mono", "Fira Code", "Consolas", monospace; font-size: 13px;'>

<span style='color: #d4a574;'>            ██████</span>                      <span style='color: #5eb3f6;'>usuario</span>   {os.getlogin()}
<span style='color: #d4a574;'>        ████░░░░░░████</span>                  <span style='color: #ff6b6b;'>os</span>        {platform.system()} {platform.release()}
<span style='color: #d4a574;'>      ██░░░░░░░░░░░░██</span>                <span style='color: #f9ca24;'>kernel</span>    {platform.version()[:35]}
<span style='color: #d4a574;'>    ██░░░░░░░░░░░░░░░░██</span>              <span style='color: #ff85c0;'>cpu</span>       {cpu_info}
<span style='color: #d4a574;'>    ██░░░░░░░░░░░░░░░░██</span>              <span style='color: #7bed9f;'>gpu</span>       Integrated Graphics
<span style='color: #d4a574;'>  ██░░░░░░░░░░░░░░░░░░░░██</span>            <span style='color: #ffa502;'>terminal</span>  NEO v2.0
<span style='color: #d4a574;'>  ██░░░░░░░░░░░░░░░░░░░░██</span>            <span style='color: #70a1ff;'>ram</span>       {mem_info}
<span style='color: #d4a574;'>  ██░░░░░░░░░░░░░░░░░░░░██</span>            <span style='color: #a29bfe;'>disk</span>      {disk.used / (1024**3):.0f}GB / {disk.total / (1024**3):.0f}GB
<span style='color: #d4a574;'>  ██░░░░░░░░░░░░░░░░░░░░██</span>
<span style='color: #d4a574;'>    ██░░░░░░░░░░░░░░░░██</span>
<span style='color: #d4a574;'>    ██░░░░░░░░░░░░░░░░██</span>
<span style='color: #d4a574;'>      ██░░░░░░░░░░░░██</span>
<span style='color: #d4a574;'>        ████░░░░░░████</span>
<span style='color: #d4a574;'>            ██████</span>

</pre>
""")
        self.add_output("type 'ayuda' for commands", "#888")
        self.add_output(f"{os.getcwd()}\n", "#888")
        
        # Input area estilo Kali
        input_layout = QHBoxLayout()
        input_layout.setContentsMargins(10, 5, 10, 10)
        input_layout.setSpacing(5)
        
        # Prompt en dos líneas
        prompt_widget = QWidget()
        prompt_layout = QVBoxLayout()
        prompt_layout.setContentsMargins(0, 0, 0, 0)
        prompt_layout.setSpacing(0)
        
        prompt_line1 = QLabel(f"{os.getlogin()}@neo")
        prompt_line1.setStyleSheet("""
            QLabel {
                color: #d4a574;
                font-family: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;
                font-size: 14px;
                background: transparent;
                border: none;
            }
        """)
        
        prompt_line2 = QLabel("~$")
        prompt_line2.setStyleSheet("""
            QLabel {
                color: #7bed9f;
                font-family: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;
                font-size: 14px;
                background: transparent;
                border: none;
            }
        """)
        
        prompt_layout.addWidget(prompt_line1)
        prompt_layout.addWidget(prompt_line2)
        prompt_widget.setLayout(prompt_layout)
        
        self.input = QLineEdit()
        self.input.setStyleSheet("""
            QLineEdit {
                background-color: #1a1410;
                color: #ffffff;
                font-family: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;
                font-size: 14px;
                border: none;
                padding: 5px;
            }
        """)
        self.input.returnPressed.connect(self.execute_command)
        self.input.installEventFilter(self)
        
        input_layout.addWidget(prompt_widget)
        input_layout.addWidget(self.input, 1)
        
        # Agregar todo al container
        container_layout.addLayout(header)
        container_layout.addWidget(self.output)
        container_layout.addLayout(input_layout)
        
        container.setLayout(container_layout)
        layout.addWidget(container)
        self.setLayout(layout)
        
        # Tamaño y posición
        self.setFixedSize(1000, 600)
        self.center_on_screen()
        
        # Variables para arrastrar
        self.dragging = False
        self.drag_position = None
        
        # Efecto de opacidad para animación
        self.opacity_effect = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.opacity_effect)
        self.opacity_effect.setOpacity(0)  # Empezar invisible
    
    def showEvent(self, event):
        """Evento al mostrar la ventana - ANIMACIÓN ÉPICA TIPO PORTAL"""
        super().showEvent(event)
        
        # Posición final (centro)
        screen = QApplication.primaryScreen().geometry()
        final_x = (screen.width() - self.width()) // 2
        final_y = (screen.height() - self.height()) // 2
        
        # EFECTO 1: Empezar invisible y muy pequeño en el centro
        center_x = final_x + 500  # Centro de la ventana
        center_y = final_y + 300
        
        self.setGeometry(center_x, center_y, 0, 0)
        self.setVisible(True)
        
        # ANIMACIÓN 1: Explosión desde el centro con REBOTE EXTREMO
        self.explosion_animation = QPropertyAnimation(self, b"geometry")
        self.explosion_animation.setDuration(2500)  # 2.5 SEGUNDOS - MUY LENTO
        self.explosion_animation.setStartValue(QRect(center_x, center_y, 0, 0))
        self.explosion_animation.setEndValue(QRect(final_x, final_y, 1000, 600))
        self.explosion_animation.setEasingCurve(QEasingCurve.Type.OutElastic)  # Rebote EXTREMO
        
        # ANIMACIÓN 2: Opacidad con efecto de materialización
        self.fade_animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.fade_animation.setDuration(2500)
        self.fade_animation.setStartValue(0)
        self.fade_animation.setEndValue(1)
        self.fade_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        
        # Iniciar animaciones
        self.explosion_animation.start()
        self.fade_animation.start()
        
        # EFECTO 3: Parpadeos tipo "materialización" - MUY ESPACIADOS
        QTimer.singleShot(300, lambda: self.opacity_effect.setOpacity(0.2))
        QTimer.singleShot(500, lambda: self.opacity_effect.setOpacity(0.6))
        QTimer.singleShot(700, lambda: self.opacity_effect.setOpacity(0.3))
        QTimer.singleShot(900, lambda: self.opacity_effect.setOpacity(0.8))
        QTimer.singleShot(1100, lambda: self.opacity_effect.setOpacity(0.4))
        QTimer.singleShot(1300, lambda: self.opacity_effect.setOpacity(0.9))
        
        # EFECTO 4: Sonidos sincronizados
        QTimer.singleShot(0, lambda: self.play_sound("monitor"))
        QTimer.singleShot(600, lambda: self.play_sound("command"))
        QTimer.singleShot(1200, lambda: self.play_sound("success"))
        QTimer.singleShot(1800, lambda: self.play_sound("command"))  # Sonido extra
    
    def close_terminal(self):
        """Cerrar con ANIMACIÓN ÉPICA - IMPLOSIÓN AL CENTRO"""
        current_geo = self.geometry()
        
        # Calcular el centro de la ventana actual
        center_x = current_geo.x() + 500
        center_y = current_geo.y() + 300
        
        # EFECTO 1: Parpadeos rápidos tipo "desmaterialización"
        QTimer.singleShot(0, lambda: self.opacity_effect.setOpacity(0.8))
        QTimer.singleShot(100, lambda: self.opacity_effect.setOpacity(0.4))
        QTimer.singleShot(200, lambda: self.opacity_effect.setOpacity(0.9))
        QTimer.singleShot(300, lambda: self.opacity_effect.setOpacity(0.3))
        QTimer.singleShot(400, lambda: self.opacity_effect.setOpacity(0.7))
        QTimer.singleShot(500, lambda: self.opacity_effect.setOpacity(0.2))
        QTimer.singleShot(600, lambda: self.opacity_effect.setOpacity(0.6))
        
        # ANIMACIÓN 1: Implosión hacia el centro con EFECTO ELÁSTICO EXTREMO
        self.implosion_animation = QPropertyAnimation(self, b"geometry")
        self.implosion_animation.setDuration(2000)  # 2 SEGUNDOS - MUY LENTO
        self.implosion_animation.setStartValue(current_geo)
        self.implosion_animation.setEndValue(QRect(center_x, center_y, 0, 0))
        self.implosion_animation.setEasingCurve(QEasingCurve.Type.InElastic)  # Elástico inverso EXTREMO
        
        # ANIMACIÓN 2: Fade out
        self.fade_out_animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.fade_out_animation.setDuration(2000)
        self.fade_out_animation.setStartValue(1)
        self.fade_out_animation.setEndValue(0)
        self.fade_out_animation.setEasingCurve(QEasingCurve.Type.InCubic)
        
        # Cerrar cuando termine
        self.implosion_animation.finished.connect(QApplication.quit)
        
        # Sonidos de cierre - MÁS ESPACIADOS
        QTimer.singleShot(0, lambda: self.play_sound("command"))
        QTimer.singleShot(500, lambda: self.play_sound("error"))
        QTimer.singleShot(1000, lambda: self.play_sound("command"))
        
        # Iniciar animaciones después de los parpadeos
        QTimer.singleShot(700, lambda: self.implosion_animation.start())
        QTimer.singleShot(700, lambda: self.fade_out_animation.start())
        
    def center_on_screen(self):
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)
    
    def eventFilter(self, obj, event):
        """Manejo de historial con flechas"""
        if obj == self.input and event.type() == event.Type.KeyPress:
            if event.key() == Qt.Key.Key_Up:
                if self.history_index > 0:
                    self.history_index -= 1
                    self.input.setText(self.command_history[self.history_index])
                return True
            elif event.key() == Qt.Key.Key_Down:
                if self.history_index < len(self.command_history) - 1:
                    self.history_index += 1
                    self.input.setText(self.command_history[self.history_index])
                else:
                    self.history_index = len(self.command_history)
                    self.input.clear()
                return True
        return super().eventFilter(obj, event)
    
    def mousePressEvent(self, event):
        """Iniciar arrastre"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragging = True
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
    
    def mouseMoveEvent(self, event):
        """Arrastrar ventana"""
        if self.dragging and event.buttons() == Qt.MouseButton.LeftButton:
            self.move(event.globalPosition().toPoint() - self.drag_position)
    
    def mouseReleaseEvent(self, event):
        """Terminar arrastre"""
        self.dragging = False
    
    def add_output(self, text, color="#d4a574"):
        """Agregar texto al output con efecto progresivo"""
        # Dividir el texto en líneas si tiene saltos de línea
        lines = text.split('\n')
        
        # Si es una sola línea corta, mostrarla directamente
        if len(lines) == 1 and len(text) < 100:
            self.output.append(f'<span style="color: {color};">{text}</span>')
            self.output.verticalScrollBar().setValue(
                self.output.verticalScrollBar().maximum()
            )
        else:
            # Mostrar líneas progresivamente
            self.add_lines_progressively(lines, 0, color)
    
    def add_lines_progressively(self, lines, index, color):
        """Agregar líneas progresivamente con delay"""
        if index < len(lines):
            if lines[index]:  # Solo agregar si la línea no está vacía
                self.output.append(f'<span style="color: {color};">{lines[index]}</span>')
            else:
                self.output.append('')  # Línea vacía
            
            QApplication.processEvents()
            self.output.verticalScrollBar().setValue(
                self.output.verticalScrollBar().maximum()
            )
            
            # Siguiente línea después de 20ms (más rápido)
            QTimer.singleShot(20, lambda: self.add_lines_progressively(lines, index + 1, color))
    
    def execute_command(self):
        """Ejecutar comando ingresado"""
        command = self.input.text().strip()
        if not command:
            return
        
        # Sonido al ejecutar comando
        self.play_sound("command")
        
        # Agregar al historial
        self.command_history.append(command)
        self.history_index = len(self.command_history)
        
        # Mostrar comando con prompt minimalista
        self.add_output(f"<span style='color: #d4a574;'>{os.getlogin()}@neo</span> <span style='color: #7bed9f;'>~$</span> <span style='color: #ffffff;'>{command}</span>", "#d4a574")
        self.input.clear()
        
        # Ejecutar comando con manejo de errores
        try:
            self.process_command(command)
        except Exception as e:
            self.add_output(f"error al ejecutar comando: {str(e)}", "#ff6b6b")
            self.play_sound("error")
            print(f"Error en comando '{command}': {e}")  # Debug en consola

    
    def process_command(self, command):
        """Procesar y ejecutar comandos"""
        parts = command.split()
        if not parts:
            return
        
        cmd = parts[0].lower()
        args = parts[1:]
        
        # Comandos personalizados
        if cmd in ["ayuda", "help"]:
            self.show_help()
        elif cmd in ["limpiar", "clear", "cls"]:
            # Limpiar con banner minimalista
            import platform
            cpu_info = f"{psutil.cpu_count(logical=False)} cores @ {psutil.cpu_freq().current:.0f}MHz" if psutil.cpu_freq() else f"{psutil.cpu_count(logical=False)} cores"
            mem = psutil.virtual_memory()
            mem_info = f"{mem.used / (1024**3):.1f}GB / {mem.total / (1024**3):.1f}GB"
            disk = psutil.disk_usage('/')
            
            self.output.setHtml(f"""
<pre style='line-height: 1.3; font-family: "JetBrains Mono", "Fira Code", "Consolas", monospace; font-size: 13px;'>

<span style='color: #d4a574;'>            ██████</span>                      <span style='color: #5eb3f6;'>usuario</span>   {os.getlogin()}
<span style='color: #d4a574;'>        ████░░░░░░████</span>                  <span style='color: #ff6b6b;'>os</span>        {platform.system()} {platform.release()}
<span style='color: #d4a574;'>      ██░░░░░░░░░░░░██</span>                <span style='color: #f9ca24;'>kernel</span>    {platform.version()[:35]}
<span style='color: #d4a574;'>    ██░░░░░░░░░░░░░░░░██</span>              <span style='color: #ff85c0;'>cpu</span>       {cpu_info}
<span style='color: #d4a574;'>    ██░░░░░░░░░░░░░░░░██</span>              <span style='color: #7bed9f;'>gpu</span>       Integrated Graphics
<span style='color: #d4a574;'>  ██░░░░░░░░░░░░░░░░░░░░██</span>            <span style='color: #ffa502;'>terminal</span>  NEO v2.0
<span style='color: #d4a574;'>  ██░░░░░░░░░░░░░░░░░░░░██</span>            <span style='color: #70a1ff;'>ram</span>       {mem_info}
<span style='color: #d4a574;'>  ██░░░░░░░░░░░░░░░░░░░░██</span>            <span style='color: #a29bfe;'>disk</span>      {disk.used / (1024**3):.0f}GB / {disk.total / (1024**3):.0f}GB
<span style='color: #d4a574;'>  ██░░░░░░░░░░░░░░░░░░░░██</span>
<span style='color: #d4a574;'>    ██░░░░░░░░░░░░░░░░██</span>
<span style='color: #d4a574;'>    ██░░░░░░░░░░░░░░░░██</span>
<span style='color: #d4a574;'>      ██░░░░░░░░░░░░██</span>
<span style='color: #d4a574;'>        ████░░░░░░████</span>
<span style='color: #d4a574;'>            ██████</span>

</pre>
""")
            self.play_sound("success")
        elif cmd in ["hora", "time"]:
            self.add_output(f"{datetime.now().strftime('%H:%M:%S')}")
        elif cmd in ["fecha", "date"]:
            self.add_output(f"{datetime.now().strftime('%d/%m/%Y - %A')}")
        elif cmd == "whoami":
            self.add_output(f"{os.getlogin()}")
        elif cmd == "pwd":
            self.add_output(f"{os.getcwd()}")
        elif cmd == "cpu":
            self.show_cpu_info()
        elif cmd == "ram":
            self.show_ram_info()
        elif cmd == "disk":
            self.show_disk_info()
        elif cmd == "info":
            self.show_system_info()
        elif cmd == "monitor":
            self.start_monitor()
        elif cmd == "stop":
            if self.monitor_active:
                self.stop_monitor()
            else:
                self.add_output("no hay monitor activo", "#888")
        elif cmd in ["dir", "ls"]:
            self.list_directory(args)
        elif cmd == "cd":
            self.change_directory(args)
        elif cmd in ["exit", "salir"]:
            self.add_output("usa el botón X para cerrar", "#888")
        else:
            # Ejecutar comando del sistema
            self.execute_system_command(command)
    
    def show_help(self):
        """Mostrar ayuda minimalista"""
        help_lines = [
            '',
            '<span style="color: #d4a574;">comandos disponibles:</span>',
            '',
            '<span style="color: #888888;">sistema</span>',
            '  <span style="color: #7bed9f;">ayuda</span>           muestra esta ayuda',
            '  <span style="color: #7bed9f;">clear</span>           limpia la terminal',
            '  <span style="color: #7bed9f;">info</span>            información del sistema',
            '  <span style="color: #7bed9f;">cpu</span>             información del CPU',
            '  <span style="color: #7bed9f;">ram</span>             información de RAM',
            '  <span style="color: #7bed9f;">disk</span>            información del disco',
            '  <span style="color: #7bed9f;">monitor</span>         monitor en tiempo real',
            '  <span style="color: #7bed9f;">stop</span>            detiene el monitor',
            '',
            '<span style="color: #888888;">archivos</span>',
            '  <span style="color: #7bed9f;">ls</span>              lista archivos',
            '  <span style="color: #7bed9f;">cd [ruta]</span>       cambia directorio',
            '  <span style="color: #7bed9f;">pwd</span>             directorio actual',
            '',
            '<span style="color: #888888;">otros comandos de sistema disponibles</span>',
            ''
        ]
        
        # Mostrar líneas progresivamente
        self.show_lines_progressively(help_lines, 0)
        self.play_sound("success")
    
    def show_lines_progressively(self, lines, index):
        """Mostrar líneas una por una con delay"""
        if index < len(lines):
            self.output.append(lines[index])
            QApplication.processEvents()
            self.output.verticalScrollBar().setValue(
                self.output.verticalScrollBar().maximum()
            )
            # Siguiente línea después de 20ms
            QTimer.singleShot(20, lambda: self.show_lines_progressively(lines, index + 1))
    
    def list_directory(self, args=None):
        """Listar archivos del directorio actual"""
        try:
            path = args[0] if args else os.getcwd()
            if not os.path.isabs(path):
                path = os.path.join(os.getcwd(), path)
            
            files = os.listdir(path)
            self.add_output(f"\n<span style='color: #888;'>{path}</span>\n")
            
            dirs = []
            files_list = []
            
            for f in files:
                full_path = os.path.join(path, f)
                if os.path.isdir(full_path):
                    dirs.append(f)
                else:
                    files_list.append(f)
            
            # Mostrar carpetas primero
            for d in sorted(dirs):
                self.add_output(f"  <span style='color: #5eb3f6;'>{d}/</span>")
            
            # Luego archivos
            for f in sorted(files_list):
                self.add_output(f"  <span style='color: #d4a574;'>{f}</span>")
            
            self.add_output(f"\n<span style='color: #888;'>{len(dirs)} carpetas, {len(files_list)} archivos</span>\n")
            self.play_sound("success")
        except Exception as e:
            self.add_output(f"error: {str(e)}", "#ff6b6b")
            self.play_sound("error")
    
    def change_directory(self, args):
        """Cambiar directorio"""
        if not args:
            home = os.path.expanduser("~")
            os.chdir(home)
            self.add_output(f"{os.getcwd()}")
            self.play_sound("success")
            return
        
        try:
            path = args[0]
            if path == "..":
                os.chdir("..")
            elif path == "~":
                os.chdir(os.path.expanduser("~"))
            else:
                os.chdir(path)
            self.add_output(f"{os.getcwd()}")
            self.play_sound("success")
        except Exception as e:
            self.add_output(f"error: {str(e)}", "#ff6b6b")
            self.play_sound("error")
    
    def show_cpu_info(self):
        """Mostrar información del CPU"""
        try:
            import platform
            cpu_count = psutil.cpu_count(logical=False)
            cpu_count_logical = psutil.cpu_count(logical=True)
            cpu_percent = psutil.cpu_percent(interval=1)
            cpu_freq = psutil.cpu_freq()
            
            self.add_output("")
            self.add_output(f"núcleos físicos    {cpu_count}")
            self.add_output(f"núcleos lógicos    {cpu_count_logical}")
            self.add_output(f"uso actual         {cpu_percent}%")
            if cpu_freq:
                self.add_output(f"frecuencia         {cpu_freq.current:.0f} MHz")
            self.add_output(f"arquitectura       {platform.machine()}")
            self.add_output("")
            self.play_sound("success")
        except Exception as e:
            self.add_output(f"error: {str(e)}", "#ff6b6b")
            self.play_sound("error")
    
    def show_ram_info(self):
        """Mostrar información de RAM"""
        try:
            mem = psutil.virtual_memory()
            mem_total_gb = mem.total / (1024**3)
            mem_used_gb = mem.used / (1024**3)
            mem_available_gb = mem.available / (1024**3)
            
            self.add_output("")
            self.add_output(f"total              {mem_total_gb:.2f} GB")
            self.add_output(f"usada              {mem_used_gb:.2f} GB ({mem.percent}%)")
            self.add_output(f"disponible         {mem_available_gb:.2f} GB")
            self.add_output("")
            self.play_sound("success")
        except Exception as e:
            self.add_output(f"error: {str(e)}", "#ff6b6b")
            self.play_sound("error")
    
    def show_disk_info(self):
        """Mostrar información del disco"""
        try:
            disk = psutil.disk_usage('/')
            disk_total_gb = disk.total / (1024**3)
            disk_used_gb = disk.used / (1024**3)
            disk_free_gb = disk.free / (1024**3)
            
            self.add_output("")
            self.add_output(f"total              {disk_total_gb:.2f} GB")
            self.add_output(f"usado              {disk_used_gb:.2f} GB ({disk.percent}%)")
            self.add_output(f"libre              {disk_free_gb:.2f} GB")
            self.add_output("")
            self.play_sound("success")
        except Exception as e:
            self.add_output(f"error: {str(e)}", "#ff6b6b")
            self.play_sound("error")
    
    def show_system_info(self):
        """Mostrar información completa del sistema"""
        try:
            import platform
            
            self.add_output("")
            self.add_output("<span style='color: #d4a574;'>información del sistema</span>")
            self.add_output("")
            
            # Sistema
            self.add_output(f"sistema            {platform.system()} {platform.release()}")
            self.add_output(f"versión            {platform.version()[:50]}")
            self.add_output(f"arquitectura       {platform.machine()}")
            self.add_output(f"hostname           {platform.node()}")
            self.add_output(f"usuario            {os.getlogin()}")
            
            # CPU
            cpu_count = psutil.cpu_count(logical=False)
            cpu_count_logical = psutil.cpu_count(logical=True)
            cpu_percent = psutil.cpu_percent(interval=1)
            self.add_output("")
            self.add_output(f"cpu                {cpu_count} núcleos físicos, {cpu_count_logical} lógicos")
            self.add_output(f"uso cpu            {cpu_percent}%")
            
            # RAM
            mem = psutil.virtual_memory()
            mem_total_gb = mem.total / (1024**3)
            mem_used_gb = mem.used / (1024**3)
            self.add_output("")
            self.add_output(f"ram total          {mem_total_gb:.2f} GB")
            self.add_output(f"ram usada          {mem_used_gb:.2f} GB ({mem.percent}%)")
            
            # Disco
            disk = psutil.disk_usage('/')
            disk_total_gb = disk.total / (1024**3)
            disk_used_gb = disk.used / (1024**3)
            self.add_output("")
            self.add_output(f"disco total        {disk_total_gb:.2f} GB")
            self.add_output(f"disco usado        {disk_used_gb:.2f} GB ({disk.percent}%)")
            
            # Procesos
            process_count = len(psutil.pids())
            self.add_output("")
            self.add_output(f"procesos activos   {process_count}")
            self.add_output("")
            
            self.play_sound("success")
        except Exception as e:
            self.add_output(f"error: {str(e)}", "#ff6b6b")
            self.play_sound("error")
    
    def start_monitor(self):
        """Iniciar monitor en tiempo real"""
        if self.monitor_active:
            self.add_output("monitor ya activo. usa 'stop' para detenerlo", "#ffa502")
            return
        
        self.monitor_active = True
        self.play_sound("monitor")
        self.add_output("")
        self.add_output("<span style='color: #7bed9f;'>monitor activado</span>")
        self.add_output("<span style='color: #888;'>actualizando cada 2s... (stop para detener)</span>")
        self.add_output("")
        
        # Crear timer para actualización
        self.monitor_timer = QTimer()
        self.monitor_timer.timeout.connect(self.update_monitor)
        self.monitor_timer.start(2000)  # Actualizar cada 2 segundos
        
        # Mostrar primera actualización
        self.update_monitor()
    
    def update_monitor(self):
        """Actualizar información del monitor"""
        if not self.monitor_active:
            return
        
        try:
            # LIMPIAR TODO y mostrar solo la info actualizada
            self.output.clear()
            
            # Header con hora actual
            self.output.append(f"<span style='color: #d4a574;'>monitor en vivo - {datetime.now().strftime('%H:%M:%S')}</span>")
            self.output.append("<span style='color: #888;'>actualizando cada 2s... (stop para detener)</span>")
            self.output.append("")
            
            # CPU
            cpu_percent = psutil.cpu_percent(interval=0.5)
            cpu_freq = psutil.cpu_freq()
            
            self.output.append(f"<span style='color: #d4a574;'>cpu</span> {psutil.cpu_count(logical=False)} núcleos físicos, {psutil.cpu_count(logical=True)} lógicos")
            if cpu_freq:
                self.output.append(f"<span style='color: #d4a574;'>freq</span> {cpu_freq.current:.0f} MHz")
            
            # Barra CPU
            bar_length = 30
            filled = int(bar_length * cpu_percent / 100)
            bar = "█" * filled + "░" * (bar_length - filled)
            color = "#7bed9f" if cpu_percent < 50 else "#ffa502" if cpu_percent < 80 else "#ff6b6b"
            self.output.append(f"<span style='color: #d4a574;'>uso</span> <span style='color: {color};'>[{bar}] {cpu_percent:.1f}%</span>")
            self.output.append("")
            
            # RAM
            mem = psutil.virtual_memory()
            mem_used_gb = mem.used / (1024**3)
            mem_total_gb = mem.total / (1024**3)
            
            filled = int(bar_length * mem.percent / 100)
            bar = "█" * filled + "░" * (bar_length - filled)
            color = "#7bed9f" if mem.percent < 50 else "#ffa502" if mem.percent < 80 else "#ff6b6b"
            self.output.append(f"<span style='color: #d4a574;'>ram</span> <span style='color: {color};'>[{bar}] {mem_used_gb:.2f}/{mem_total_gb:.2f} GB ({mem.percent:.1f}%)</span>")
            self.output.append("")
            
            # Disco
            disk = psutil.disk_usage('/')
            disk_used_gb = disk.used / (1024**3)
            disk_total_gb = disk.total / (1024**3)
            
            filled = int(bar_length * disk.percent / 100)
            bar = "█" * filled + "░" * (bar_length - filled)
            color = "#7bed9f" if disk.percent < 50 else "#ffa502" if disk.percent < 80 else "#ff6b6b"
            self.output.append(f"<span style='color: #d4a574;'>disk</span> <span style='color: {color};'>[{bar}] {disk_used_gb:.1f}/{disk_total_gb:.1f} GB ({disk.percent:.1f}%)</span>")
            self.output.append("")
            
            # Red
            net = psutil.net_io_counters()
            net_sent_mb = net.bytes_sent / (1024**2)
            net_recv_mb = net.bytes_recv / (1024**2)
            self.output.append(f"<span style='color: #d4a574;'>net</span> up {net_sent_mb:.1f} MB | down {net_recv_mb:.1f} MB")
            
            # Procesos
            process_count = len(psutil.pids())
            self.output.append(f"<span style='color: #d4a574;'>proc</span> {process_count} activos")
            
        except Exception as e:
            self.add_output(f"error en monitor: {str(e)}", "#ff6b6b")
            self.stop_monitor()
    
    def stop_monitor(self):
        """Detener monitor"""
        if self.monitor_timer:
            self.monitor_timer.stop()
            self.monitor_timer = None
        self.monitor_active = False
        self.add_output("")
        self.add_output("<span style='color: #ffa502;'>monitor detenido</span>", "#ffa502")
        self.add_output("")
        self.play_sound("success")
    
    def execute_system_command(self, command):
        """Ejecutar comando del sistema"""
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30,
                encoding='utf-8',
                errors='replace'
            )
            
            if result.stdout:
                lines = result.stdout.split('\n')
                for i, line in enumerate(lines):
                    if line.strip():
                        self.add_output(line)
                        QApplication.processEvents()
                        if i % 5 == 0:
                            time.sleep(0.05)
            
            if result.stderr:
                lines = result.stderr.split('\n')
                for line in lines:
                    if line.strip():
                        self.add_output(line, "#ffa502")
                        QApplication.processEvents()
            
            if result.returncode != 0 and not result.stdout and not result.stderr:
                self.add_output(f"código de error: {result.returncode}", "#ffa502")
            elif not result.stdout and not result.stderr and result.returncode == 0:
                self.add_output("ok")
                self.play_sound("success")
                
        except subprocess.TimeoutExpired:
            self.add_output("timeout (30s)", "#ff6b6b")
            self.play_sound("error")
        except FileNotFoundError:
            self.add_output(f"comando no encontrado: {command.split()[0]}", "#ff6b6b")
            self.add_output("verifica que el comando esté instalado o escribe 'ayuda'", "#888")
            self.play_sound("error")
        except Exception as e:
            self.add_output(f"error: {str(e)}", "#ff6b6b")
            self.play_sound("error")

def main():
    app = QApplication(sys.argv)
    
    # Crear y mostrar SOLO la terminal
    terminal = FloatingTerminal(None)
    terminal.show()
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
