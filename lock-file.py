from Crypto.Cipher import AES
from tools import create_parser, join
from Crypto.Util.Padding import pad
from base64 import b64encode

if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()

    key = namespace.password.encode()
    key = pad(key, AES.block_size)

    cipher = AES.new(key, AES.MODE_CBC)

    try:
        # try to open file with passwords
        file = open(namespace.sourcefile, 'r')
    except FileNotFoundError:
        # if file dose note found, close the program
        print('Source file not found')
        raise SystemExit(1)

    passwords = file.read().encode()
    file.close()

    encrypted_bytes = cipher.encrypt(pad(passwords, AES.block_size))

    path = namespace.encryptedfile
    name = namespace.name

    iv = b64encode(cipher.iv).decode('utf-8')
    encrypted = b64encode(encrypted_bytes).decode('utf-8')

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

    file.write(iv + encrypted)
    file.close()
