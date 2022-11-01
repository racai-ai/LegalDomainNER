# Python implementation

This folder contains the Python command-line implementation.

```
usage: rule_based.py [-h] [--keywords KEYWORDS] [--rules RULES] --conllup CONLLUP

optional arguments:
  -h, --help           show this help message and exit
  --keywords KEYWORDS  Keywords file.
  --rules RULES        Rules file
  --conllup CONLLUP    CoNLL-U Plus file containing the legal reference
                       annotation to be classified.
```

Creating a venv to run this application:
```
python3 -m venv venv

source venv/bin/activate

pip3 install numpy
```

Example:
```
python rule_based.py --conllup test.conllup
ordin
```
