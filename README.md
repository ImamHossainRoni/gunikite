#  🐎 GuniKite

`gunikite` is a utility class for running Gunicorn servers from a virtual environment. It helps you find the location of the Gunicorn executable within the virtual environment and run it with specified parameters.

## Installation

You can install `gunikite` using pip:

```shell
pip install gunikite
```


## Usage

```python
from gunikite import GunicornRunner

# Create a GunicornRunner instance
gunicorn_runner = GunicornRunner(
    worker=4,
    host="localhost",
    port=8080,
    module_name="myapp",
    app_class_name="app",
    enable_reload=True
)

# Run Gunicorn with the specified parameters
gunicorn_runner.run_gunicorn()
