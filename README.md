# Media Scanner

A Python-based tool for scanning, categorizing, and selecting media files on Android devices via ADB.

## Features

- Connects to Android devices using ADB
- Scans for files in device storage (excluding Android/system directories)
- Categorizes files into photos, videos, documents, and others
- Provides interactive selection of categories for backup
- Displays file counts and previews selected files

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

## Project Structure

- `main.py`: Entry point of the application.
- `media_scanner.py`: Core logic for scanning and categorizing files.
- `category_selector.py`: Interactive category selection menu.
- `adb_manager.py`: Handles ADB device communication and detection.
- `scanner.py`: Additional scanning utilities (if any).
- `backup_engine.py`: Handles backup operations (if implemented).
- `estimator.py`: Estimates storage usage (if implemented).
- `ui.py`: User interface components (if any).
- `selector.py`: File selection utilities (if any).
- `utils.py`: Helper functions.

## How It Works

1. `main.py` initializes the ADB manager and checks device connection.
2. `MediaScanner` scans the device storage for files using ADB shell commands.
3. Files are categorized based on file extensions.
4. `CategorySelector` presents a menu for the user to choose which categories to process.
5. Selected files are then available for further processing (e.g., backup, estimation).

## Notes

- The script currently scans `/storage/emulated/0` (primary shared storage) and excludes Android system directories.
- Ensure your device is authorized for USB debugging when prompted.
- This tool is for personal use; please respect privacy and copyright when handling media files.

## License

MIT