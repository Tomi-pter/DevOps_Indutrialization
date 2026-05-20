# Challenges

## Table of contents

- [Broken virtual environment](#broken-virtual-environment-due-to-removed-python-installation)
  - [Summary](#summary)
  - [Root cause](#root-cause)
  - [How](#how-it-manifested)
  - [Solution](#solution)

### Broken virtual environment due to removed Python installation

#### Summary:

- While attempting to run the project's development server (`runserver.py`), the virtual environment's Python executable failed with the error:

  "No Python at 'C:\\Users\\Terry\\AppData\\Local\\Programs\\Python\\Python39\\python.exe'"

#### Root cause:

- The project's virtual environment (`env`) was created previously using a system Python installation under the Windows user `Terry`.
- That original Python installation was later removed or is no longer present on the machine, but `env` still points to it via `pyvenv.cfg`.

#### How it manifested:

- Running `.\\env\\Scripts\\python.exe .\\runserver.py` returned: `No Python at 'C:\\Users\\Terry\\AppData\\Local\\Programs\\Python\\Python39\\python.exe'` and exited with code 1
- `env\\pyvenv.cfg` contained the line `home = C:\\Users\\Terry\\AppData\\Local\\Programs\\Python\\Python39`

#### Solution:

1. I recreated the virtual environment using a valid Python installation:

```powershell
# from project root
Remove-Item -Recurse -Force .\\env
py -3 -m venv .\\env
.\\env\\Scripts\\Activate.ps1
python -m pip install -r requirements.txt
python .\\runserver.py
```
