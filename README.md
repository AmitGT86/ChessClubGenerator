# ChessClubGenerator

This Python script, `tourn.py`, manages chess tournaments. It allows users to create tournaments, manage existing ones, register players, and enter match results.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need Python installed on your system. The script is tested with Python 3.8 and above. You also need to install several packages to run the script and generate reports.

### Installing

First, clone the repository or download the source code to your local machine. Then, navigate to the directory containing `tournament_manager.py` and run the following command to install the required Python packages:

```bash
pip install flake8 flake8-html

To generate flake html report :
flake8 --format=html --htmldir=flake-report tournament_manager.py

