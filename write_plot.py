import json

import pandas as pd
import plotly.express as px


def main() -> None:
    """Main function"""
    with open("data/simulation_results.json", "r") as f:
        data = json.load(f)
    df = pd.DataFrame(data)

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
    )
    fig.write_image("img/plot.png")


if __name__ == "__main__":
    main()
