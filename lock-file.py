from Crypto.Cipher import DES
from tools import create_parser, pad, HOME, join

if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()

    key = namespace.password.encode()
    key = pad(key)

    des = DES.new(key, DES.MODE_ECB)

    file = open(namespace.sourcefile, 'r')
    passwords = file.read().encode()
    file.close()
    passwords = pad(passwords)

    encrypted_text = des.encrypt(passwords)

    encoding_path: list = namespace.encryptedfile.split('.')
    encoding_dir_path = encoding_path[0]

    if len(encoding_path) == 2:
        file = open(namespace.encryptedfile, 'wb')
    elif len(encoding_path) == 1:
        if namespace.name is None:
            file = open(join(encoding_dir_path, 'crypto.txt'), 'wb')
        else:
            file = open(join(encoding_dir_path, namespace.name), 'wb')
    else:
        raise Exception('Error path to encoding file')
    file.write(encrypted_text)
    file.close()

