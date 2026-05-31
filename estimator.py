import subprocess
import shutil
import re

class BackupEstimator:
    def __init__(self, device_id):
        self.device_id = device_id

    def _run_adb(self, command):
        result = subprocess.run(
            ["adb", "-s", self.device_id, "shell"] + command,
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    def get_folder_file_count(self, path):
        cmd = [
            "find",
            path,
            "-type",
            "f",
            "|",
            "wc",
            "-l"
        ]    
        output = self._run_adb(
            ["sh", "-c", "find '{}' -type f | wc -l".format(path)]
        )
        try:
            return int(output)
        except:
            return 0
    def get_folder_size_bytes(self, path):
        output = self._run_adb(
            ["du", "-sb", path]
        )    
        match = re.search(r"(\d+)", output)
        if match:
            return int(match.group(1))
        return 0
    
    @staticmethod
    def format_size(size):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024:
                return f"{size:.2f} {unit}"
            size /= 1024
        return f"{size:.2f} PB"
    def get_available_disk_space(self, destination):
        usage = shutil.disk_usage(destination)
        return usage.free
    def estimate_backup_time(self, total_size_bytes):
        gb = total_size_bytes / (1024 ** 3)
        low = max(1, round(gb / 4))
        high = max(2, round(gb / 2))
        return low, high
    def analyze(self, folders, destination):
        total_files = 0
        total_size = 0
        folder_stats = []
        print("\nCalculating estiimates...\n")

        for folder in folders:
            print(f"Analyzing {folder['name']}...")
            file_count = self.get_folder_file_count(folder["path"])
            size = self.get_folder_size_bytes(folder["path"])
            folder_stats.append({
                "name": folder["name"],
                "files": file_count,
                "size": size
            })
        free_space = self.get_available_disk_space(destination)
        low, high = self.estimate_backup_time(total_size)
        return {
            "folders": folder_stats,
            "total_files": total_files,
            "total_size": total_size,
            "free_space": free_space,
            "estimated_time": (low, high)
        }    