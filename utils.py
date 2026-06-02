from pathlib import Path
from datetime import datetime

def generate_archive_name(
        device_name,
        destination
):
    today = datetime.now().strftime(
        "%Y-%m-%d"
        )
    safe_name = (
        device_name
        .replace(" ", "_")
        .replace("/", "_")
    )
    counter = 1
    while True:
        filename = (
            f"{safe_name}_"
            f"{today}_"
            f"{counter:03d}.zip"
        )
        full_path = (
            Path(destination) / filename
        )
        if not full_path.exists():
            return str(full_path)
        counter += 1