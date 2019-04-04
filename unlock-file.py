from Crypto.Cipher import DES
from tools import create_parser, pad, join, ArgumentParser


if __name__ == '__main__':
    parser: ArgumentParser = create_parser()
    namespace = parser.parse_args()

    file = open(namespace.encryptedfile, 'rb')
    crypto: bytes = file.read()
    file.close()

    key: bytes = namespace.password.encode()
    key = pad(key)

    des: DES = DES.new(key, DES.MODE_ECB)
    data: bytes = des.decrypt(crypto)

    file_info: list = namespace.sourcefile.split('.')
    # path to dir with decoding file
    file_path: str = file_info[0]
    file_name: str = ''

    if len(file_info) == 2:
        # if path has file name
        file = open(file_path, 'w')
    elif len(file_info) == 1:
        # if only path to dir, set base file name or users (via key --name)
        if namespace.name is None:
            file_name: str = 'passwords.txt'
        else:
            file_name: str = namespace.name
        file = open(join(file_path, file_name), 'w')
    else:
        raise Exception('Error output file name')

    try:
        # password is write
        file.write(data.decode())
    except UnicodeDecodeError:
        # password is wrong
        file.close()
        if len(file_info) == 2:
            file = open(file_path, 'wb')
        else:
            file = open(join(file_path, file_name), 'wb')
        file.write(data)
    file.close()
