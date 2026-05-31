from adb_manager import ADBManger
from scanner import DeviceScanner
from selector import FolderSelector
from estimator import BackupEstimator
from ui import show_estimate

def main():
    adb = ADBManger()
    status = adb.is_device_ready()
    if status == "NO_DEVICE":
        print("No device detected. Please connect your phone.")
        return
    if status == "UNAUTHORIZED":
        print("Device detected but unauthorized.")
        print("Please allow USB debugging on your phone.")
        return
    
    device_id = adb.detect_device()
    print(f"Device connected: {device_id}")
    info = adb.get_device_info()

    print("\n Device Info")
    print("----------------")
    print(f"Model: {info['model']}")
    print(f"Manufacturer: {info['manufacturer']}")
    print(f"Android: {info['android_version']}")

    scanner = DeviceScanner(device_id)
    folders = scanner.scan()
    print("\nDetected Folders")
    print("----------------")

    for index, folder in enumerate(folders,start=1):
        print(f"{index}. {folder['name']}")

    selected_folders = FolderSelector.select_folders(
        folders
        )
    if selected_folders is None:
        print("Backup cancelled.")
        exit()
    if not selected_folders:
        print("No folders selected. Exiting.")
        exit()
    print("\nSelected Folders")
    print("----------------")
    for folder in selected_folders:
        print(f"✓ {folder['name']}")    

    destination = input(
        "\nEnter backup destination path: "
    ).strip()
    estimator = BackupEstimator(
        device_id
    )
    results = estimator.analyze(
        selected_folders,
        destination
    )   
    proceed = show_estimate(results)
    if not proceed:
        print("\nBackup cancelled.")
        exit()     

if __name__ == "__main__":
    main()  