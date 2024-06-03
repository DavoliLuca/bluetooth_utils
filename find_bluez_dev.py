# simple inquiry example
import bluetooth

nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("Found {} devices.".format(len(nearby_devices)))

for addr, name in nearby_devices:
    print("  {} - {}".format(addr, name))
    if "HC-05" in name:
        board_address = addr
        board_name = name

services = bluetooth.find_service(address=board_address)
print(services)
