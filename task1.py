from pathlib import Path
import shutil
import argparse
import os

def copy_files(src_path: Path, dist_path: Path):
    for item in src_path.iterdir():
        if item.is_file() and os.access(item, os.R_OK):
            file_ext = item.suffix.lstrip('.')
            new_dir = dist_path / file_ext
            if not new_dir.exists():
                new_dir.mkdir(parents=True)
            shutil.copy2(item, new_dir / item.name)
        elif item.is_dir():
            copy_files(item, dist_path)


def main():
    parser = argparse.ArgumentParser(description="Description of your program")
    parser.add_argument("-s", "--src", required=True, help="soutce folder")
    parser.add_argument("-d", "--dist", required=False, default='dist', help="distination folder")

    args = parser.parse_args()

    src_path = Path(args.src)
    if not src_path.exists():
        print(f"{args.src} not exists")
        exit

    if not os.access(args.src, os.R_OK):
        print(f"{args.src} not readable")
        exit

    dist_path = Path(args.dist)
    if not dist_path.exists():
        dist_path.mkdir(parents=True)

    copy_files(src_path, dist_path)

if __name__ == "__main__":
    main()