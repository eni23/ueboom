import asyncio
from bleak import BleakClient

async def run(UE_BOOM_MAC, loop, service_uuid, characteristic_uuid):
    async with BleakClient(UE_BOOM_MAC, loop=loop) as client:
        value = await client.read_gatt_char(characteristic_uuid)
        print(str(value, "utf-8"))

UE_BOOM_MAC = "C0:28:8D:8F:C3:6F"
service_uuid = "00001800-0000-1000-8000-00805f9b34fb"
characteristic_uuid = "00002a00-0000-1000-8000-00805f9b34fb"
loop = asyncio.get_event_loop()
loop.run_until_complete(run(UE_BOOM_MAC, loop, service_uuid, characteristic_uuid))
