from tkinter import Tk
from tkinter import filedialog

class FolderPicker:
    @staticmethod
    def select_folder():
        root = Tk()
        root.withdraw()  # Hide the main window
        root.attributes("-topmost", True)
        folder = filedialog.askdirectory(
            title="Select Backup Destination"
        )
        root.destroy()  # Clean up the Tkinter instance
        return folder