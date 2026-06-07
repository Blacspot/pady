from adb_manager import ADBManger
from media_scanner import MediaScanner
from category_selector import CategorySelector
from estimate_ui import EstimateUI
from backup_estimator import BackupEstimator
from folder_picker import FolderPicker
import shutil
from archive_namer import ArchiveNamer
from workspace_manager import WorkspaceManager
from copy_engine import CopyEngine
from zip_engine import ZipEngine


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
    print(
        f"\nWelcome to Pady The Android Backup Tool!\n"
    )

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
    #selected_files = selected_files[:20]

    #print(
        #f"\nTEST MODE: Using only "
       # f"{len(selected_files)} files."
    #)
    
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
    archive_path = ArchiveNamer.generate(
        info['model'],
        destination
    )
    print(
        f"\nArchive will be created as:\n"
        f"\nArchive Path:\n{repr(archive_path)}"
    )

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
    temp_dir = WorkspaceManager.create(
        destination
    )

    copier = CopyEngine(
        device_id
    )

    copier.copy_files(
        selected_files,
        temp_dir
    )
    try:
         ZipEngine.create_zip(
            temp_dir,
            archive_path
        )

    except Exception as e:
        print(f"\nZIP Error: {e}")
        return

    WorkspaceManager.cleanup(
        temp_dir
    )

    print(
        "\nBackup completed successfully."
    )


if __name__ == "__main__":
    main()