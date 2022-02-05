# namegen
This tool is a simple names / ideas generator.<br>
Specify list of keywords to get randomly paired synonyms (produced by NLTK).<br>
The tool works offline but NLTK will need to download its dictionaries. Note, that NLTK library downloads its dictionaries to user's home directory. You may want to remove them after using the generator.<br>
The results are sorted alphabetically.<br>
# Examples
Generate up to 20 names using given keywords:
```
$ namegen --count 20 fancy flower design view image
blossom image
design blossom
design image
efflorescence view
figure aspect
flower design
flower designing
fondness flower
image bloom
image position
image survey
image view
partiality flower
pattern image
prime position
project blossom
range eyeshot
see bloom
sight intention
view double
```
By default names consist of 2 components. Use `--components` (or `-m`) option to override this setting.<br>
Find synonyms for the word "source":
```
$ namegen --components 1 source
author
beginning
generator
informant
reference
reservoir
root
rootage
seed
source
```

# Installation
## Requirements
Python >= 3.6

## Install
Use pip:
```
git clone https://github.com/fuzzah/namegen
cd namegen
pip install .
```
## Uninstall
To uninstall use pip:
```
pip uninstall namegen
```
You may also want to remove nltk_data folder in your home directory.
