"""Copy the original AI Excited artwork to the requested output directory."""

import os
from pathlib import Path


def main():
    source = Path(__file__).resolve().parent / "entry.png"
    data = source.read_bytes()
    if len(data) > 1024 * 1024:
        raise ValueError("Entry image exceeds the 1 MiB limit.")

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.png").write_bytes(data)


if __name__ == "__main__":
    main()
