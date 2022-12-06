import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Program Files (x86)\Python37-32\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Program Files (x86)\Python37-32\tcl\tk8.6"

executables = [cx_Freeze.Executable("Notepad Plus.py", base=base, icon="notpad.ico")]
									# python main file name/path 		icon file name/path

cx_Freeze.setup(
    name = "Notepad Plus", # Software name
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["notpad.ico",'tcl86t.dll','tk86t.dll',"Icon"]}},
    version = "1.01",														#icon file name/path ,2 dll file where python.exe install into this DLLS folder name ,icon folder
    author="anupam kayal", #creator name
    description = "Tkinter Application",
    executables = executables
    )
