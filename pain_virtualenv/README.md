# Description

This is my awersome research on virtual environments. The article is available at doi:10.1111/1000-7 
You can easily reproduce my results by running scripts locally.
Please cite me!

## Usage

### This directory contains following files:
File | Description
------------ | -------------
pain.py | script we extremely want to run
requirements.txt | list of modules required to run the script pain.py
README.md | instructions for running the script pain.py and installing the modules required for it

### These files should be downloaded in one directory together.

### Make new directory and go to this directory (pain, for example):
```
mkdir pain
cd pain
```

### Download files from these directory to your new directory pain

### Requirements:
OS: Ubuntu 18.04.
Python 3.9.7, versions, older than 3.9 and newer as Python 3.10 are currently not supported by the script and its requirements

### Installing Python 3.9.7:
```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.9
sudo apt-get install python3.9-venv
```

If any errors raised, try update and upgrade your OS and try again:
```
sudo apt-get update && sudo apt-get upgrade
```

### Installing virtual environment (virtualenv):
```
python3 -m pip install virtualenv
```

### Making new virtual environment named pain:
```
python3.9 -m venv pain
```

### Activating new virtual environment named pain:
```
source pain/bin/activate
```

### Upgrade pip and setuptools:
```
python3 -m pip install --upgrade pip setuptools
```

### Installing modules crucial to successfully RUN pain.py:
```
pip install -r requirements.txt
```

### RUN the script pain.py
```
python3 pain.py
```
### To deactivate virtual environment type:
```
deactivate
```

### To delete virtual environment delete its directory:
```
rm -r ./pain
```
