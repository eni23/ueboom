#!/usr/bin/env python3

import socket

# ue boom bluetooth mac address
UE_BOOM_MAC = "10:94:97:05:5F:38"

# ue boom spp bt channel 
UE_BOOM_PORT = 1

# message to turn the speaker off
UE_BOOM_OFF_MSG = b'\x02\x01\xb6'

def main():
  dev = socket.socket(
    socket.AF_BLUETOOTH, 
    socket.SOCK_STREAM, 
    socket.BTPROTO_RFCOMM
  )
  dev.connect((
    UE_BOOM_MAC,
    UE_BOOM_PORT
  ))
  dev.sendall(b'\x02\x01\xb6')
  dev.close()


if __name__ == '__main__':
  main()

