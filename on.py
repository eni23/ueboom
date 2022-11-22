#!/usr/bin/env python3

import bleak
import asyncio

# ue boom bluetooth mac address
UE_BOOM_MAC = "10:94:97:05:5F:38"

# any mac that was paired to ue boom works here
MY_MAC = "F4:7B:09:A2:6A:E2"

# service to turn on 
PWR_ON = "c6d6dc0d-07f5-47ef-9b59-630622b01fd3"

async def main():
  ble_msg = bytearray.fromhex(MY_MAC.replace(":",""))
  ble_msg.append(1)
  dev = bleak.BleakClient(UE_BOOM_MAC)
  await dev.connect()
  await dev.write_gatt_char(PWR_ON, ble_msg)

if __name__ == '__main__':
  asyncio.run(main())