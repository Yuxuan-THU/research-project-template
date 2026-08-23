"""Run the Python research pipeline in a deterministic file-name order.

Default stages:
    source/cleaning/*.py
    source/analysis/*.py

Optional collection stage:
    python replication/run_all.py --include-collection

Files beginning with an underscore are skipped. Any failed script stops the
pipeline immediately and returns a non-zero exit code.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def ensure_output_directories() -> None:
    for relative_path in (
        "outputs/data",
        "outputs/figures",
        "outputs/tables",
        "outputs/models",
        "outputs/other",
    ):
        (PROJECT_ROOT / relative_path).mkdir(parents=True, exist_ok=True)


def scripts_in(relative_directory: str) -> list[Path]:
    directory = PROJECT_ROOT / relative_directory
    return sorted(
        path
        for path in directory.glob("*.py")
        if path.is_file() and not path.name.startswith("_")
    )


def run_stage(label: str, relative_directory: str) -> None:
    scripts = scripts_in(relative_directory)
    print(f"\n=== {label} ===")
    if not scripts:
        print(f"No Python scripts found in {relative_directory}; skipping.")
        return

    for script in scripts:
        relative_script = script.relative_to(PROJECT_ROOT)
        print(f"Running {relative_script}")
        subprocess.run(
            [sys.executable, str(script)],
            cwd=PROJECT_ROOT,
            check=True,
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the research pipeline.")
    parser.add_argument(
        "--include-collection",
        action="store_true",
        help="Run data/collection/*.py before cleaning and analysis.",
    )
    args = parser.parse_args()

    ensure_output_directories()

    if args.include_collection:
        run_stage("DATA COLLECTION", "data/collection")

    run_stage("DATA CLEANING", "source/cleaning")
    run_stage("DATA ANALYSIS", "source/analysis")
    print("\nPipeline completed successfully.")


if __name__ == "__main__":
    main()
