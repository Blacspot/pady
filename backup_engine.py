import subprocess
import zipfile
import os

class BackupEngine:
    def __init__(self, device_id):
        self.device_id = device_id
    def adb_shell(self, command):
        result = subprocess.run(
            [
                "adb",
                "-s",
                self.device_id,
                "shell",
                command
            ],
            capture_output=True,
            text=True
        )
        return result.stdout.strip()    
    def get_files(self, folder_path):
        command = (
            f'find "{folder_path}"'
            f'-type f'
        )
        output = self.adb_shell(command)
        files = [
            line.strip()
            for line in output.splitlines()
            if line.strip()
        ]
        return files
    def build_file_list(
            self,
            selected_folders
    ):
        all_files = []
        print("\nScanning files...\n")
        for folder in selected_folders:
            files = self.get_files(
                folder["path"]
            )
            print(
                f"{folder['name']}:"
                f"{len(files):,} files"
            )
            all_files.extend(files)
        return all_files