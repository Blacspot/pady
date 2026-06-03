import subprocess
import os

class DeviceScanner:
    def __init__(self, device_id):
        self.device_id = device_id

        self.common_folders = [
            ("DCIM", "/storage/emulated/0/DCIM"),
            ("Pictures", "/storage/emulated/0/Pictures"),
            ("Downloads", "/storage/emulated/0/Download"),
            ("Movies", "/storage/emulated/0/Movies"),
            ("Whatsapp", "/storage/emulated/0/Whatsapp"),
            ("AndroidMedia", "/storage/emulated/0/Android/media"),
        ]
    def folder_exists(self, path):
        cmd = [
            "adb",
            "-s",
            self.device_id,
            "shell",
            f"if [-d '{path}']; then echo EXISTS; fi"
        ]    

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )
        return "EXISTS" in result.stdout
    def scan(self):
        discovered = []
        print("\nScanning device storage...\n")
        for  name, path in self.common_folders:
            print(f"Checking {name}...")
            if self.folder_exists(path):
                discovered.append({
                    "name": name,
                    "path": path
                })
        return discovered        