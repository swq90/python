import sys
import struct
import os.path
from socket import socket


def sendfile():
    client = socket()
    client.connect(('10.0.0.10', 666))

    # file_name = sys.argv[1]
    # file_path = sys.argv[2]
    # file_name = byte(input('filename'))
    file_name = input('filename')
    file_path = os.getcwd()
    print(file_path + "\\" + file_name)
    # file_first = struct.pack('1024s',file_name)
    client.send(bytes(file_name, encoding="utf8"))

    print ('b')
    with open(file_path + "\\" + file_name, 'rb') as fp:
        for line in fp:
            client.send(line)
    print('p')
    client.close()


if __name__ == '__main__':
    sendfile()
