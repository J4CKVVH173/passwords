from Crypto.Cipher import DES
from tools import create_parser, pad, join, ArgumentParser


if __name__ == '__main__':
    parser: ArgumentParser = create_parser()
    namespace = parser.parse_args()

    try:
        file = open(namespace.encryptedfile, 'rb')
    except:
        print('Encrypted file path error')
        raise SystemExit(1)
    crypto: bytes = file.read()
    file.close()

    key: bytes = namespace.password.encode()
    key = pad(key)

    des: DES = DES.new(key, DES.MODE_ECB)
    data: bytes = des.decrypt(crypto)

    try:
        passwords = data.decode()
    except UnicodeDecodeError:
        print('Error password')
        raise SystemExit(1)

    path = namespace.sourcefile
    name = namespace.name

    try:
        # open or create file via path
        file = open(path, 'w')
    except IsADirectoryError:
        # if path with out name, try to create or open file with name
        file = open(join(path, name), 'w')
    except FileNotFoundError:
        # can not fined dir with file
        print('No such file or dir')
        raise SystemExit(1)
    except:
        print('Path error')
        raise SystemExit(1)

    file.write(passwords)
    file.close()
