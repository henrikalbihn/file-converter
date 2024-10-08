# 5-Way Simulation Results
## Performance Plot
![Performance Plot](img/plot.png)
## Summary Statistics
```
  converter_type  duration                                        
                      mean       std       min       max    median
0         duckdb  0.946849  0.018945  0.913193  1.049822  0.946237
1      fireducks  1.049473  0.024370  1.013930  1.182517  1.043024
2         pandas  3.197043  0.031152  3.040715  3.259631  3.201332
3         polars  0.467181  0.042989  0.354204  0.646659  0.466661```
## Full Results
```json
[
  {
    "start_time": "2024-10-08T18:29:09.915333",
    "end_time": "2024-10-08T18:29:10.861739",
    "duration": 0.9464058876037598,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:29:10.861776",
    "end_time": "2024-10-08T18:29:13.902490",
    "duration": 3.0407145023345947,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:29:13.902514",
    "end_time": "2024-10-08T18:29:14.256719",
    "duration": 0.3542044162750244,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:29:14.256747",
    "end_time": "2024-10-08T18:29:15.380228",
    "duration": 1.123481035232544,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:29:15.380257",
    "end_time": "2024-10-08T18:29:16.322470",
    "duration": 0.9422132968902588,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:29:16.322500",
    "end_time": "2024-10-08T18:29:19.513309",
    "duration": 3.1908085346221924,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:29:19.513334",
    "end_time": "2024-10-08T18:29:20.041807",
    "duration": 0.528472900390625,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:29:20.041837",
    "end_time": "2024-10-08T18:29:21.073524",
    "duration": 1.0316870212554932,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:29:21.073549",
    "end_time": "2024-10-08T18:29:22.036746",
    "duration": 0.9631967544555664,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:29:22.036775",
    "end_time": "2024-10-08T18:29:25.204106",
    "duration": 3.1673312187194824,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:29:25.204136",
    "end_time": "2024-10-08T18:29:25.613361",
    "duration": 0.4092249870300293,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:29:25.613391",
    "end_time": "2024-10-08T18:29:26.718452",
    "duration": 1.1050612926483154,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:29:26.718478",
    "end_time": "2024-10-08T18:29:27.637394",
    "duration": 0.9189159870147705,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:29:27.637423",
    "end_time": "2024-10-08T18:29:30.823024",
    "duration": 3.1856017112731934,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:29:30.823048",
    "end_time": "2024-10-08T18:29:31.341281",
    "duration": 0.5182332992553711,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:29:31.341311",
    "end_time": "2024-10-08T18:29:32.373927",
    "duration": 1.032616138458252,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:29:32.373951",
    "end_time": "2024-10-08T18:29:33.296399",
    "duration": 0.922447919845581,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:29:33.296425",
    "end_time": "2024-10-08T18:29:36.472317",
    "duration": 3.1758921146392822,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:29:36.472342",
    "end_time": "2024-10-08T18:29:37.119001",
    "duration": 0.6466588973999023,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:29:37.119031",
    "end_time": "2024-10-08T18:29:38.184610",
    "duration": 1.0655794143676758,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:29:38.184638",
    "end_time": "2024-10-08T18:29:39.109800",
    "duration": 0.9251627922058105,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:29:39.109828",
    "end_time": "2024-10-08T18:29:42.206554",
    "duration": 3.0967259407043457,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:29:42.206577",
    "end_time": "2024-10-08T18:29:42.613614",
    "duration": 0.40703701972961426,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:29:42.613642",
    "end_time": "2024-10-08T18:29:43.650888",
    "duration": 1.037245750427246,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:29:43.650913",
    "end_time": "2024-10-08T18:29:44.572999",
    "duration": 0.9220867156982422,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:29:44.573028",
    "end_time": "2024-10-08T18:29:47.733270",
    "duration": 3.1602425575256348,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:29:47.733294",
    "end_time": "2024-10-08T18:29:48.137985",
    "duration": 0.4046907424926758,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:29:48.138013",
    "end_time": "2024-10-08T18:29:49.171145",
    "duration": 1.0331318378448486,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:29:49.171171",
    "end_time": "2024-10-08T18:29:50.084364",
    "duration": 0.9131927490234375,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:29:50.084393",
    "end_time": "2024-10-08T18:29:53.278040",
    "duration": 3.1936466693878174,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:29:53.278065",
    "end_time": "2024-10-08T18:29:53.760013",
    "duration": 0.481947660446167,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:29:53.760041",
    "end_time": "2024-10-08T18:29:54.784539",
    "duration": 1.0244982242584229,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:29:54.784564",
    "end_time": "2024-10-08T18:29:55.726102",
    "duration": 0.9415378570556641,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:29:55.726131",
    "end_time": "2024-10-08T18:29:58.927469",
    "duration": 3.201338052749634,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:29:58.927494",
    "end_time": "2024-10-08T18:29:59.390231",
    "duration": 0.4627366065979004,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:29:59.390259",
    "end_time": "2024-10-08T18:30:00.419798",
    "duration": 1.0295395851135254,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:30:00.419823",
    "end_time": "2024-10-08T18:30:01.334049",
    "duration": 0.9142255783081055,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:30:01.334077",
    "end_time": "2024-10-08T18:30:04.539045",
    "duration": 3.204968214035034,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:30:04.539070",
    "end_time": "2024-10-08T18:30:05.025352",
    "duration": 0.4862828254699707,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:30:05.025381",
    "end_time": "2024-10-08T18:30:06.085349",
    "duration": 1.0599677562713623,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:30:06.085377",
    "end_time": "2024-10-08T18:30:07.011209",
    "duration": 0.9258322715759277,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:30:07.011237",
    "end_time": "2024-10-08T18:30:10.243035",
    "duration": 3.2317981719970703,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:30:10.243061",
    "end_time": "2024-10-08T18:30:10.727912",
    "duration": 0.4848506450653076,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:30:10.727950",
    "end_time": "2024-10-08T18:30:11.779578",
    "duration": 1.051628828048706,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:30:11.779604",
    "end_time": "2024-10-08T18:30:12.730361",
    "duration": 0.9507577419281006,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:30:12.730390",
    "end_time": "2024-10-08T18:30:15.929964",
    "duration": 3.1995744705200195,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:30:15.929989",
    "end_time": "2024-10-08T18:30:16.388817",
    "duration": 0.4588277339935303,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:30:16.388845",
    "end_time": "2024-10-08T18:30:17.415842",
    "duration": 1.0269973278045654,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:30:17.415867",
    "end_time": "2024-10-08T18:30:18.362397",
    "duration": 0.9465301036834717,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:30:18.362426",
    "end_time": "2024-10-08T18:30:21.582316",
    "duration": 3.2198894023895264,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:30:21.582341",
    "end_time": "2024-10-08T18:30:22.077097",
    "duration": 0.49475598335266113,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:30:22.077127",
    "end_time": "2024-10-08T18:30:23.133312",
    "duration": 1.056185007095337,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:30:23.133337",
    "end_time": "2024-10-08T18:30:24.078478",
    "duration": 0.9451403617858887,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:30:24.078506",
    "end_time": "2024-10-08T18:30:27.295836",
    "duration": 3.21733021736145,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:30:27.295868",
    "end_time": "2024-10-08T18:30:27.850341",
    "duration": 0.5544731616973877,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:30:27.850371",
    "end_time": "2024-10-08T18:30:28.914314",
    "duration": 1.0639433860778809,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:30:28.914353",
    "end_time": "2024-10-08T18:30:29.964175",
    "duration": 1.0498218536376953,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:30:29.964221",
    "end_time": "2024-10-08T18:30:33.218374",
    "duration": 3.254153251647949,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:30:33.218399",
    "end_time": "2024-10-08T18:30:33.705325",
    "duration": 0.4869260787963867,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:30:33.705355",
    "end_time": "2024-10-08T18:30:34.758921",
    "duration": 1.0535664558410645,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:30:34.758951",
    "end_time": "2024-10-08T18:30:35.709431",
    "duration": 0.9504797458648682,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:30:35.709461",
    "end_time": "2024-10-08T18:30:38.934060",
    "duration": 3.2245991230010986,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:30:38.934089",
    "end_time": "2024-10-08T18:30:39.351768",
    "duration": 0.4176793098449707,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:30:39.351798",
    "end_time": "2024-10-08T18:30:40.389854",
    "duration": 1.038055419921875,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:30:40.389879",
    "end_time": "2024-10-08T18:30:41.329754",
    "duration": 0.9398758411407471,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:30:41.329783",
    "end_time": "2024-10-08T18:30:44.522949",
    "duration": 3.1931653022766113,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:30:44.522974",
    "end_time": "2024-10-08T18:30:44.959342",
    "duration": 0.4363672733306885,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:30:44.959390",
    "end_time": "2024-10-08T18:30:45.982789",
    "duration": 1.0233993530273438,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:30:45.982816",
    "end_time": "2024-10-08T18:30:46.951607",
    "duration": 0.9687910079956055,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:30:46.951636",
    "end_time": "2024-10-08T18:30:50.072416",
    "duration": 3.120779514312744,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:30:50.072441",
    "end_time": "2024-10-08T18:30:50.482740",
    "duration": 0.41029930114746094,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:30:50.482770",
    "end_time": "2024-10-08T18:30:51.553544",
    "duration": 1.0707733631134033,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:30:51.553569",
    "end_time": "2024-10-08T18:30:52.469194",
    "duration": 0.9156248569488525,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:30:52.469223",
    "end_time": "2024-10-08T18:30:55.681155",
    "duration": 3.2119319438934326,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:30:55.681181",
    "end_time": "2024-10-08T18:30:56.203890",
    "duration": 0.5227088928222656,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:30:56.203922",
    "end_time": "2024-10-08T18:30:57.231983",
    "duration": 1.0280609130859375,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:30:57.232008",
    "end_time": "2024-10-08T18:30:58.162568",
    "duration": 0.9305593967437744,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:30:58.162593",
    "end_time": "2024-10-08T18:31:01.337399",
    "duration": 3.174806833267212,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:31:01.337426",
    "end_time": "2024-10-08T18:31:01.747813",
    "duration": 0.4103868007659912,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:31:01.747842",
    "end_time": "2024-10-08T18:31:02.774891",
    "duration": 1.0270490646362305,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:31:02.774916",
    "end_time": "2024-10-08T18:31:03.709468",
    "duration": 0.9345519542694092,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:31:03.709497",
    "end_time": "2024-10-08T18:31:06.906297",
    "duration": 3.1967997550964355,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:31:06.906323",
    "end_time": "2024-10-08T18:31:07.326643",
    "duration": 0.4203200340270996,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:31:07.326672",
    "end_time": "2024-10-08T18:31:08.384775",
    "duration": 1.0581035614013672,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:31:08.384805",
    "end_time": "2024-10-08T18:31:09.316440",
    "duration": 0.9316344261169434,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:31:09.316469",
    "end_time": "2024-10-08T18:31:12.542852",
    "duration": 3.2263834476470947,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:31:12.542877",
    "end_time": "2024-10-08T18:31:13.028163",
    "duration": 0.48528623580932617,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:31:13.028192",
    "end_time": "2024-10-08T18:31:14.083423",
    "duration": 1.0552310943603516,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:31:14.083454",
    "end_time": "2024-10-08T18:31:15.018659",
    "duration": 0.9352054595947266,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:31:15.018690",
    "end_time": "2024-10-08T18:31:18.206017",
    "duration": 3.1873271465301514,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:31:18.206043",
    "end_time": "2024-10-08T18:31:18.626589",
    "duration": 0.4205460548400879,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:31:18.626618",
    "end_time": "2024-10-08T18:31:19.662470",
    "duration": 1.0358526706695557,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:31:19.662495",
    "end_time": "2024-10-08T18:31:20.584346",
    "duration": 0.9218509197235107,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:31:20.584374",
    "end_time": "2024-10-08T18:31:23.767283",
    "duration": 3.182908535003662,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:31:23.767310",
    "end_time": "2024-10-08T18:31:24.185338",
    "duration": 0.4180283546447754,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:31:24.185367",
    "end_time": "2024-10-08T18:31:25.246751",
    "duration": 1.0613834857940674,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:31:25.246776",
    "end_time": "2024-10-08T18:31:26.186545",
    "duration": 0.9397692680358887,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:31:26.186573",
    "end_time": "2024-10-08T18:31:29.446205",
    "duration": 3.259631395339966,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:31:29.446237",
    "end_time": "2024-10-08T18:31:29.997555",
    "duration": 0.5513186454772949,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:31:29.997587",
    "end_time": "2024-10-08T18:31:31.057055",
    "duration": 1.0594673156738281,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:31:31.057081",
    "end_time": "2024-10-08T18:31:32.063659",
    "duration": 1.0065782070159912,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:31:32.063711",
    "end_time": "2024-10-08T18:31:35.312455",
    "duration": 3.248744010925293,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:31:35.312482",
    "end_time": "2024-10-08T18:31:35.728678",
    "duration": 0.4161961078643799,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:31:35.728708",
    "end_time": "2024-10-08T18:31:36.794296",
    "duration": 1.0655887126922607,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:31:36.794328",
    "end_time": "2024-10-08T18:31:37.761050",
    "duration": 0.9667222499847412,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:31:37.761080",
    "end_time": "2024-10-08T18:31:41.013630",
    "duration": 3.2525506019592285,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:31:41.013654",
    "end_time": "2024-10-08T18:31:41.478492",
    "duration": 0.46483778953552246,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:31:41.478522",
    "end_time": "2024-10-08T18:31:42.519541",
    "duration": 1.0410182476043701,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:31:42.519567",
    "end_time": "2024-10-08T18:31:43.483658",
    "duration": 0.9640908241271973,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:31:43.483697",
    "end_time": "2024-10-08T18:31:46.713797",
    "duration": 3.23009991645813,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:31:46.713822",
    "end_time": "2024-10-08T18:31:47.173358",
    "duration": 0.4595358371734619,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:31:47.173385",
    "end_time": "2024-10-08T18:31:48.224524",
    "duration": 1.0511384010314941,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:31:48.224548",
    "end_time": "2024-10-08T18:31:49.175872",
    "duration": 0.9513239860534668,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:31:49.175901",
    "end_time": "2024-10-08T18:31:52.375342",
    "duration": 3.1994409561157227,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:31:52.375384",
    "end_time": "2024-10-08T18:31:52.791074",
    "duration": 0.41568970680236816,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:31:52.791104",
    "end_time": "2024-10-08T18:31:53.855306",
    "duration": 1.064201831817627,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:31:53.855330",
    "end_time": "2024-10-08T18:31:54.806078",
    "duration": 0.9507482051849365,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:31:54.806107",
    "end_time": "2024-10-08T18:31:58.003218",
    "duration": 3.197111129760742,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:31:58.003243",
    "end_time": "2024-10-08T18:31:58.437358",
    "duration": 0.434114933013916,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:31:58.437388",
    "end_time": "2024-10-08T18:31:59.466474",
    "duration": 1.029085397720337,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:31:59.466500",
    "end_time": "2024-10-08T18:32:00.417085",
    "duration": 0.950585126876831,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:32:00.417114",
    "end_time": "2024-10-08T18:32:03.618168",
    "duration": 3.2010538578033447,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:32:03.618195",
    "end_time": "2024-10-08T18:32:04.109265",
    "duration": 0.4910697937011719,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:32:04.109294",
    "end_time": "2024-10-08T18:32:05.183872",
    "duration": 1.0745782852172852,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:32:05.183941",
    "end_time": "2024-10-08T18:32:06.138864",
    "duration": 0.9549229145050049,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:32:06.138893",
    "end_time": "2024-10-08T18:32:09.341134",
    "duration": 3.2022416591644287,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:32:09.341166",
    "end_time": "2024-10-08T18:32:09.830784",
    "duration": 0.48961830139160156,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:32:09.830812",
    "end_time": "2024-10-08T18:32:10.871900",
    "duration": 1.0410878658294678,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:32:10.871926",
    "end_time": "2024-10-08T18:32:11.815435",
    "duration": 0.9435086250305176,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:32:11.815467",
    "end_time": "2024-10-08T18:32:15.014563",
    "duration": 3.199096202850342,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:32:15.014588",
    "end_time": "2024-10-08T18:32:15.478383",
    "duration": 0.4637949466705322,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:32:15.478411",
    "end_time": "2024-10-08T18:32:16.536956",
    "duration": 1.058544635772705,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:32:16.536980",
    "end_time": "2024-10-08T18:32:17.487226",
    "duration": 0.9502460956573486,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:32:17.487252",
    "end_time": "2024-10-08T18:32:20.673099",
    "duration": 3.1858460903167725,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:32:20.673124",
    "end_time": "2024-10-08T18:32:21.081568",
    "duration": 0.4084439277648926,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:32:21.081596",
    "end_time": "2024-10-08T18:32:22.108784",
    "duration": 1.0271883010864258,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:32:22.108816",
    "end_time": "2024-10-08T18:32:23.060975",
    "duration": 0.9521591663360596,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:32:23.061001",
    "end_time": "2024-10-08T18:32:26.255698",
    "duration": 3.194697856903076,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:32:26.255723",
    "end_time": "2024-10-08T18:32:26.708040",
    "duration": 0.4523169994354248,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:32:26.708070",
    "end_time": "2024-10-08T18:32:27.769671",
    "duration": 1.061601161956787,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:32:27.769696",
    "end_time": "2024-10-08T18:32:28.711143",
    "duration": 0.9414474964141846,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:32:28.711172",
    "end_time": "2024-10-08T18:32:31.893786",
    "duration": 3.182614326477051,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:32:31.893809",
    "end_time": "2024-10-08T18:32:32.331085",
    "duration": 0.43727588653564453,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:32:32.331115",
    "end_time": "2024-10-08T18:32:33.351499",
    "duration": 1.0203838348388672,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:32:33.351524",
    "end_time": "2024-10-08T18:32:34.304317",
    "duration": 0.9527935981750488,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:32:34.304354",
    "end_time": "2024-10-08T18:32:37.537567",
    "duration": 3.23321270942688,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:32:37.537593",
    "end_time": "2024-10-08T18:32:38.017713",
    "duration": 0.4801197052001953,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:32:38.017752",
    "end_time": "2024-10-08T18:32:39.105776",
    "duration": 1.0880234241485596,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:32:39.105835",
    "end_time": "2024-10-08T18:32:40.046921",
    "duration": 0.9410855770111084,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:32:40.046949",
    "end_time": "2024-10-08T18:32:43.244740",
    "duration": 3.197791337966919,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:32:43.244764",
    "end_time": "2024-10-08T18:32:43.703478",
    "duration": 0.45871400833129883,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:32:43.703507",
    "end_time": "2024-10-08T18:32:44.727993",
    "duration": 1.024486780166626,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:32:44.728018",
    "end_time": "2024-10-08T18:32:45.673683",
    "duration": 0.9456651210784912,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:32:45.673715",
    "end_time": "2024-10-08T18:32:48.875042",
    "duration": 3.201326608657837,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:32:48.875067",
    "end_time": "2024-10-08T18:32:49.334073",
    "duration": 0.45900630950927734,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:32:49.334100",
    "end_time": "2024-10-08T18:32:50.362853",
    "duration": 1.0287528038024902,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:32:50.362878",
    "end_time": "2024-10-08T18:32:51.305903",
    "duration": 0.9430255889892578,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:32:51.305932",
    "end_time": "2024-10-08T18:32:54.498661",
    "duration": 3.1927287578582764,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:32:54.498685",
    "end_time": "2024-10-08T18:32:54.958119",
    "duration": 0.45943331718444824,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:32:54.958147",
    "end_time": "2024-10-08T18:32:56.004105",
    "duration": 1.0459575653076172,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:32:56.004128",
    "end_time": "2024-10-08T18:32:56.949804",
    "duration": 0.9456758499145508,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:32:56.949833",
    "end_time": "2024-10-08T18:33:00.142021",
    "duration": 3.192188024520874,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:33:00.142048",
    "end_time": "2024-10-08T18:33:00.663531",
    "duration": 0.5214831829071045,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:33:00.663559",
    "end_time": "2024-10-08T18:33:01.701864",
    "duration": 1.0383050441741943,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:33:01.701890",
    "end_time": "2024-10-08T18:33:02.663310",
    "duration": 0.9614200592041016,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:33:02.663338",
    "end_time": "2024-10-08T18:33:05.870516",
    "duration": 3.2071781158447266,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:33:05.870541",
    "end_time": "2024-10-08T18:33:06.343483",
    "duration": 0.4729421138763428,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:33:06.343512",
    "end_time": "2024-10-08T18:33:07.407059",
    "duration": 1.0635476112365723,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:33:07.407085",
    "end_time": "2024-10-08T18:33:08.357327",
    "duration": 0.9502410888671875,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:33:08.357355",
    "end_time": "2024-10-08T18:33:11.552015",
    "duration": 3.194659948348999,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:33:11.552040",
    "end_time": "2024-10-08T18:33:11.964620",
    "duration": 0.4125792980194092,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:33:11.964658",
    "end_time": "2024-10-08T18:33:12.997591",
    "duration": 1.0329325199127197,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:33:12.997617",
    "end_time": "2024-10-08T18:33:13.946091",
    "duration": 0.9484736919403076,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:33:13.946120",
    "end_time": "2024-10-08T18:33:17.160981",
    "duration": 3.2148609161376953,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:33:17.161006",
    "end_time": "2024-10-08T18:33:17.673865",
    "duration": 0.512859582901001,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:33:17.673893",
    "end_time": "2024-10-08T18:33:18.712218",
    "duration": 1.0383245944976807,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:33:18.712284",
    "end_time": "2024-10-08T18:33:19.656372",
    "duration": 0.9440875053405762,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:33:19.656401",
    "end_time": "2024-10-08T18:33:22.838972",
    "duration": 3.1825709342956543,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:33:22.838998",
    "end_time": "2024-10-08T18:33:23.335179",
    "duration": 0.4961817264556885,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:33:23.335207",
    "end_time": "2024-10-08T18:33:24.357668",
    "duration": 1.0224604606628418,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:33:24.357694",
    "end_time": "2024-10-08T18:33:25.303410",
    "duration": 0.9457159042358398,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:33:25.303439",
    "end_time": "2024-10-08T18:33:28.511871",
    "duration": 3.2084319591522217,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:33:28.511895",
    "end_time": "2024-10-08T18:33:28.920356",
    "duration": 0.4084603786468506,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:33:28.920384",
    "end_time": "2024-10-08T18:33:29.964503",
    "duration": 1.0441193580627441,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:33:29.964528",
    "end_time": "2024-10-08T18:33:30.915562",
    "duration": 0.9510343074798584,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:33:30.915592",
    "end_time": "2024-10-08T18:33:34.041143",
    "duration": 3.125551223754883,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:33:34.041167",
    "end_time": "2024-10-08T18:33:34.449730",
    "duration": 0.40856289863586426,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:33:34.449759",
    "end_time": "2024-10-08T18:33:35.499680",
    "duration": 1.0499215126037598,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:33:35.499706",
    "end_time": "2024-10-08T18:33:36.454648",
    "duration": 0.9549424648284912,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:33:36.454678",
    "end_time": "2024-10-08T18:33:39.669435",
    "duration": 3.214756965637207,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:33:39.669464",
    "end_time": "2024-10-08T18:33:40.143003",
    "duration": 0.4735398292541504,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:33:40.143032",
    "end_time": "2024-10-08T18:33:41.184091",
    "duration": 1.0410590171813965,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:33:41.184120",
    "end_time": "2024-10-08T18:33:42.128171",
    "duration": 0.9440510272979736,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:33:42.128206",
    "end_time": "2024-10-08T18:33:45.303760",
    "duration": 3.1755530834198,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:33:45.303784",
    "end_time": "2024-10-08T18:33:45.770425",
    "duration": 0.4666404724121094,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:33:45.770452",
    "end_time": "2024-10-08T18:33:46.784382",
    "duration": 1.013929843902588,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:33:46.784408",
    "end_time": "2024-10-08T18:33:47.734565",
    "duration": 0.9501571655273438,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:33:47.734594",
    "end_time": "2024-10-08T18:33:50.904028",
    "duration": 3.16943359375,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:33:50.904053",
    "end_time": "2024-10-08T18:33:51.338979",
    "duration": 0.43492603302001953,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:33:51.339008",
    "end_time": "2024-10-08T18:33:52.374561",
    "duration": 1.035552978515625,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:33:52.374587",
    "end_time": "2024-10-08T18:33:53.321995",
    "duration": 0.9474079608917236,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:33:53.322023",
    "end_time": "2024-10-08T18:33:56.524567",
    "duration": 3.2025439739227295,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:33:56.524593",
    "end_time": "2024-10-08T18:33:57.052978",
    "duration": 0.5283851623535156,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:33:57.053004",
    "end_time": "2024-10-08T18:33:58.095750",
    "duration": 1.042745590209961,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:33:58.095777",
    "end_time": "2024-10-08T18:33:59.048340",
    "duration": 0.9525628089904785,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:33:59.048366",
    "end_time": "2024-10-08T18:34:02.244390",
    "duration": 3.1960244178771973,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:34:02.244416",
    "end_time": "2024-10-08T18:34:02.656675",
    "duration": 0.4122583866119385,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:34:02.656704",
    "end_time": "2024-10-08T18:34:03.694707",
    "duration": 1.0380034446716309,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:34:03.694762",
    "end_time": "2024-10-08T18:34:04.646691",
    "duration": 0.9519283771514893,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:34:04.646719",
    "end_time": "2024-10-08T18:34:07.852781",
    "duration": 3.206061840057373,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:34:07.852806",
    "end_time": "2024-10-08T18:34:08.350032",
    "duration": 0.4972257614135742,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:34:08.350060",
    "end_time": "2024-10-08T18:34:09.438107",
    "duration": 1.0880472660064697,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:34:09.438133",
    "end_time": "2024-10-08T18:34:10.405120",
    "duration": 0.966986894607544,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:34:10.405149",
    "end_time": "2024-10-08T18:34:13.624464",
    "duration": 3.2193143367767334,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:34:13.624490",
    "end_time": "2024-10-08T18:34:14.105886",
    "duration": 0.4813961982727051,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:34:14.105928",
    "end_time": "2024-10-08T18:34:15.185132",
    "duration": 1.0792038440704346,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:34:15.185156",
    "end_time": "2024-10-08T18:34:16.145559",
    "duration": 0.9604029655456543,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:34:16.145590",
    "end_time": "2024-10-08T18:34:19.352376",
    "duration": 3.206786632537842,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:34:19.352402",
    "end_time": "2024-10-08T18:34:19.846005",
    "duration": 0.4936037063598633,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:34:19.846033",
    "end_time": "2024-10-08T18:34:20.897043",
    "duration": 1.051009178161621,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:34:20.897070",
    "end_time": "2024-10-08T18:34:21.822918",
    "duration": 0.9258480072021484,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:34:21.822948",
    "end_time": "2024-10-08T18:34:25.034747",
    "duration": 3.2117998600006104,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:34:25.034774",
    "end_time": "2024-10-08T18:34:25.505169",
    "duration": 0.4703950881958008,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:34:25.505198",
    "end_time": "2024-10-08T18:34:26.542351",
    "duration": 1.0371530055999756,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:34:26.542376",
    "end_time": "2024-10-08T18:34:27.479387",
    "duration": 0.9370105266571045,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:34:27.479419",
    "end_time": "2024-10-08T18:34:30.683543",
    "duration": 3.2041239738464355,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:34:30.683569",
    "end_time": "2024-10-08T18:34:31.149851",
    "duration": 0.4662818908691406,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:34:31.149879",
    "end_time": "2024-10-08T18:34:32.213199",
    "duration": 1.0633208751678467,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:34:32.213224",
    "end_time": "2024-10-08T18:34:33.129629",
    "duration": 0.9164042472839355,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:34:33.129658",
    "end_time": "2024-10-08T18:34:36.301351",
    "duration": 3.171692371368408,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:34:36.301377",
    "end_time": "2024-10-08T18:34:36.731932",
    "duration": 0.4305553436279297,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:34:36.731961",
    "end_time": "2024-10-08T18:34:37.776380",
    "duration": 1.044419527053833,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:34:37.776412",
    "end_time": "2024-10-08T18:34:38.699041",
    "duration": 0.9226288795471191,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:34:38.699070",
    "end_time": "2024-10-08T18:34:41.911734",
    "duration": 3.2126641273498535,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:34:41.911760",
    "end_time": "2024-10-08T18:34:42.371754",
    "duration": 0.4599940776824951,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:34:42.371783",
    "end_time": "2024-10-08T18:34:43.439821",
    "duration": 1.068037509918213,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:34:43.439845",
    "end_time": "2024-10-08T18:34:44.364062",
    "duration": 0.9242165088653564,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:34:44.364091",
    "end_time": "2024-10-08T18:34:47.551436",
    "duration": 3.187345266342163,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:34:47.551461",
    "end_time": "2024-10-08T18:34:48.049243",
    "duration": 0.49778151512145996,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:34:48.049272",
    "end_time": "2024-10-08T18:34:49.079577",
    "duration": 1.0303044319152832,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:34:49.079602",
    "end_time": "2024-10-08T18:34:50.034973",
    "duration": 0.9553709030151367,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:34:50.035003",
    "end_time": "2024-10-08T18:34:53.254979",
    "duration": 3.2199766635894775,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:34:53.255006",
    "end_time": "2024-10-08T18:34:53.719945",
    "duration": 0.4649386405944824,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:34:53.719980",
    "end_time": "2024-10-08T18:34:54.783968",
    "duration": 1.0639886856079102,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:34:54.784034",
    "end_time": "2024-10-08T18:34:55.731006",
    "duration": 0.946972131729126,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:34:55.731034",
    "end_time": "2024-10-08T18:34:58.916502",
    "duration": 3.1854684352874756,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:34:58.916527",
    "end_time": "2024-10-08T18:34:59.409479",
    "duration": 0.4929521083831787,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:34:59.409509",
    "end_time": "2024-10-08T18:35:00.438268",
    "duration": 1.0287587642669678,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:35:00.438294",
    "end_time": "2024-10-08T18:35:01.377990",
    "duration": 0.9396963119506836,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:35:01.378019",
    "end_time": "2024-10-08T18:35:04.586900",
    "duration": 3.208880662918091,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:35:04.586925",
    "end_time": "2024-10-08T18:35:05.081874",
    "duration": 0.4949495792388916,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:35:05.081904",
    "end_time": "2024-10-08T18:35:06.155219",
    "duration": 1.073315143585205,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:35:06.155246",
    "end_time": "2024-10-08T18:35:07.102704",
    "duration": 0.947458028793335,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:35:07.102733",
    "end_time": "2024-10-08T18:35:10.307520",
    "duration": 3.204786539077759,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:35:10.307546",
    "end_time": "2024-10-08T18:35:10.804638",
    "duration": 0.49709200859069824,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:35:10.804666",
    "end_time": "2024-10-08T18:35:11.853196",
    "duration": 1.0485308170318604,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:35:11.853222",
    "end_time": "2024-10-08T18:35:12.803903",
    "duration": 0.950681209564209,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:35:12.803934",
    "end_time": "2024-10-08T18:35:16.015628",
    "duration": 3.2116942405700684,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:35:16.015652",
    "end_time": "2024-10-08T18:35:16.481831",
    "duration": 0.46617865562438965,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:35:16.481865",
    "end_time": "2024-10-08T18:35:17.551909",
    "duration": 1.0700445175170898,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:35:17.551935",
    "end_time": "2024-10-08T18:35:18.504231",
    "duration": 0.9522964954376221,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:35:18.504261",
    "end_time": "2024-10-08T18:35:21.745870",
    "duration": 3.2416083812713623,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:35:21.745899",
    "end_time": "2024-10-08T18:35:22.256155",
    "duration": 0.5102560520172119,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:35:22.256188",
    "end_time": "2024-10-08T18:35:23.438705",
    "duration": 1.1825170516967773,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:35:23.438748",
    "end_time": "2024-10-08T18:35:24.455941",
    "duration": 1.0171928405761719,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:35:24.455969",
    "end_time": "2024-10-08T18:35:27.652031",
    "duration": 3.196061611175537,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:35:27.652055",
    "end_time": "2024-10-08T18:35:28.108292",
    "duration": 0.4562375545501709,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:35:28.108321",
    "end_time": "2024-10-08T18:35:29.127062",
    "duration": 1.0187404155731201,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:35:29.127090",
    "end_time": "2024-10-08T18:35:30.077264",
    "duration": 0.9501743316650391,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:35:30.077293",
    "end_time": "2024-10-08T18:35:33.227099",
    "duration": 3.149806499481201,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:35:33.227123",
    "end_time": "2024-10-08T18:35:33.691619",
    "duration": 0.4644961357116699,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:35:33.691647",
    "end_time": "2024-10-08T18:35:34.727434",
    "duration": 1.0357868671417236,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:35:34.727458",
    "end_time": "2024-10-08T18:35:35.673526",
    "duration": 0.9460675716400146,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:35:35.673555",
    "end_time": "2024-10-08T18:35:38.878325",
    "duration": 3.2047696113586426,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:35:38.878350",
    "end_time": "2024-10-08T18:35:39.359729",
    "duration": 0.48137879371643066,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:35:39.359761",
    "end_time": "2024-10-08T18:35:40.403487",
    "duration": 1.0437264442443848,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:35:40.403520",
    "end_time": "2024-10-08T18:35:41.368750",
    "duration": 0.9652302265167236,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:35:41.368778",
    "end_time": "2024-10-08T18:35:44.576455",
    "duration": 3.2076761722564697,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:35:44.576481",
    "end_time": "2024-10-08T18:35:45.047220",
    "duration": 0.47073864936828613,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:35:45.047248",
    "end_time": "2024-10-08T18:35:46.098803",
    "duration": 1.0515551567077637,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:35:46.098829",
    "end_time": "2024-10-08T18:35:47.051363",
    "duration": 0.9525341987609863,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:35:47.051409",
    "end_time": "2024-10-08T18:35:50.229282",
    "duration": 3.1778736114501953,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:35:50.229307",
    "end_time": "2024-10-08T18:35:50.689322",
    "duration": 0.46001505851745605,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:35:50.689350",
    "end_time": "2024-10-08T18:35:51.729065",
    "duration": 1.0397148132324219,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:35:51.729118",
    "end_time": "2024-10-08T18:35:52.669379",
    "duration": 0.9402611255645752,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:35:52.669408",
    "end_time": "2024-10-08T18:35:55.872257",
    "duration": 3.2028491497039795,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:35:55.872282",
    "end_time": "2024-10-08T18:35:56.389046",
    "duration": 0.5167639255523682,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:35:56.389074",
    "end_time": "2024-10-08T18:35:57.479200",
    "duration": 1.0901260375976562,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:35:57.479225",
    "end_time": "2024-10-08T18:35:58.404712",
    "duration": 0.9254865646362305,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:35:58.404740",
    "end_time": "2024-10-08T18:36:01.589239",
    "duration": 3.1844992637634277,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:36:01.589266",
    "end_time": "2024-10-08T18:36:02.008366",
    "duration": 0.4190995693206787,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:36:02.008399",
    "end_time": "2024-10-08T18:36:03.045855",
    "duration": 1.037456750869751,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:36:03.045880",
    "end_time": "2024-10-08T18:36:03.961744",
    "duration": 0.9158637523651123,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:36:03.961772",
    "end_time": "2024-10-08T18:36:07.175984",
    "duration": 3.214212656021118,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:36:07.176012",
    "end_time": "2024-10-08T18:36:07.642693",
    "duration": 0.46668100357055664,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:36:07.642722",
    "end_time": "2024-10-08T18:36:08.730201",
    "duration": 1.0874783992767334,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:36:08.730226",
    "end_time": "2024-10-08T18:36:09.671892",
    "duration": 0.9416658878326416,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:36:09.671926",
    "end_time": "2024-10-08T18:36:12.813328",
    "duration": 3.1414012908935547,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:36:12.813352",
    "end_time": "2024-10-08T18:36:13.241372",
    "duration": 0.42801976203918457,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:36:13.241402",
    "end_time": "2024-10-08T18:36:14.283011",
    "duration": 1.041609287261963,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:36:14.283039",
    "end_time": "2024-10-08T18:36:15.233814",
    "duration": 0.9507744312286377,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:36:15.233844",
    "end_time": "2024-10-08T18:36:18.443597",
    "duration": 3.2097530364990234,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:36:18.443621",
    "end_time": "2024-10-08T18:36:18.864257",
    "duration": 0.4206359386444092,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:36:18.864286",
    "end_time": "2024-10-08T18:36:19.950142",
    "duration": 1.0858561992645264,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:36:19.950169",
    "end_time": "2024-10-08T18:36:20.892802",
    "duration": 0.9426333904266357,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:36:20.892831",
    "end_time": "2024-10-08T18:36:24.091617",
    "duration": 3.1987860202789307,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:36:24.091642",
    "end_time": "2024-10-08T18:36:24.568830",
    "duration": 0.4771873950958252,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:36:24.568858",
    "end_time": "2024-10-08T18:36:25.600940",
    "duration": 1.032081127166748,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:36:25.600970",
    "end_time": "2024-10-08T18:36:26.546718",
    "duration": 0.9457480907440186,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:36:26.546746",
    "end_time": "2024-10-08T18:36:29.755633",
    "duration": 3.2088868618011475,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:36:29.755660",
    "end_time": "2024-10-08T18:36:30.251328",
    "duration": 0.4956686496734619,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:36:30.251355",
    "end_time": "2024-10-08T18:36:31.291587",
    "duration": 1.0402324199676514,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:36:31.291613",
    "end_time": "2024-10-08T18:36:32.240413",
    "duration": 0.9487998485565186,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:36:32.240442",
    "end_time": "2024-10-08T18:36:35.431337",
    "duration": 3.1908950805664062,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:36:35.431360",
    "end_time": "2024-10-08T18:36:35.931911",
    "duration": 0.5005512237548828,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:36:35.931939",
    "end_time": "2024-10-08T18:36:36.961231",
    "duration": 1.0292916297912598,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:36:36.961256",
    "end_time": "2024-10-08T18:36:37.915423",
    "duration": 0.9541668891906738,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:36:37.915452",
    "end_time": "2024-10-08T18:36:41.132394",
    "duration": 3.2169418334960938,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:36:41.132421",
    "end_time": "2024-10-08T18:36:41.624143",
    "duration": 0.49172234535217285,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:36:41.624171",
    "end_time": "2024-10-08T18:36:42.667475",
    "duration": 1.0433030128479004,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:36:42.667505",
    "end_time": "2024-10-08T18:36:43.620873",
    "duration": 0.9533684253692627,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:36:43.620902",
    "end_time": "2024-10-08T18:36:46.859107",
    "duration": 3.2382044792175293,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:36:46.859131",
    "end_time": "2024-10-08T18:36:47.383244",
    "duration": 0.5241124629974365,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:36:47.383273",
    "end_time": "2024-10-08T18:36:48.434821",
    "duration": 1.0515475273132324,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:36:48.434870",
    "end_time": "2024-10-08T18:36:49.379880",
    "duration": 0.945009708404541,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:36:49.379909",
    "end_time": "2024-10-08T18:36:52.587514",
    "duration": 3.2076053619384766,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:36:52.587539",
    "end_time": "2024-10-08T18:36:53.046539",
    "duration": 0.4589993953704834,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:36:53.046567",
    "end_time": "2024-10-08T18:36:54.079778",
    "duration": 1.0332109928131104,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:36:54.079835",
    "end_time": "2024-10-08T18:36:55.023620",
    "duration": 0.943784236907959,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:36:55.023649",
    "end_time": "2024-10-08T18:36:58.215506",
    "duration": 3.191857099533081,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:36:58.215531",
    "end_time": "2024-10-08T18:36:58.685554",
    "duration": 0.47002220153808594,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:36:58.685582",
    "end_time": "2024-10-08T18:36:59.724372",
    "duration": 1.0387895107269287,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:36:59.724398",
    "end_time": "2024-10-08T18:37:00.668828",
    "duration": 0.9444305896759033,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:37:00.668856",
    "end_time": "2024-10-08T18:37:03.874654",
    "duration": 3.2057974338531494,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:37:03.874679",
    "end_time": "2024-10-08T18:37:04.395118",
    "duration": 0.5204386711120605,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:37:04.395147",
    "end_time": "2024-10-08T18:37:05.445085",
    "duration": 1.0499379634857178,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:37:05.445116",
    "end_time": "2024-10-08T18:37:06.406578",
    "duration": 0.9614622592926025,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:37:06.406605",
    "end_time": "2024-10-08T18:37:09.625747",
    "duration": 3.219142198562622,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:37:09.625774",
    "end_time": "2024-10-08T18:37:10.114254",
    "duration": 0.4884805679321289,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:37:10.114281",
    "end_time": "2024-10-08T18:37:11.184000",
    "duration": 1.0697181224822998,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:37:11.184024",
    "end_time": "2024-10-08T18:37:12.126958",
    "duration": 0.9429337978363037,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:37:12.126986",
    "end_time": "2024-10-08T18:37:15.327528",
    "duration": 3.20054292678833,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:37:15.327553",
    "end_time": "2024-10-08T18:37:15.841786",
    "duration": 0.5142331123352051,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:37:15.841814",
    "end_time": "2024-10-08T18:37:16.879741",
    "duration": 1.0379271507263184,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:37:16.879766",
    "end_time": "2024-10-08T18:37:17.823032",
    "duration": 0.9432656764984131,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:37:17.823060",
    "end_time": "2024-10-08T18:37:21.026544",
    "duration": 3.203483819961548,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:37:21.026570",
    "end_time": "2024-10-08T18:37:21.485725",
    "duration": 0.4591548442840576,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:37:21.485755",
    "end_time": "2024-10-08T18:37:22.508257",
    "duration": 1.0225026607513428,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:37:22.508282",
    "end_time": "2024-10-08T18:37:23.450182",
    "duration": 0.9418997764587402,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:37:23.450210",
    "end_time": "2024-10-08T18:37:26.651963",
    "duration": 3.2017531394958496,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:37:26.651987",
    "end_time": "2024-10-08T18:37:27.147262",
    "duration": 0.49527525901794434,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:37:27.147291",
    "end_time": "2024-10-08T18:37:28.186115",
    "duration": 1.0388233661651611,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:37:28.186140",
    "end_time": "2024-10-08T18:37:29.134559",
    "duration": 0.9484193325042725,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:37:29.134589",
    "end_time": "2024-10-08T18:37:32.341239",
    "duration": 3.2066497802734375,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:37:32.341265",
    "end_time": "2024-10-08T18:37:32.823613",
    "duration": 0.4823484420776367,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:37:32.823641",
    "end_time": "2024-10-08T18:37:33.846523",
    "duration": 1.0228822231292725,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:37:33.846549",
    "end_time": "2024-10-08T18:37:34.785509",
    "duration": 0.9389603137969971,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:37:34.785538",
    "end_time": "2024-10-08T18:37:37.986542",
    "duration": 3.2010037899017334,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:37:37.986571",
    "end_time": "2024-10-08T18:37:38.405727",
    "duration": 0.419156551361084,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:37:38.405757",
    "end_time": "2024-10-08T18:37:39.457339",
    "duration": 1.051581621170044,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:37:39.457365",
    "end_time": "2024-10-08T18:37:40.400659",
    "duration": 0.9432938098907471,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:37:40.400686",
    "end_time": "2024-10-08T18:37:43.502957",
    "duration": 3.102271795272827,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:37:43.502980",
    "end_time": "2024-10-08T18:37:44.000440",
    "duration": 0.49746036529541016,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:37:44.000469",
    "end_time": "2024-10-08T18:37:45.062472",
    "duration": 1.0620036125183105,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:37:45.062499",
    "end_time": "2024-10-08T18:37:46.008363",
    "duration": 0.9458639621734619,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:37:46.008391",
    "end_time": "2024-10-08T18:37:49.217911",
    "duration": 3.209520101547241,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:37:49.217938",
    "end_time": "2024-10-08T18:37:49.649843",
    "duration": 0.43190503120422363,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:37:49.649872",
    "end_time": "2024-10-08T18:37:50.690049",
    "duration": 1.0401771068572998,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:37:50.690074",
    "end_time": "2024-10-08T18:37:51.636748",
    "duration": 0.9466736316680908,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:37:51.636777",
    "end_time": "2024-10-08T18:37:54.816796",
    "duration": 3.180018424987793,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:37:54.816820",
    "end_time": "2024-10-08T18:37:55.227810",
    "duration": 0.41099023818969727,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:37:55.227839",
    "end_time": "2024-10-08T18:37:56.253717",
    "duration": 1.0258781909942627,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:37:56.253743",
    "end_time": "2024-10-08T18:37:57.214142",
    "duration": 0.9603993892669678,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:37:57.214171",
    "end_time": "2024-10-08T18:38:00.409295",
    "duration": 3.195124626159668,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:38:00.409322",
    "end_time": "2024-10-08T18:38:00.821903",
    "duration": 0.412581205368042,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:38:00.821931",
    "end_time": "2024-10-08T18:38:01.892114",
    "duration": 1.0701825618743896,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:38:01.892171",
    "end_time": "2024-10-08T18:38:02.847553",
    "duration": 0.9553811550140381,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:38:02.847581",
    "end_time": "2024-10-08T18:38:06.051339",
    "duration": 3.2037580013275146,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:38:06.051363",
    "end_time": "2024-10-08T18:38:06.511751",
    "duration": 0.46038818359375,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:38:06.511786",
    "end_time": "2024-10-08T18:38:07.580134",
    "duration": 1.0683484077453613,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:38:07.580165",
    "end_time": "2024-10-08T18:38:08.528373",
    "duration": 0.9482088088989258,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:38:08.528410",
    "end_time": "2024-10-08T18:38:11.747806",
    "duration": 3.219395160675049,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:38:11.747832",
    "end_time": "2024-10-08T18:38:12.157831",
    "duration": 0.40999913215637207,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:38:12.157860",
    "end_time": "2024-10-08T18:38:13.194708",
    "duration": 1.036848545074463,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:38:13.194734",
    "end_time": "2024-10-08T18:38:14.133543",
    "duration": 0.9388093948364258,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:38:14.133572",
    "end_time": "2024-10-08T18:38:17.336545",
    "duration": 3.202972888946533,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:38:17.336570",
    "end_time": "2024-10-08T18:38:17.829279",
    "duration": 0.4927084445953369,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:38:17.829306",
    "end_time": "2024-10-08T18:38:18.898788",
    "duration": 1.069481372833252,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:38:18.898813",
    "end_time": "2024-10-08T18:38:19.863278",
    "duration": 0.9644656181335449,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:38:19.863307",
    "end_time": "2024-10-08T18:38:23.056174",
    "duration": 3.1928672790527344,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:38:23.056198",
    "end_time": "2024-10-08T18:38:23.525080",
    "duration": 0.46888208389282227,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:38:23.525108",
    "end_time": "2024-10-08T18:38:24.548212",
    "duration": 1.0231046676635742,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:38:24.548238",
    "end_time": "2024-10-08T18:38:25.511101",
    "duration": 0.9628632068634033,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:38:25.511130",
    "end_time": "2024-10-08T18:38:28.718020",
    "duration": 3.206890106201172,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:38:28.718044",
    "end_time": "2024-10-08T18:38:29.233286",
    "duration": 0.515242338180542,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:38:29.233315",
    "end_time": "2024-10-08T18:38:30.295280",
    "duration": 1.061964750289917,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  },
  {
    "start_time": "2024-10-08T18:38:30.295305",
    "end_time": "2024-10-08T18:38:31.249682",
    "duration": 0.9543764591217041,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "duckdb"
  },
  {
    "start_time": "2024-10-08T18:38:31.249711",
    "end_time": "2024-10-08T18:38:34.447834",
    "duration": 3.198122262954712,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "pandas"
  },
  {
    "start_time": "2024-10-08T18:38:34.447861",
    "end_time": "2024-10-08T18:38:34.949512",
    "duration": 0.5016510486602783,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "polars"
  },
  {
    "start_time": "2024-10-08T18:38:34.949538",
    "end_time": "2024-10-08T18:38:35.981261",
    "duration": 1.0317225456237793,
    "input_file": "/home/runner/work/file-converter/file-converter/data/mmlu-ml-100k.json",
    "output_format": "csv",
    "converter_type": "fireducks"
  }
]```
