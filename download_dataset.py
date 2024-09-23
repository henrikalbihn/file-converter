import json
from pathlib import Path

import pandas as pd
from datasets import load_dataset

DATASET_ID = "lighteval/mmlu"
OUTPUT_FILE = "data/mmlu-ml-100k.json"


def download_dataset() -> None:
    """Download the dataset and save it to a file"""
    print("Downloading... Please wait.")
    dataset = load_dataset(DATASET_ID, "machine_learning")

    df = pd.concat(
        [
            dataset["auxiliary_train"].to_pandas(),
            dataset["test"].to_pandas(),
            dataset["validation"].to_pandas(),
            dataset["dev"].to_pandas(),
        ]
    )
    data = df.to_dict(orient="records")
    Path(OUTPUT_FILE).write_text(json.dumps(data, default=str))
    print(f"Wrote [{DATASET_ID}] to {OUTPUT_FILE}")


if __name__ == "__main__":
    download_dataset()
