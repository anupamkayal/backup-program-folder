from  cx_Freeze import setup,Executable
setup(name="text_editor_simple",
author="Anupam",
version="0.2",
Executables=[Executable("""python file path""",
icon="""icon .ico path""",
shortcutname="Text editor",shortcutdir="DesktopFolder")]
)