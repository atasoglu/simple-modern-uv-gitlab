from pathlib import Path

import copier


def main() -> None:
    pkg_dir = Path(__file__).parent
    # In a built wheel, copier.yml is included alongside this file.
    # In editable/dev mode, fall back to the project root (two levels up from src/pkg/).
    if not (pkg_dir / "copier.yml").exists():
        pkg_dir = pkg_dir.parent.parent
    copier.run_copy(str(pkg_dir))


if __name__ == "__main__":
    main()
