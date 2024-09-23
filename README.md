# DuckDB File Conversion Benchmark 🦆

Comparison of file conversion between duckdb and pandas. On average, duckdb script is ~3x faster than pandas.

```txt
                duration
                    mean       std       min       max    median
converter_type
duckdb          0.707661  0.013660  0.696621  0.773661  0.704687
pandas          2.140695  0.030148  2.111300  2.255578  2.134108
```

Simulation results based on 30 iterations and 100k rows sampled from the machine learning subset of the [MMLU dataset](https://huggingface.co/datasets/lighteval/mmlu) `lighteval/mmlu`.

> Note: some additional performance overhead can be attributed to the python interpreter vs invoking duckdb directly from the shell. In fairness, the duckdb script runtime also includes checking if the system has the necessary dependencies and thus the performance difference is likely even more significant.

## Requirements

```bash
pip install -r requirements.txt
```

## Usage

### DuckDB script

```bash
./file-converter.sh <input_file> -f <output_format> [-o <output_file>] [-v]
```

### Python script

```bash
python file_converter.py <input_file> -f <output_format> [-o <output_file>] [-v]
```

### Simulation

To run the simulation:

```bash
python simulate.py
```
