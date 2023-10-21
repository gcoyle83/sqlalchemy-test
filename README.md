# Setup

-  First clone the repo
-  If system Python is not 3.12, download and install it to default location
-  Create a py312 virtual environment by running `C:\Users\<user>\AppData\Local\Programs\Python\Python312\python -m venv .venv` (or similar, depending on your install location and OS) from the local repo root
-  Activate the virtual env with `.venv/Scripts/Activate.ps1` (Powershell) or `.venv/Scripts/activate` (Bash)
-  Add required packages with `pip install -r requirements.txt`
-  Open IDE of choice, if not already there from above (tested in VS Code)
-  Open `src/sql-test.ipynb` and select the local .venv kernel, follow prompts