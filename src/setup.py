# from cx_Freeze import setup, Executable
# import os.path
#
# PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
# os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
# os.environ['Tk_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
#
# base = "Win32GUI"  # Pour application graphique sous Windows
#
# options = {
#     'build_exe': {
#         'include_files': [
#             os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
#             os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
#             "images", "images/map.ico"
#         ],
#         'includes': ['pyvis'],
#         'packages': ['pygments'],
#
#
#     },
# }
#
# # options d'inclusion/exclusion des modules
# includes = ['pyvis']  # nommer les modules non trouves par cx_freeze
# excludes = []
# packages = ['pygments']  # nommer les packages utilises
#
# # copier les fichiers non-Python et/ou repertoires et leur contenu:
# includefiles = ["images"]
#
# # Paramètres de l'exécutable
# target = Executable(
#     script="MAP_Graphe_Mac.py",
#     copyright="Slackh",
#     base=base)
#
# setup(name="ERC-MAP FTW",
#       version="0.1",
#       options=options,
#       description="C'est un projet de stage",
#       executables=[target]
#       )

import sys, os
from cx_Freeze import setup, Executable

#############################################################################
# preparation des options

# chemins de recherche des modules
# ajouter d'autres chemins (absolus) si necessaire: sys.path + ["chemin1", "chemin2"]
path = sys.path

# options d'inclusion/exclusion des modules
includes = ['pyvis']  # nommer les modules non trouves par cx_freeze
excludes = []
packages = ['pygments']  # nommer les packages utilises

# copier les fichiers non-Python et/ou repertoires et leur contenu:
includefiles = ["images", "images/map.ico", "readme.txt"]

if sys.platform == "win32":
    pass
    # includefiles += [...] : ajouter les recopies specifiques à Windows
elif sys.platform == "linux2":
    pass
    # includefiles += [...] : ajouter les recopies specifiques à Linux
else:
    pass
    # includefiles += [...] : cas du Mac OSX non traite ici

# pour que les bibliotheques binaires de /usr/lib soient recopiees aussi sous Linux
binpathincludes = []
if sys.platform == "linux2":
    binpathincludes += ["/usr/lib"]

# niveau d'optimisation pour la compilation en bytecodes
optimize = 0

# si True, n'affiche que les warning et les erreurs pendant le traitement cx_freeze
silent = True

# construction du dictionnaire des options
options = {"path": path,
           "includes": includes,
           "excludes": excludes,
           "packages": packages,
           "include_files": includefiles,
           "bin_path_includes": binpathincludes,
           "optimize": optimize,
           "silent": silent
           }

# pour inclure sous Windows les dll system de Windows necessaires
if sys.platform == "win32":
    options["include_msvcr"] = True

#############################################################################
# preparation des cibles
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # pour application graphique sous Windows
    # base = "Console" # pour application en console sous Windows

icone = None
if sys.platform == "win32":
    icone = "images/map.ico"

cible_1 = Executable(
    script="MAP_Graphe.pyw",
    base=base,
    icon="images/map.ico"
)
#
# cible_2 = Executable(
#     script="MAP_Graphe.pyw",
#     base=base,
#     icon="images/map.ico"
# )

#############################################################################
# creation du setup
setup(
    name="MAP_Graphe",
    version="1.10",
    description="Projet Stage",
    author="Stanislas 'Slackh' Köhler",
    options={"build_exe": options},
    executables=[cible_1]
)
