# Web checker application

The main source code is web_checker.py which uses the requests library to check the response of eacg url parsed. 

The urls are provided via a text file 'urls.txt' meaning any text file can be used in place of this as long as it passes unit tests for valid urls.

Each response from the web check is printed into a logfile and also to a json file which can be used for the optional web interface to monitor the status of the webpages in the list.

Unit tests validate all inputs to web_checker method.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install setup.py

```bash
pip install .
```

## Usage
```bash
python run.py
``'

In general the security measures that would come into consideration for monitoring tools would be:
- strong authentication and authorization mechanism
- role based access control
- data protection measures (encryption, masking, etc)
- compliance with data protection laws
- regular updates on monitoring tool to prevent malware
