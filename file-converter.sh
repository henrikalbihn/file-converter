#!/usr/bin/env bash

set -euo pipefail

DESCRIPTION="Convert an input file of {csv, parquet, json} format to {csv, parquet, json} format"
DUCKDB_VERSION="1.1.0"
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
    -*) echo "Unknown option: $1"; usage ;;
    *)
      if [ -z "$INPUT_PATH" ]; then
        INPUT_PATH="$1"
      else
        echo "Unexpected argument: $1"; usage
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

# if OUTPUT_PATH is not provided, use the same path as the input file
if [ -z "${OUTPUT_PATH}" ]; then
  OUTPUT_PATH="${INPUT_PATH%.*}.${OUTPUT_FORMAT}"
fi

check_system() {
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

  if $VERBOSE; then
    echo "FILE CONVERTER"
    echo "---------------------------------"
    echo "Time: [$(date +%Y-%m-%d\ %H:%M:%S)]"
    echo "System: [${system}]"

  fi
}

check_duckdb_installed() {
  if ! command -v duckdb &> /dev/null; then
    echo "DuckDB could not be found"
    download_duckdb
  else
    duckdb_version=$(duckdb --version)
    if $VERBOSE; then
      echo "DuckDB version: [${duckdb_version}]"
    fi
  fi
}

download_duckdb() {
  case "${system}" in
    Darwin)
      if command -v brew &> /dev/null; then
        brew install duckdb
        brew install coreutils
      else
        echo "Homebrew is not installed. Please install Homebrew or DuckDB manually."
        exit 1
      fi
      ;;
    linux-amd64)
      bin_url="https://github.com/duckdb/duckdb/releases/download/v${DUCKDB_VERSION}/duckdb_cli-linux-amd64.zip"
      ;;
    linux-arm64)
      bin_url="https://github.com/duckdb/duckdb/releases/download/v${DUCKDB_VERSION}/duckdb_cli-linux-aarch64.zip"
      ;;
  esac

  if [ "${system}" != "Darwin" ]; then
    if command -v apt-get &> /dev/null; then
      sudo apt-get update
      sudo apt-get install -y unzip wget
    elif command -v yum &> /dev/null; then
      sudo yum install -y unzip wget
    else
      echo "Unsupported package manager. Please install unzip and wget manually."
      exit 1
    fi
    wget "${bin_url}" -O duckdb.zip
    unzip duckdb.zip
    chmod +x duckdb
    sudo mv duckdb /usr/local/bin/duckdb
  fi
}

file_to_file() {
  file_formats=("csv" "parquet" "json")
  this_file_format="${INPUT_PATH##*.}"

  if $VERBOSE; then
    echo "Input path: [${INPUT_PATH}]"
    echo "Output path: [${OUTPUT_PATH}]"
  fi

  if [[ ! " ${file_formats[*]} " =~ ${this_file_format} ]]; then
    echo "Invalid input file format: ${this_file_format}"
    exit 1
  fi

  case "${this_file_format}" in
    csv)
      if $VERBOSE; then echo "Input format: [CSV]"; fi
      input_format="read_csv_auto"
      ;;
    parquet)
      if $VERBOSE; then echo "Input format: [PARQUET]"; fi
      input_format="read_parquet"
      ;;
    json)
      if $VERBOSE; then echo "Input format: [JSON]"; fi
      input_format="read_json_auto"
      ;;
  esac

  case "${OUTPUT_FORMAT}" in
    parquet|json|csv)
      out_upper=$(echo "${OUTPUT_FORMAT}" | tr '[:lower:]' '[:upper:]')
      if $VERBOSE; then echo "Output format: [${out_upper}]"; fi
      ;;
    *) echo "Invalid output format: ${OUTPUT_FORMAT}"; exit 1 ;;
  esac

  # https://duckdb.org/docs/sql/statements/copy#format-specific-options
  format_args=""
  case "${OUTPUT_FORMAT}" in
    parquet) format_args="format parquet" ;;
    json) format_args="format json, array true" ;;
    csv) format_args="format csv" ;;
  esac

  start_time=$(${DATE_CMD} +%s.%3N)

  QUERY="
  copy (from ${input_format}('${INPUT_PATH}'))
  to '${OUTPUT_PATH}'
  (${format_args});"
  if $VERBOSE; then
    echo "---------------------------------"
    echo "Query: ${QUERY}"
    echo "---------------------------------"
  fi
  duckdb -c "${QUERY}"

  end_time=$(${DATE_CMD} +%s.%3N)
  duration=$(echo "$end_time - $start_time" | bc)

  echo "[${INPUT_PATH}] -> [${OUTPUT_PATH}]"
  printf "Conversion completed in %.4f seconds\n" "$duration"
}

main() {
  check_system
  check_duckdb_installed
  file_to_file
}

main
