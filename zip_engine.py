import os
import zipfile
from tkinter import Tk
from datetime import datetime

class ZipEngine:
    def __init__(self):
        self.root = Tk()
        self.root.withdraw()  # Hide the main window
    def select_source(self):
        """Select multiple files or a folder"""
        choice = input("Type 'f' for files or 'd' for directory: ").lower()

        if choice == 'f':
            files = file    