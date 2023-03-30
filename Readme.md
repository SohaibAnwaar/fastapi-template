# CMMS System

Description

# Pre Requisite

1. Python 3.9.13
2. Conda (For making virtual Environemnts you can also use pyenv)
3. Postgres and PGAdmin (TO view data)


# Start Backend Server

Install conda first 
[(Click Here)](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

After Installation make Conda virtual environment

```
# Creating conda env
conda create -n cmms python=3.10

# Activating conda env
conda activate cmms 

# Install required packages
pip install -r requirements.txt

```

Run Server
```
# Go to the code folder
cd <code_folder>

# Run Database migrations
alembic head upgrade

# Run Server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Run API documentation
http://localhost:8000/docs
```


# API documentation

After starting the server go to the link

http://localhost:8000/docs


# Test Cases
Run test-cases with following commands
```
pytest # Run without showing print in code.


pytest -s # Run and show prints inside code.
```