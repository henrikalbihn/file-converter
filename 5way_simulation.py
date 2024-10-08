#!/usr/bin/env python3

import json
import os
import time
from datetime import datetime
from pathlib import Path
from textwrap import dedent
from typing import Literal

import duckdb
import fireducks.pandas as fd
import pandas as pd
import plotly.express as px
import polars as pl
from datafusion import SessionContext

INPUT_FILE = "data/mmlu-ml-100k.json"
INPUT_PATH = Path(INPUT_FILE).resolve()
assert INPUT_PATH.exists(), f"Input file not found: {INPUT_FILE}"
assert INPUT_PATH.suffix in [
    ".csv",
    ".parquet",
    ".json",
], "Input file must be a {CSV, Parquet, JSON} file"
INPUT_FILE = str(INPUT_PATH)

OUTPUT_FORMAT = "csv"
ITERATIONS = 100
OUTPUT_FILE = "data/simulation_results.json"


def get_input_format(input_file: str) -> Literal["csv", "parquet", "json"]:
    """Get the input format of the file.

    Args:
        input_file: The path to the input file.

    Returns:
        The input format of the file.
    """
    return input_file.split(".")[-1]


def run_converter(
    converter_type: Literal[
        "duckdb",
        "fireducks",
        "pandas",
        "polars",
        "datafusion",
    ],
    input_file: str,
    output_format: str,
) -> dict:
    """Run the converter and return the results.

    Args:
        converter_type: The type of converter to use. One of {duckdb, fireducks, pandas, polars, datafusion}.
        input_file: The path to the input file.
        output_format: The format to convert the file to.

    Returns:
        The results of the converter.
    """
    start_time = time.time()

    match converter_type:
        case "duckdb":
            duckdb_convert(input_file, output_format)
        case "pandas":
            pandas_convert(input_file, output_format)
        case "polars":
            polars_convert(input_file, output_format)
        case "fireducks":
            fireducks_convert(input_file, output_format)
        case "datafusion":
            datafusion_convert(input_file, output_format)
        case _:
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


def datafusion_convert(input_file: str, output_format: str) -> None:
    """Convert the input file to the output format using DataFusion.

    Args:
        input_file: The path to the input file.
        output_format: The format to convert the file to.
    """
    output_file = f"/tmp/output_datafusion.{output_format}"
    input_format = get_input_format(input_file)
    ctx = SessionContext()
    # Datafusion requires pathlib.Path objects
    input_file = Path(input_file).resolve()
    match input_format:
        case "json":
            df = ctx.read_json(input_file)
        case "csv":
            df = ctx.read_csv(input_file)
        case "parquet":
            df = ctx.read_parquet(input_file)
        case _:
            raise ValueError(f"Unknown input format: {input_format}")
    match output_format:
        case "csv":
            df.write_csv(output_file, with_header=True)
        case "parquet":
            df.write_parquet(output_file)
        case "json":
            df.write_json(output_file)
        case _:
            raise ValueError(f"Unknown output format: {output_format}")


def duckdb_convert(input_file: str, output_format: str) -> None:
    """Convert the input file to the output format using DuckDB.

    Args:
        input_file: The path to the input file.
        output_format: The format to convert the file to.
    """
    input_format = get_input_format(input_file)

    match input_format:
        case "json":
            input_format = "read_json_auto"
        case "csv":
            input_format = "read_csv_auto"
        case "parquet":
            input_format = "read_parquet"
        case _:
            raise ValueError(f"Unknown input format: {input_format}")

    match output_format:
        case "csv":
            format_args = "format csv"
        case "parquet":
            format_args = "format parquet"
        case "json":
            format_args = "format json, array true"
        case _:
            raise ValueError(f"Unknown output format: {output_format}")

    output_file = f"/tmp/output_duckdb.{output_format}"
    query = dedent(
        f"""
    COPY (FROM {input_format}('{input_file}'))
    TO '{output_file}'
    ({format_args});
    """
    )
    _ = duckdb.sql(query)


def pandas_convert(input_file: str, output_format: str) -> None:
    """Convert the input file to the output format using Pandas.

    Args:
        input_file: The path to the input file.
        output_format: The format to convert the file to.
    """
    output_file = f"/tmp/output_pandas.{output_format}"
    input_format = get_input_format(input_file)
    match input_format:
        case "json":
            df = pd.read_json(input_file)
        case "csv":
            df = pd.read_csv(input_file)
        case "parquet":
            df = pd.read_parquet(input_file)
        case _:
            raise ValueError(f"Unknown input format: {input_format}")
    match output_format:
        case "csv":
            df.to_csv(output_file, index=False)
        case "parquet":
            df.to_parquet(output_file, index=False)
        case "json":
            df.to_json(output_file, orient="records")


def fireducks_convert(input_file: str, output_format: str) -> None:
    """Convert the input file to the output format using FireDucks Pandas.

    Args:
        input_file: The path to the input file.
        output_format: The format to convert the file to.
    """
    output_file = f"/tmp/output_pandas.{output_format}"
    input_format = get_input_format(input_file)
    match input_format:
        case "json":
            df = fd.read_json(input_file)
        case "csv":
            df = fd.read_csv(input_file)
        case "parquet":
            df = fd.read_parquet(input_file)
        case _:
            raise ValueError(f"Unknown input format: {input_format}")
    match output_format:
        case "csv":
            df.to_csv(output_file, index=False)
        case "parquet":
            df.to_parquet(output_file, index=False)
        case "json":
            df.to_json(output_file, orient="records")


def polars_convert(input_file: str, output_format: str) -> None:
    """Convert the input file to the output format using Polars.

    Args:
        input_file: The path to the input file.
        output_format: The format to convert the file to.
    """
    output_file = f"/tmp/output_polars.{output_format}"
    input_format = get_input_format(input_file)
    match input_format:
        case "json":
            df = pl.read_json(input_file)
        case "csv":
            df = pl.read_csv(input_file)
        case "parquet":
            df = pl.read_parquet(input_file)
        case _:
            raise ValueError(f"Unknown input format: {input_format}")
    match output_format:
        case "csv":
            df.write_csv(output_file)
        case "parquet":
            df.write_parquet(output_file)
        case "json":
            df.write_json(output_file)


def monte_carlo(iterations: int = ITERATIONS) -> list:
    """Run the Monte Carlo simulation.

    Args:
        iterations: The number of iterations to run.

    Returns:
        The results of the simulation.
    """
    results = []
    for _ in range(iterations):
        results.extend(
            [
                run_converter("duckdb", INPUT_FILE, OUTPUT_FORMAT),
                run_converter("pandas", INPUT_FILE, OUTPUT_FORMAT),
                run_converter("polars", INPUT_FILE, OUTPUT_FORMAT),
                run_converter("fireducks", INPUT_FILE, OUTPUT_FORMAT),
                run_converter("datafusion", INPUT_FILE, OUTPUT_FORMAT),
            ]
        )
    return results


def save_results(results: list[dict]) -> None:
    with open(OUTPUT_FILE, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Results saved to [{OUTPUT_FILE}]")


def plot_results(results: list[dict]) -> None:
    """Plot the results of the simulation.

    Args:
        results: The results of the simulation.
    """
    df = pd.DataFrame(results)
    title = dedent(
        """
    Distribution of execution time (DuckDB vs Pandas vs Polars)
    <br>
    <span style='font-size: 0.8em; color: gray'>
        * lower is better
    </span>
    """
    )
    fig = px.histogram(
        df,
        x="duration",
        color="converter_type",
        opacity=0.6,
        marginal="violin",
        hover_data=df.columns,
        nbins=len(df),
        barmode="overlay",
        title=title,
        labels={"duration": "Execution Time (s)"},
    )
    fig.write_image("img/plot.png")
    print("Plot saved to [img/plot.png]")


def write_summary_stats(summary_stats: pd.DataFrame) -> None:
    """Write summary statistics to a file."""
    with open("data/summary_stats.txt", "w") as f:
        f.write(summary_stats.to_string())


def main() -> None:
    """Main function"""
    start_time = time.time()
    print(f"Running [{ITERATIONS}] iterations of the simulation...")
    results = monte_carlo()
    df = pd.DataFrame(results)
    agg_func = {"duration": ["mean", "std", "min", "max", "median"]}
    summary_stats = (
        df.groupby("converter_type")
        .agg(agg_func)
        .reset_index()
        # .sort_values("mean", ascending=True)
    )
    print(summary_stats)
    save_results(results)
    plot_results(results)
    write_summary_stats(summary_stats)
    end_time = time.time()

    # Clean up output files
    for file in Path("/tmp/").glob("output_*"):
        if file.suffix in [".csv", ".parquet", ".json"]:
            file.unlink()

    duration = end_time - start_time
    print(f"Complete! Total time: [{duration:.2f}s]")


if __name__ == "__main__":
    main()
