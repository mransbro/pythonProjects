#!python

from hashlib import md5
import os
from collections import defaultdict
import argparse
from rich.console import Console
from rich.table import Table


def find_duplicate_files(path):
    hashes = defaultdict(list)
    duplicates = {}

    try:
        for root, _, files in os.walk(path):
            for file_name in files:
                file_path = os.path.join(root, file_name)

                if not os.path.isfile(file_path):
                    continue

                with open(file_path, "rb") as file:
                    file_data = file.read()
                    file_hash = md5(file_data).hexdigest()
                
                hashes[file_hash].append(file_path)

        for hash_value, file_paths in hashes.items():
            if len(file_paths) > 1:
                duplicates[hash_value] = file_paths

        return duplicates

    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    my_parser = argparse.ArgumentParser(description="Find Duplicate Files")
    my_parser.add_argument("--filepath", help="File path to search for duplicate files.", action="store", type=str, dest='path')
    args = my_parser.parse_args()

    table = Table(title="Duplicate Files")
    table.add_column("File hash", style="cyan")
    table.add_column("Files", style="magenta")

    duplicates = find_duplicate_files(args.path)
   
    if duplicates:
        if len(duplicates) == 0:
            print("No duplicate files found.")
        else:
            for hash_value, file_paths in duplicates.items():
                table.add_row(hash_value, "\n".join(file_paths))
            console = Console()
            console.print(table)


if __name__ == "__main__":
    main()
