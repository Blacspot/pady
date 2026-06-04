import shutil

class BackupEstimator:
    @staticmethod
    def estimate(selected_files, stats, destination):
        total_size = 0
        for category in stats.values():
            total_size += category["size"]
        free_space = shutil.disk_usage(destination).free
        gb = total_size / (1024 ** 3)

        min_time = max(1, round(gb / 4))
        max_time = max(1, round(gb / 2))

        return {
            "size": total_size,
            "free_space": free_space,
            "min_time": min_time,
            "max_time": max_time
        }    