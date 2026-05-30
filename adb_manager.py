import subprocess
import json

class ADBManger:
    def __init__(self):
        self.device_id = None

    def run_adb(self, command):
        result = subprocess.run(
            ["adb"] + command,
            capture_output=True,
            text=True
        )
        return result.stdout.strip()

    def get_devices(self):
        output = self.run_adb(["devices"])
        lines = output.splitlines()[1:]
        devices = []
        for line in lines:
            if "\tdevice" in line:
                device_id = line.split("\t")[0]
                devices.append(device_id)
        return devices
    def detect_device(self):
        devices = self.get_devices()

        if not devices:
            return None
        self.device_id = devices[0]
        return self.device_id
    def get_device_info(self):
        if not self.device_id:
            return None

        model = self.run_adb(
            ["-s", self.device_id, "shell", "getprop", "ro.product.model"]
            ) 
        manufacturer = self.run_adb(
            ["-s", self.device_id, "shell", "getprop", "ro.product.manufacturer"]
            ) 
               
        
        android_version = self.run_adb(
            ["-s", self.device_id, "shell", "getprop", "ro.build.version.release"]
        )
        return {
            "device_id": self.device_id,
            "model": model,
            "manufacturer": manufacturer,
            "android_version": android_version
        }
    def is_device_ready(self):
        devices = self.get_devices()

        if not devices:
            return "NO_DEVICE"
        
        raw = self.run_adb(["devices"])
        if "unauthorized" in raw:
            return "UNAUTHORIZED"