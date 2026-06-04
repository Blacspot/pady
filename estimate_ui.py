from media_scanner import MediaScanner

class EstimateUI:
    @staticmethod
    def display(result, destination):
        print("\n")
        print("=" * 60)
        print("BACKUP ESTIMATE")
        print("=" * 60)

        print(
            f"Files Selected : "
            f"{result['total_files']:,}"
        )

        print(
            f"Backup Size : "
            f"{MediaScanner.format_size(result['total_size'])}"
        )

        print(
            f"Destination  : "
            f"{destination}"
        )

        print(
            f"Free Space   : "
            f"{MediaScanner.format_size(result['free_space'])}"
        )

        print(
            f"Estimated Time: "
            f"{result['min_time']} - "
            f"{result['max_time']} minutes"
        )
        print("=" * 60)
        

        if result["enough_space"]:
            print("\nEnough disk space available")
        else:
            print("\nInsufficient disk space")

        print("=" * 60)    

        return input(
            "\nProceed with backup? (Y/N): "
        ).strip().upper() == "Y"