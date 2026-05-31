class FolderSelector:

    @staticmethod
    def select_folders(folders):
        while True:

            print("\n" + "=" * 50)
            print("Device Storage Scan Results")
            print("=" * 50)

            for i, folder in enumerate(folders, start=1):
                print(f"[{i}] {folder['name']}")
                print(f"  Path: {folder['path']}\n")

            print("=" * 50)
            print("Options:")
            print("A - Select All")
            print("N- Select None")
            print("Q - Quit")
            print()

            choice = input(
                "Enter folder numbers to select (comma separated), or choose an option: "
            ).strip().upper()
            if choice == "Q":
                return None
            if choice == "N":
                return []
            if choice == "A":
                return folders
            
            try:
                indexes = [
                    int(x.strip())
                    for x in choice.split(",")
                ]
                selected = []
                for index in indexes:
                    if 1 <= index <= len(folders):
                        selected.append(folders[index - 1])
                    if selected:
                        return selected
                    print("\nNo valid folders selected. \n")
            except ValueError:
                print("\nInvalid input.Try again.\n")        
