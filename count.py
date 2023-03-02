import argparse
import os
import sys
from collections import defaultdict

def get_args():
    try:
        parser = argparse.ArgumentParser(allow_abbrev=False,
            description='Character, line, word counter')
        parser.add_argument('path', type=str, metavar='path',
            help="path to data")
        args = parser.parse_args()
        path = args.path
        return path
    except Exception as ex:
        print(ex, file=sys.stderr)
        sys.exit(2)

def read_text_file(file_path):
    cc = 0
    lc = 0
    wc = 0
    with open(file_path, 'r') as f:
        txt = f.read()
        cc = len(txt)
        lc = len(txt.split('\n'))
        wc = len(txt.split())
        return cc, lc, wc

def main():
    root = "/Users/alicelee/Desktop/IW"
    path = get_args()
    char_counts = defaultdict(int)
    line_counts = defaultdict(int)
    word_counts = defaultdict(int)
    pwd = os.path.join(root, path)
    os.chdir(pwd)
    for file in os.listdir():
        if file.endswith(".txt"):
            file_path = f"{pwd}/{file}"
            fname = os.path.basename(file)
            cc, lc, wc = read_text_file(file_path)
            char_counts[fname] = cc
            line_counts[fname] = lc
            word_counts[fname] = wc
    for title in char_counts:
        print(title)
        print("---------------------------------------")
        print("Character count:", char_counts[title])
        print("Line count:", line_counts[title])
        print("Word count:", word_counts[title])
        print()

if __name__ == "__main__":
    main()