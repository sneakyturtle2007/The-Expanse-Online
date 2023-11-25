#IMPORTS
import os
import subprocess
try:
    import shutil
except ImportError:
    
    subprocess.call(['pip', 'install', 'shutil'])
    import shutil
try:
    import tkinter as tk
    from tkinter import *
    from tkinter import filedialog
except ImportError:
    
    subprocess.call(['pip', 'install', 'tkinter'])
    import tkinter as tk
    from tkinter import *
    from tkinter import filedialog
try:
    from PIL import Image, ImageTk
except ImportError:
    
    subprocess.call(['pip', 'install', 'Pillow'])
    from PIL import Image
try:
    import lorem
except ImportError:
    
    subprocess.call(['pip', 'install', 'lorem'])
    import lorem

def settingUp_Interactables(window ):
    
    test = Button(window, bg="#424242", fg="#E6E6E6", text="Back", font=("Arial", 10))
    
    test.pack()
    test.place(x= 100, y = 100)