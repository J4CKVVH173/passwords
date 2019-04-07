from argparse import ArgumentParser
from os.path import expanduser, join

HOME = expanduser("~")


def create_parser() -> ArgumentParser:
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument('-p', '--password', help='password for encoding/decoding (default: 12345678)',
                        default='12345678')
    parser.add_argument('-s', '--sourcefile', default=f'{HOME}/passwords.txt',
                        help='path to file to encoding or path to write to the decode file or dir '
                             '(default: ~/passwords.txt)')
    parser.add_argument('-e', '--encryptedfile', default=f'{HOME}/crypto.txt',
                        help='path to encrypted file (default: ~/crypto.txt)')
    parser.add_argument('-n', '--name', help='output file name')

    return parser

