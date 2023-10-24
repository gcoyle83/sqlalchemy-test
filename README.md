# Setup
This repository hosts a simple `sqlite3` test. It is designed for relatively easy spin-up of the test notebook on a user's local machine, selecting one of the following options (user's choice):

-  Option A - Use an existing environment to run the notebook; requirements are Python 3.10 to 3.12 (tested), and only core Python modules are used (no additional packages required). Probably the quickest route if available.
-  Option B - If conda is already installed, navigate to the repo root and use the environment.yaml file: `conda env create --file environment.yaml`. Creates sufficient conda environment named `bcsql_env` with an IPython kernel. Fewer steps but may take just as long as Option C for conda to solve the environment. 
-  Option C - Follow these instructions to quickly build a Python 3.12 virtual environment for this project which can be deleted later:
    -  If system Python is not 3.12, download and install it [from the official site](https://www.python.org/downloads/) to default location
    -  Create a py312 virtual environment with required packages by running `C:\Users\<user>\AppData\Local\Programs\Python\Python312\python -m venv .venv` (or similar, depending on your install location and OS) from the local repo root
    -  Activate the virtual env with `.venv/Scripts/Activate.ps1` (Powershell) or `.venv/Scripts/activate` (Bash)
    -  Add required packages with `pip install -r requirements.txt`

Whichever of the above options are selected, next open your IDE of choice, if not already there from above and then open `src/skill-test.ipynb` and select the desired kernel, follow prompts to complete test.

# Suggested Testing Format
Testing is on screen, open Internet. Take 5 minutes to introduce the repo and test, then user has:

-  ~5 minutes to set up test environment as directed above
-  Provide 15 minutes for coding questions, then stop
-  Provide 5 minutes for data model discussion questions