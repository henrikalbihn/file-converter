#!/usr/bin/env bash

set -euo pipefail

DESCRIPTION="Convert an input file of {csv, parquet, json} format to {csv, parquet, json} format using Polars"
VERBOSE=false

usage() {
  echo "Usage: $0 <input_file> -f <output_format> [-o <output_file>] [-v]"
  echo "  <input_file>: Path to the input file"
  echo "  -f, --fmt: Output format {parquet, json, csv}"
  echo "  -o, --out: Output file path. If not specified, will use the input filename with new output format"
  echo "  -v, --verbose: Enable verbose output"
  echo "  -h, --help: Display this help message"
  echo "${DESCRIPTION}"
  exit 1
}

# Check if no arguments are provided
if [ $# -eq 0 ]; then
  usage
fi

# Parse command line arguments
INPUT_PATH=""
OUTPUT_FORMAT=""
OUTPUT_PATH=""

while [ $# -gt 0 ]; do
  case "$1" in
    -h|--help) usage ;;
    -f|--fmt) OUTPUT_FORMAT="$2"; shift ;;
    -o|--out) OUTPUT_PATH="$2"; shift ;;
    -v|--verbose) VERBOSE=true ;;
    -*)
      echo "Unknown option: $1"
      usage
      ;;
    *)
      if [ -z "$INPUT_PATH" ]; then
        INPUT_PATH="$1"
      else
        echo "Unexpected argument: $1"
        usage
      fi
      ;;
  esac
  shift
done

# Check if required arguments are provided
if [ -z "${INPUT_PATH}" ] || [ -z "${OUTPUT_FORMAT}" ]; then
  echo "Error: Both input file and output format must be specified."
  usage
fi

# If OUTPUT_PATH is not provided, use the same path as the input file
if [ -z "${OUTPUT_PATH}" ]; then
  OUTPUT_PATH="${INPUT_PATH%.*}.${OUTPUT_FORMAT}"
fi

# Function to check if Python is installed
check_python_installed() {
  if [[ "$OSTYPE" == "darwin"* ]]; then
    system="Darwin"
    DATE_CMD="gdate"
  elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    DATE_CMD="date"
    case "$(uname -m)" in
      x86_64) system="linux-amd64" ;;
      aarch64) system="linux-arm64" ;;
      *) echo "Unsupported Linux architecture"; exit 1 ;;
    esac
  else
    echo "Unsupported OS"; exit 1
  fi
  if ! command -v python3 &>/dev/null; then
    echo "Python3 could not be found. Please install Python3."
    exit 1
  fi
}

# Function to check if Polars is installed
check_polars_installed() {
  if ! python3 -c "import polars" &>/dev/null; then
    echo "Polars is not installed. Installing Polars..."
    if ! python3 -m pip install polars[all]; then
      echo "Failed to install Polars. Please install it manually."
      exit 1
    fi
  fi
}

file_to_file() {
  file_formats=("csv" "parquet" "json")
  this_file_format="${INPUT_PATH##*.}"
  this_file_format="${this_file_format,,}"  # Convert to lowercase

  if $VERBOSE; then
    echo "Input path: [${INPUT_PATH}]"
    echo "Output path: [${OUTPUT_PATH}]"
  fi

  if [[ ! " ${file_formats[*]} " =~ " ${this_file_format} " ]]; then
    echo "Invalid input file format: ${this_file_format}"
    exit 1
  fi

  if [[ ! " ${file_formats[*]} " =~ " ${OUTPUT_FORMAT} " ]]; then
    echo "Invalid output format: ${OUTPUT_FORMAT}"
    exit 1
  fi

  if $VERBOSE; then
    echo "Input format: [${this_file_format}]"
    echo "Output format: [${OUTPUT_FORMAT}]"
  fi

  # Prepare Python code
  PYTHON_CODE=$(cat <<END
import polars as pl
input_path = "${INPUT_PATH}"
output_path = "${OUTPUT_PATH}"
try:
    if "${this_file_format}" == "csv":
        df = pl.read_csv(input_path)
    elif "${this_file_format}" == "parquet":
        df = pl.read_parquet(input_path)
    elif "${this_file_format}" == "json":
        df = pl.read_json(input_path)
    else:
        raise ValueError("Unsupported input format")
    if "${OUTPUT_FORMAT}" == "csv":
        df.write_csv(output_path)
    elif "${OUTPUT_FORMAT}" == "parquet":
        df.write_parquet(output_path)
    elif "${OUTPUT_FORMAT}" == "json":
        df.write_json(output_path)
    else:
        raise ValueError("Unsupported output format")
except Exception as e:
    print(f"Error during file conversion: {e}")
    exit(1)
END
)

  if $VERBOSE; then
    echo "---------------------------------"
    echo "Python code to execute:"
    echo "${PYTHON_CODE}"
    echo "---------------------------------"
  fi
  start_time=$(${DATE_CMD} +%s.%3N)

  # Execute the Python code
  python3 -c "${PYTHON_CODE}"

  end_time=$(${DATE_CMD} +%s.%3N)
  duration=$(echo "$end_time - $start_time" | bc)

  echo "[${INPUT_PATH}] -> [${OUTPUT_PATH}]"
  printf "Conversion completed in %.4f seconds\n" "$duration"
}

main() {
  check_python_installed
  check_polars_installed
  file_to_file
}

main
