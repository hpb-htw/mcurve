# Mcurve

A Project to lern Python Module and PyPi

# Howto


* Setup an venv

Do this Task just once after clone project

```shell
pip install venv
python -m venv .venv
```

Venv have to be activated (each times before development)

```shell
source .venv/bin/active
```

* Run all tests

Venv must be activated before, then

```shell 
# Install this package into venv
# Just once
pip install -e .
```

Each times you change your code, run

```shell
python -m unittest discover -p "*_test.py"
```

to tests alle units of the project

