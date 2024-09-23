#!/usr/bin/env python3

import json
import subprocess
import time
from datetime import datetime
from typing import Literal

import pandas as pd

INPUT_FILE = "data/mmlu-ml-100k.json"
OUTPUT_FILE = "data/simulation_results.json"
OUTPUT_FORMAT = "csv"
ITERATIONS = 30


def run_converter(
    converter_type: Literal["duckdb", "pandas"],
    input_file: str,
    output_format: str,
) -> dict[str, float]:
    """Run the converter and return the duration

    Args:
        converter_type (Literal["duckdb", "pandas"]): The type of converter to use.
        input_file (str): The path to the input file.
        output_format (str): The format to convert to.

    Returns:
        dict[str, float]: The duration of the conversion.
    """
    start_time = time.time()

    if converter_type == "duckdb":
        subprocess.run(
            ["./file-converter.sh", input_file, "-f", output_format],
            check=True,
        )
    elif converter_type == "pandas":
        subprocess.run(
            ["python", "file_converter.py", input_file, "-f", output_format],
            check=True,
        )
    else:
        raise ValueError(f"Unknown converter type: {converter_type}")

    end_time = time.time()
    duration = end_time - start_time

    return {
        "start_time": datetime.fromtimestamp(start_time).isoformat(),
        "end_time": datetime.fromtimestamp(end_time).isoformat(),
        "duration": duration,
        "input_file": input_file,
        "output_format": output_format,
        "converter_type": converter_type,
    }


def execute() -> list[dict[str, dict[str, float]]]:
    """Execute the simulation and return the results

    Returns:
        list[dict[str, dict[str, float]]]: The results of the simulation.
    """
    return [
        run_converter("duckdb", INPUT_FILE, OUTPUT_FORMAT),
        run_converter("pandas", INPUT_FILE, OUTPUT_FORMAT),
    ]


def monte_carlo(
    iterations: int = ITERATIONS,
) -> list[dict[str, dict[str, float]]]:
    """Run the simulation multiple times and return the results

    Args:
        iterations (int, optional): The number of iterations to run. Defaults to ITERATIONS.

    Returns:
        list[dict[str, dict[str, float]]]: The results of the simulation.
    """
    results = []
    for _ in range(iterations):
        results.extend(execute())
    return results


def save_results(results: list[dict[str, dict[str, float]]]) -> None:
    """Save the results to a JSON file

    Args:
        results (list[dict[str, dict[str, float]]]): The results of the simulation.
    """
    with open(OUTPUT_FILE, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Results saved to [{OUTPUT_FILE}]")


def main() -> None:
    """Main function"""
    results = monte_carlo()
    df = pd.DataFrame(results)
    agg_func = {"duration": ["mean", "std", "min", "max", "median"]}
    summary_stats = df.groupby("converter_type").agg(agg_func)
    print(summary_stats)
    save_results(results)


if __name__ == "__main__":
    main()
