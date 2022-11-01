import argparse

def getArguments():
    parser=argparse.ArgumentParser()
    parser.add_argument("--keywords",
        default = "keywords.txt",
        type = str,
        help = "Keywords file.")
    parser.add_argument("--rules",
        default = "rules.txt",
        type = str,
        help = "Rules file")
    parser.add_argument("--conllup",
        default = None,
        required = True,
        type = str,
        help = "CoNLL-U Plus file containing the legal reference annotation to be classified.")

    args=parser.parse_args()
    return args
