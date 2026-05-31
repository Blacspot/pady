from estimator import BackupEstimator
def show_estimate(results):
    print("\n")
    print("=" * 60)
    print("Backup Estimate")
    print("=" * 60)

    for folder in results["folders"]:
        print(
            f"\n{folder['name']}"
        )
        print(
            f"Files : {folder['files']:,}"
        )
        print(
            f"Size : {BackupEstimator.format_size(folder['size'])}"
        )
    print("\n" + "=" * 60)
    print(
        f"Total Files: {results['total_files']:,}"
    )
    print(
        f"Total Size : "
        f"{BackupEstimator.format_size(results['total_size'])}"
    )
    low, high = results["estimated_time"]
    print(
        f"Estimated Time : "
        f"{low} - {high} minutes"
    )

    print(
        f"Available Space : "
        f"{BackupEstimator.format_size(results['free_space'])}"
    )
    print("=" * 60)
    if results["free_space"] < results["total_size"]:
        print("\n Insufficient Disk Space\n")
        return False
    print("\nSufficient Disk Space Available\n")
    choice = input(
        "Proceed with backup? (Y/N): "
    ).strip().upper()
    return choice == "Y"