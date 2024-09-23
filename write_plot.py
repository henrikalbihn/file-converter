#!/usr/bin/env python3

import json

import pandas as pd
import plotly.express as px


def main() -> None:
    """Main function"""
    with open("data/simulation_results.json", "r") as f:
        data = json.load(f)
    df = pd.DataFrame(data)

    title = """
Distribution of execution time (duckdb vs pandas)
<br>
<span style='font-size: 0.8em; color: gray'>
    * lower is better
</span>
"""
    # overlap histogram of distribution of duration for each converter type
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
    )
    fig.write_image("img/plot.png")


if __name__ == "__main__":
    main()
