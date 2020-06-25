## Build & package procedure:
- setup and activate a python 3.8 virtual environment in `venv`
- run the following commands:
```
pip install <mysqlclient.whl>
pip install <numpy-mkl.whl>
pip install docutils==0.15.2
pip install .
```
- install `pyinstaller` and copy the numpy hook:
```
pip install pyinstaller
cp hooks/hook-numpy.py venv/Lib/site-packages/PyInstaller/hooks
```
- package the .exe with:
```
pyinstaller cli.spec
```
- to run CellProfiler, you must set the environment variable `CP_JAVA_HOME` to the correct path (e.g., could be the `java` folder of a previous official CellProfiler release)