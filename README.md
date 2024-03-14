# simple_etl


1. Clone the repository:
```bash
git clone https://github.com/aguiarpaulo/simple_etl.git
cd simple_etl
```
2. Configure the correct Python version with `pyenv`:
```bash
pyenv install 3.11.3
pyenv local 3.11.3
```
3. Install project dependencies:
```bash
poetry shell
poetry install
```
4. Run and test the project:
```bash
poetry run python pipeline.py
```