from Crypto.Cipher import DES
from tools import create_parser, pad, join

if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()

    key = namespace.password.encode()
    key = pad(key)

    des = DES.new(key, DES.MODE_ECB)

    try:
        # try to open file with passwords
        file = open(namespace.sourcefile, 'r')
    except FileNotFoundError:
        # if file dose note found, close the program
        print('Source file not found')
        raise SystemExit(1)

    passwords = file.read().encode()
    file.close()
    passwords = pad(passwords)

    encrypted_text = des.encrypt(passwords)

    path = namespace.encryptedfile
    name = namespace.name

    try:
        # open or create file via path
        file = open(path, 'wb')
    except IsADirectoryError:
        # if path with out name, try to create or open file with name
        file = open(join(path, name), 'wb')
    except FileNotFoundError:
        # can not fined dir with file
        print('No such file or dir')
        raise SystemExit(1)
    except:
        print('Path error')
        raise SystemExit(1)


    file.write(encrypted_text)
    file.close()

