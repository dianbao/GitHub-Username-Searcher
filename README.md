# GitHub-Username-Searcher
[![GitHub stars](https://img.shields.io/github/stars/i6x/GitHub-Username-Searcher.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/i6x/GitHub-Username-Searcher/stargazers/)
[![GitHub followers](https://img.shields.io/github/followers/i6x.svg?style=social&label=Follow&maxAge=2592000)](https://github.com/i6x?tab=followers)
[![Requirements Status](https://requires.io/github/i6x/GitHub-Username-Searcher/requirements.svg?branch=master)](https://requires.io/github/i6x/GitHub-Username-Searcher/requirements/?branch=master)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
[![Run on Repl.it](https://repl.it/badge/github/i6x/GitHub-Username-Searcher)](https://repl.it/github/i6x/GitHub-Username-Searcher)

A script to automate checking the avaliability of bulk usernames

## Installation
```bash
git clone https://github.com/i6x/GitHub-Username-Searcher
cd GitHub-Username-Searcher
chmod +x check  # Unix only
```
## Usage
Usernames to search for should be a stored in a text file with each username seperated by a line break

To check for three-character avaliable usernames from a file using the sample provided run the following:
```bash
# Unix
./check 3char.txt
```
```powershell
# Windows
py -3 check 3char.txt
```
This will check `3char.txt` for avaliable usernames using 100 threads, this may take a while depending on how many usernames are being checked and how powerful your processor is. You can specify how many threads to use by providing an additional argument
```bash
# Unix
./check 3char.txt 69
```
```powershell
# Windows
py -3 check 3char.txt 69
```
This will use 69 threads rather than the default 100 to check usernames. More threads will return faster results but will also use more resources. 

If you wish to exit the program while it is running please do not close your terminal's window because depending on your distro this may or may not kill the program completely, instead, you should use <kbd>CTRL</kbd>+<kbd>C</kbd>.


