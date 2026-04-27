import sys
from pathlib import Path

import copier


def main() -> None:
    if len(sys.argv) > 1:
        dst_path = sys.argv[1]
    else:
        dst_path = input("Destination directory (e.g. ./my-project): ").strip()
        if not dst_path:
            print("Error: destination cannot be empty.")
            sys.exit(1)

    pkg_dir = Path(__file__).parent
    # In a built wheel, copier.yml is included alongside this file.
    # In editable/dev mode, fall back to the project root (two levels up from src/pkg/).
    if not (pkg_dir / "copier.yml").exists():
        pkg_dir = pkg_dir.parent.parent

    # vcs_ref="HEAD" forces copier to use the current working tree instead of
    # the latest git tag, so template changes are reflected immediately without
    # needing a new release tag.
    copier.run_copy(str(pkg_dir), dst_path, vcs_ref="HEAD")


if __name__ == "__main__":
    main()
