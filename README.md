# GitHub-Username-Searcher
A script to automate checking the avaliability of bulk usernames

## Installation
```bash
git clone https://github.com/i6x/GitHub-Username-Searcher
cd GitHub-Username-Searcher
chmod +x check
```
## Usage
Usernames to search for should be a stored in a text file with each username seperated by a line break

To check for avaliable usernames from a file run the following:
```bash
./check filename.txt
```
This will check `filename.txt` for avaliable usernames using 100 threads, this may take a few seconds or a few minutes depending on how many usernames are being checked and how powerful your processor is. You can specify how many threads to use by providing an additional argument
```bash
./check filename.txt 69
```
This will use 69 threads rather than the default 100 to check usernames. More threads will return faster results but will also use more resources. 

If you wish to exit the program while it is running please do not close your terminal's window because depending on your distro this may or may not kill the program completely, instead, you should use <kbd>CTRL</kbd>+<kbd>C</kbd>.
