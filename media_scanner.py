import subprocess
import os

class MediaScanner:
     PHOTO_EXTENSIONS = {
         '.jpg', '.jpeg', '.png', '.heic', '.webp'
     }
     VIDEO_EXTENSIONS = {
         '.mp4', '.mov', '.avi', '.mkv', '.webm', '.3gp'
     }
     DOCUMENT_EXTENSIONS = {
         '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt'
     }
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
            text=True,
            encoding="utf-8",
            errors="ignore"
        )
        return result.stdout if result.stdout else ""
     def get_all_files(self):
         print("\nScanning for device storage...\n")
         output = self.adb_shell(
                'find /storage/emulated/0 \
                ! -path "/storage/emulated/0/Android/*" \
                -type f'
            )
         files = []
         for line in output.splitlines():
                line = line.strip()
                if line:
                    files.append(line)
         return files
     def categorize_files(self, files):
            categorized = {
                "photos": [],
                "videos": [],
                "documents": [],
                "other": []
            }
            for file in files:
                extension = os.path.splitext(file)[1].lower()
                if extension in self.PHOTO_EXTENSIONS:
                    categorized["photos"].append(file)
                elif extension in self.VIDEO_EXTENSIONS:
                    categorized["videos"].append(file)
                elif extension in self.DOCUMENT_EXTENSIONS:
                    categorized["documents"].append(file)
                else:
                    categorized["other"].append(file)
            return categorized
            
     def build_statistics(self, categories):
         stats = {}
         for category, files in categories.items():
             stats[category] = {
                    "count": len(files)
             }
             
         return stats