# **intercom**

[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://opensource.org/licenses/mit)

Intercom test - distancer.

Usage
```console
$ intercom FPATH
```

Example:
```console
$ intercom customer.txt
```

You can use `--help` to print help message.
```console
$ intercom --help
Usage: intercom [OPTIONS] FPATH

Options:
  --help  Show this message and exit.
```

# Installation
Install the cli tool using the following command:

```console
$ python3 setup.py install
```

# Development

For development of this tool, you need to install the required dependencies. (Use of virtual environments are strongly suggested)

```console
$ python3 -m virtualenv venv
$ source ./venv/bin/activate
# pip install -r requirements.txt
```

For running the unit tests:
```console
(venv) $ python3 -m unittest tests -v
```

# To do
- Write better documentation.
- Write better tests.

***

Tested with Python 3.8.9 on macOS 10.15.7