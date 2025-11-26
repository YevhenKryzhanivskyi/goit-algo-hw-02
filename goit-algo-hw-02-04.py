import os
import shutil
import sys


def copy_files_recursively(src_dir, dest_dir):
    """Рекурсивно копіює файли та сортує їх за розширенням."""
    try:
        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)

            if os.path.isdir(src_path):
                copy_files_recursively(src_path, dest_dir)
            elif os.path.isfile(src_path):
                file_ext = os.path.splitext(item)[1].lower().strip('.')
                if not file_ext:
                    file_ext = 'no_extension'

                ext_dir = os.path.join(dest_dir, file_ext)
                os.makedirs(ext_dir, exist_ok=True)

                dest_path = os.path.join(ext_dir, item)
                try:
                    shutil.copy2(src_path, dest_path)
                    print(f"Файл: {src_path} скопійовано до {dest_path}")
                except (FileNotFoundError, PermissionError) as e:
                    print(f"Помилка копіювання файлу {src_path}: {e}")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Помилка доступу до директорії {src_dir}: {e}")


def main():
    """
    Запускає рекурсивне копіювання файлів із вихідної директорії
    до директорії призначення, сортує їх за розширенням.
    """
    if len(sys.argv) < 2:
        print(
            "Використання: python goit-algo-hw-02-04.py "
            "<source_directory> [<destination_directory>]"
        )
        return

    src_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    if not os.path.exists(src_dir) or not os.path.isdir(src_dir):
        print(
            f"Початкова директорія {src_dir} не існує "
            f"або не є директорією."
        )
        return

    os.makedirs(dest_dir, exist_ok=True)

    print(f"Копіювання файлів з директорії {src_dir} до {dest_dir}")
    copy_files_recursively(src_dir, dest_dir)
    print("Копіювання завершено.")


if __name__ == "__main__":
    main()
