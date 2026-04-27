from pathlib import Path

import copier


def main() -> None:
    copier.run_copy(str(Path(__file__).parent))


if __name__ == "__main__":
    main()

