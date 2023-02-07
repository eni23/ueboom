#!/usr/bin/env python3

UE_BOOM_MAC = "10:94:97:05:5F:38"
service_uuid = "00001800-0000-1000-8000-00805f9b34fb"
characteristic_uuid = "00002a00-0000-1000-8000-00805f9b34fb"

async def main():
    async with BleakClient(UE_BOOM_MAC) as client:
        value = await client.read_gatt_char(characteristic_uuid)
        print(str(value, "utf-8"))

if __name__ == '__main__':
    asyncio.run(main())
