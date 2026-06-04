# MOSFET Characterization Plotter

A tool for parsing, analyzing, and visualizing MOSFET characterization data from CSV files. Automatically detects the measurement type and routes it to the correct parser and plot.

## Features

- **Auto-detection** of measurement type based on column names
- **Interactive plots** with hover tooltips via `mplcursors`
- Supports the following characterizations:
  - **RDSon** — On-resistance vs VDS, grouped by VGS
  - **IG** — Gate current vs VGS, grouped by VDS
  - **3rd Quadrant** — IDSabs vs VDSabs, grouped by VGS

## Requirements

Install dependencies with:

```bash
pip install numpy matplotlib mplcursors
```

Python 3.11+ recommended.

## Usage

```bash
python main.py
```

A file dialog will open — select a `.csv` characterization file. The tool will automatically detect the measurement type and plot it.

## CSV Format

The tool expects CSV files in the following format:

```
DataName, VDS, IDS, VGS, RDSon
DataValue, 0.1, 0.5, 15.0, 0.015
DataValue, 0.2, 1.0, 15.0, 0.016
...
```

Column names are matched case-insensitively. Supported column names per measurement type:

| Measurement | Required Columns |
|-------------|-----------------|
| RDSon | `VDS`, `IDS`, `VGS`, `RDSon` |
| IG | `VDS`, `VGS`, `IG` or `IGabs` |
| 3rd Quadrant | `VDS`, `IDS`, `VDSabs`, `IDSabs` |

## Project Structure

```
plotter/
├── main.py        # Entry point, file selection and routing
├── rdson.py       # RDSon parser and plot
├── igs.py         # IG parser and plot
├── quadrant.py    # 3rd Quadrant parser and plot
└── README.md
```

## Roadmap

- [ ] Executable builds for Windows, macOS, and Linux
- [ ] GUI for file selection and settings
- [ ] Multiple file selection — plot all files automatically
- [ ] Improved 3rd Quadrant plot separation for better curve distinction
- [ ] Additional characterization parameters beyond the most common ones

## License

MIT
