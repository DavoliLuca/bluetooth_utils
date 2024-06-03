"""import bleak
import asyncio

async def main():
    device = await bleak.BleakScanner.find_device_by_name("Redmi Note 12")
    print("Found device: ", device)
    return device

asyncio.run(main())
"""
import asyncio
import bleak
from bleak import BleakScanner
import time

async def get_list_available_devices():
    devices = await BleakScanner.discover(return_adv=True)
    print(devices.keys())
    #print(len(devices))
    return devices

def find_device_uuid():
    devices_pre = asyncio.run(get_list_available_devices())
    #print(len(devices_pre))
    input("Activate your bluetooth device")
    time.sleep(5)
    devices_post = asyncio.run(get_list_available_devices())
    #print(len(devices_post))
    result = []
    for d in devices_post:
        if d not in devices_pre:
            result.append(d)
    input("Deactivate your bluetooth device")
    for i, r in enumerate(result):
        if r in devices_post:
            result.pop(i)
    #print(result)
    return result

async def get_device_by_address(address):
    device = await BleakScanner.find_device_by_address(address)
    return device

"""async def get_adv():
    scanner = BleakScanner()
    async for bd, ad in BleakScanner.advertisement_data(BleakScanner):
        print(ad.local_name)
    lambda
    if filterfunc(bd, ad):
        return bd
"""

async def print_adv():
    scanner = BleakScanner
    try:
        async with asyncio.timeout(10):
            async for bd, ad in scanner.advertisement_data():
                try:
                    print(ad.local_name)
                except:
                    print("ex")
                    pass
    except asyncio.TimeoutError:
                print("tim")
                return None

async def get_adv():
     await print_adv()


while 1:
    devices = asyncio.run(get_list_available_devices())
    if "70:09:71:95:63:43" in devices.keys():
        print("IT'S ON")

'''for k in devices.keys():
     print(k)
     print(devices[k][1].local_name)

# print(devices)

result = find_device_uuid()

asyncio.run(get_adv())

BleakScanner.find_device_by_name
address = "6B:CB:AC:6A:9C:AC"

addresses = find_device_uuid()
address = addresses[0]

device = asyncio.run(get_device_by_address(address))
if device is None:
    print(f"No device was found with the {address} address")
else:
    print(device)
    print(type(device))'''
