from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from tools import create_parser, join, ArgumentParser
from base64 import b64decode


if __name__ == '__main__':
    parser: ArgumentParser = create_parser()
    namespace = parser.parse_args()

    try:
        file = open(namespace.encryptedfile, 'r')
    except:
        print('Encrypted file path error')
        raise SystemExit(1)
    crypto: str = file.read()
    file.close()

    key: bytes = namespace.password.encode()
    key = pad(key, AES.block_size)

    iv = b64decode(crypto[0:24])
    ct = b64decode(crypto[24:])

    cipher: AES = AES.new(key, AES.MODE_CBC, iv)
    try:
        data: bytes = unpad(cipher.decrypt(ct), AES.block_size)
    except ValueError:
        print("Error password")
        raise SystemExit(1)

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
