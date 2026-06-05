import os
import subprocess

class CopyEngine:
    def __init__(self, device_id):
        self.device_id = device_id
    def copy_files(
            self,
            selected_files,
            temp_dir
    )    :
        total_files = len(selected_files)
        for index, file in enumerate(
            selected_files,
            start=1
        ):
            source = file["path"]
            relative = source.replace(
                "/storage/emulated/0/",
                ""
            )
            destination = os.path.join(
                temp_dir,
                relative.replace("/", os.sep)
            )
            os.makedirs(
                os.path.dirname(destination),
                exist_ok=True
            )
            print(
               f"\rCopying"
               f"{index:,}/{total_files:,}", 
               end=""
            )
            subprocess.run(
                [
                    "adb",
                    "-s",
                    self.device_id,
                    "pull",
                    source,
                    destination
                ],
                capture_output=True,
            )
        print("\n")