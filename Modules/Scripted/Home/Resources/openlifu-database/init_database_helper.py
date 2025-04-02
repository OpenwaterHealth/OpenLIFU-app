import os
import shutil
import sys
from pathlib import Path

def copy_default_db_from_source_to_destination(destination, source):
    db_destination = Path(destination)
    db_source = Path(source)  # should be the default db
    db_destination.parent.mkdir(parents=True, exist_ok=True)

    # Copy the entire folder from source to destination
    if not db_destination.exists():
        shutil.copytree(db_source, db_destination)

    # Set perms
    if os.name == "nt":
        # On Windows: setting permissions to 777 is not exactly applicable
        os.system(f'icacls "{db_destination}" /grant Everyone:F /T /C')
    else:
        for root, dirs, files in os.walk(db_destination):
            for d in dirs:
                os.chmod(Path(root) / d, 0o777)
            for f in files:
                os.chmod(Path(root) / f, 0o777)
        os.chmod(db_destination, 0o777)
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: init_database_helper.py <db_destination>")
        sys.exit(1)

    copy_default_db_from_source_to_destination(sys.argv[1], sys.argv[2])
