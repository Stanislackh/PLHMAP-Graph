from cx_Freeze import setup, Executable
import os.path

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['Tk_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

base = "Win32GUI"  # Pour application graphique sous Windows

options = {
    'build_exe': {
        'include_files': [
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll')
        ],
    },
}

setup(name="BlapBlap,",
      options=options,
      version="0.0.0.1",
      author="Slackh",
      description="Blap Blap ",
      executables=[Executable("InterfaceTkinterTestGraph.pyw", base=base, icon='icone.ico')]
      )
