# System Setup Utils

This is kind of a wrapper around that allows us to run bash commands easily from Python.

No more YML files or configurations.

Simple Python functions for common tasks.

## Getting started

### Installation

Install the repository using `pip`

```bash
pip install https://github.com/Mittal-Analytics/system-setup/archive/main.zip
```

### Usage

Start using the functions

``` python
from system_setup import utils as setup

# create directory
setup.bash('mkdir -p /home/ubuntu/project')

# initialize git directory
setup.bash('git init /home/ubuntu/repos')

# run sudo commands
setup.bash('sudo mkdir -p /app')

# replace line in a file
setup.replace_line('/etc/hosts/', '#127.0.0.1 foobar.com', '127.0.0.1 foobar.com')
```

### Recipes

These are few common recipes already included.

[todo]


## Development

Please create a pull-request to contribute more common utils.

### Publishing new releases

Update the version in `setup.py`. The create the release.

```bash
python setup.py sdist
```