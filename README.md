# Media Scanner & Backup

A Python-based tool for scanning media files on Android devices via ADB, categorizing them, and performing backups as ZIP archives.

## Features

- Connects to Android devices using ADB
- Scans for files in device storage (excluding Android/system directories)
- Categorizes files into photos, videos, documents, and others
- Estimates backup size and free space before proceeding
- Interactive category selection for backup
- Copies selected files to a local workspace and creates a ZIP archive
- Device info display (model, manufacturer, Android version)

## Requirements

- Python 3.x
- ADB (Android Debug Bridge) installed and in PATH
- USB debugging enabled on the Android device

## Usage

1. Connect your Android device via USB and enable USB debugging.
2. Run the script: `python main.py`
3. Follow the prompts:
    - The script will check for a connected device.
    - It will scan for files and categorize them.
    - Select categories by entering numbers (e.g., "1,3" for photos and documents) or "A" for all.
    - Enter "Q" to quit.
    - Select a backup destination folder.
    - Review the backup estimate and confirm.
4. Files are copied to a temporary workspace and archived into a ZIP.

## Project Structure

- `main.py`: Entry point of the application.
- `adb_manager.py`: Handles ADB device communication and detection.
- `media_scanner.py`: Core logic for scanning and categorizing files.
- `category_selector.py`: Interactive category selection menu.
- `folder_picker.py`: UI for selecting backup destination folder.
- `backup_estimator.py`: Estimates backup size, duration, and workspace requirements.
- `estimate_ui.py`: Displays the backup estimate and confirmation prompt.
- `archive_namer.py`: Generates archive filenames based on device model.
- `workspace_manager.py`: Manages temporary directories for backup staging.
- `copy_engine.py`: Handles file copying from device via ADB.
- `zip_engine.py`: Creates ZIP archives from staged files.
- `utils.py`: Helper functions.

## How It Works

1. `main.py` initializes the ADB manager and checks device connection.
2. `ADBManger` detects the connected device and retrieves device info.
3. `MediaScanner` scans the device storage for files using ADB shell commands.
4. Files are categorized based on file extensions.
5. `CategorySelector` presents a menu for the user to choose which categories to process.
6. `FolderPicker` prompts the user for a backup destination.
7. `ArchiveNamer` generates a ZIP filename based on the device model.
8. `BackupEstimator` calculates total size, number of files, free space, and estimated time.
9. Files are copied from the device to a temporary workspace via `CopyEngine`.
10. `ZipEngine` creates a ZIP archive of the staged files.
11. `WorkspaceManager` cleans up the temporary directory.

## Notes

- The script scans `/storage/emulated/0` (primary shared storage) and excludes Android system directories.
- Ensure your device is authorized for USB debugging when prompted.
- This tool is for personal use; please respect privacy and copyright when handling media files.

## License

MIT
