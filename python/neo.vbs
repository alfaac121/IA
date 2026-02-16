Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")

' Obtener la ruta del script
strScriptPath = objFSO.GetParentFolderName(WScript.ScriptFullName)

' Ejecutar Python sin mostrar ventana
objShell.Run "pythonw """ & strScriptPath & "\neo_assistant_v2.py""", 0, False

Set objShell = Nothing
Set objFSO = Nothing
