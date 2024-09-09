# Python .gitignore Updater

A flexible tool to update your `.gitignore` file with common patterns for various programming languages and environments.

## Features

- Easily extendable to support new pattern sets
- Command-line interface with flags for each supported pattern set
- Automatically creates .gitignore file if it doesn't exist
- Adds patterns without duplicating existing entries

## Installation

To use this tool, you need both the main script and the patterns folder. To get started:

1) Clone the repo

```bash
git clone https://github.com/griffinbaker12/gitignore-updater.git
cd gitignore-updater
chmod +x gitignore_updater.py
```

2) Set up an alias (optional, but recommended)

Add this line to your shell configuration file (e.g., .bashrc, .zshrc):

```bash
alias update-gitignore="python3 /path/to/gitignore_updater.py"
```

Replace `/path/to/gitignore_updater.py` with the actual path where you saved the script.

## Usage

Run the script in your project directory:

```bash
python3 /path/to/gitignore_updater.py [OPTIONS]
```

Or, if you set up an alias:

```bash
update-gitignore [OPTIONS]
```

## Options

- `--python`: add Python patterns (default if no options selected)
- ... (insert your custom option here)

You can combine multiple options:

```bash
python3 gitignore_updater.py --python --your-custom-option
```

## Adding New Patterns

1) Navigate to the patterns directory.
2) Create a new text file named after the language or environment (e.g., rust.txt).
3) Add the patterns, one per line.
4) The script will automatically recognize the new pattern set and add a corresponding command-line option.


## Contributing

Please feel free to open a PR to add a cli argument for any patterns that you catch yourself typing a lot!

## License

[MIT License](LICENSE)
