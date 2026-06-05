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
         command = (
            'find /storage/emulated/0 '
            '! -path "/storage/emulated/0/Android/*" '
            '-type f '
            '-exec stat -c "%s|%n" {} \\;'
         )
         output = self.adb_shell(command)
         files = []
         for line in output.splitlines():
             if "|" not in line:
                 continue
             try:
                 size_str, path = line.split(
                    "|",
                    1
                 )
                 path = path.strip()
                 IGNORE_FOLDERS = [
                     "/.thumbnails/",
                     "/cache/",
                     "/Android/data/",
                     "/Android/obb/"
                 ]
                 if any(folder in path for folder in IGNORE_FOLDERS):
                     continue

                 files.append({
                     "path": path.strip(),
                     "size": int(size_str)
                 })

             except:
               pass
   
         return files
     def categorize_files(self, files):
            categorized = {
                "photos": [],
                "videos": [],
                "documents": [],
                "other": []
            }
            for file in files:
                extension = os.path.splitext(file["path"])[1].lower()
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
             total_size = sum(
                 file["size"] for file in files
             )
             
            
             stats[category] = {
                    "count": len(files),
                    "size": total_size
             }
             
         return stats
     def get_file_size(self, filepath):
         output = self.adb_shell(
                f'stat -c %s "{filepath}"'
         )
         try:
             return int(output.strip())
         except:
                return 0
         
     @staticmethod
     def format_size(size):

       units = [
           "B",
           "KB",
           "MB",
           "GB",
           "TB"
       ]

       for unit in units:

           if size < 1024:
               return f"{size:.2f} {unit}"

           size /= 1024

       return f"{size:.2f} PB"   