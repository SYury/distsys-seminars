import socket
import struct
import time


if __name__ == '__main__':
    time.sleep(2)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, struct.pack('b', 1))
    sock.sendto(b'hello from sender', ('224.0.2.0', 10000))
    sock.close()
