"""
Convert an input file of {csv, parquet, json} format to {csv, parquet, json} format
"""

import argparse
import time
from pathlib import Path
from typing import Optional

import pandas as pd


def convert_file(
    input_path: Path,
    output_format: str,
    output_path: Optional[Path] = None,
) -> None:
    """Convert a file from one format to another.

    Args:
        input_path (Path): Path to the input file.
        output_format (str): Desired output format (csv, parquet, or json).
        output_path (Optional[Path], optional): Path for the output file. If not provided,
            uses the input filename with the new output format. Defaults to None.

    Raises:
        ValueError: If the input or output format is not supported.
    """
    start_time = time.time()

    # Determine input format
    input_format = input_path.suffix[1:].lower()

    # Read the input file
    if input_format == "csv":
        df = pd.read_csv(input_path)
    elif input_format == "parquet":
        df = pd.read_parquet(input_path)
    elif input_format == "json":
        df = pd.read_json(input_path)
    else:
        raise ValueError(f"Unsupported input format: {input_format}")

    # If output_path is not provided, use the same path as the input file
    if output_path is None:
        output_path = input_path.with_suffix(f".{output_format}")

    # Write the output file
    if output_format == "csv":
        df.to_csv(output_path, index=False)
    elif output_format == "parquet":
        df.to_parquet(output_path, index=False)
    elif output_format == "json":
        df.to_json(output_path, orient="records")
    else:
        raise ValueError(f"Unsupported output format: {output_format}")

    end_time = time.time()
    print(f"[{input_path}] -> [{output_path}]")
    print(f"Conversion completed in {end_time - start_time:.4f} seconds")


def main() -> None:
    """Main function"""
    parser = argparse.ArgumentParser(
        description="Convert an input file of {csv, parquet, json} format to {csv, parquet, json} format"
    )
    parser.add_argument("input_file", type=Path, help="Path to the input file")
    parser.add_argument(
        "-f",
        "--fmt",
        required=True,
        choices=["csv", "parquet", "json"],
        help="Output format",
    )
    parser.add_argument(
        "-o",
        "--out",
        type=Path,
        help="Output file path. If not specified, will use the input filename with new output format",
    )
    args = parser.parse_args()

    convert_file(args.input_file, args.fmt, args.out)


if __name__ == "__main__":
    main()
