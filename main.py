from adb_manager import ADBManger
from media_scanner import MediaScanner
from category_selector import CategorySelector
from estimate_ui import EstimateUI
from backup_estimator import BackupEstimator
from folder_picker import FolderPicker
import shutil


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

    print("\nDevice Info")
    print("----------------")

    print(f"Model: {info['model']}")
    print(f"Manufacturer: {info['manufacturer']}")
    print(f"Android: {info['android_version']}")

    scanner = MediaScanner(device_id)

    all_files = scanner.get_all_files()
    print(f"\nDiscovered {len(all_files):,} files.")

    categories = scanner.categorize_files(
        all_files
    )

    stats = scanner.build_statistics(
        categories
    )

    selected_files = CategorySelector.select(
        categories,
        stats
    )

    if selected_files is None:
        print("Backup cancelled.")
        return
    print(
        "\nPlease select backup destination...."
    )
    destination = FolderPicker.select_folder()
    if not destination:
        print("\nNo destination selected.")
        return
    free_space = shutil.disk_usage(destination).free
    print(
        f"\nAvailable free space: "
        f"{MediaScanner.format_size(free_space)}"
        )
    print(f"\nSelected destination:\n{destination}")

    print(
        f"\nSelected {len(selected_files):,} files."
    )

    print("\nFirst 10 files detected:")

    for file in selected_files[:10]:
        print(
           f"{MediaScanner.format_size(file['size'])}"
           f" -> "
           f"{file['path']}"
        )
    estimate = BackupEstimator.estimate(
        selected_files,
        destination
    )

    proceed = EstimateUI.display(
        estimate,
        destination
    )

    if not proceed:
        print("\nBackup cancelled.")
        return    


if __name__ == "__main__":
    main()