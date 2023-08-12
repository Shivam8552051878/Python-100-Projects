import subprocess
import optparse
import re
subprocess.call(["clr"])
parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its Mac address")
parser.add_option("-m", "--mac", dest="new_mac", help="Your new mac address")
(option, arg) = parser.parse_args()
interface = option.interface
new_mac = option.new_mac
subprocess.call("ifconfig", shell=True)
subprocess.call(f"ifconfig {interface} down", shell=True)
subprocess.call(f"ifconfig {interface} hw ether {new_mac}", shell=True)
subprocess.call(f"ifconfig {interface} up", shell=True)

print(f"Your new Mac address: {new_mac} for interface: {interface}")

def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its Mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="Your new mac address")
    (option, argument) =  parser.parse_args()
    if not option.interface:
        parser.error("[-] Please specify an INTERFACE, use --help for more info.")
    elif not option.new_mac:
        parser.error("[-] Please specify an MAC, use --help for more info.")
    else:
        return option


# ew5090 ryzer gems


# parser = optparse.OptionParser()
# parser.add_option("-i", "--interface", dest="interface", help="Interface to change its Mac address")
# parser.add_option("-m", "--mac", dest="new_mac", help="Your new mac address")
# (option, arg) = parser.parse_args()
# interface = option.interface
# new_mac = option.new_mac

mac_address_search_resault = subprocess.check_output(["ifconfig", option.interface])

re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", mac_address_search_resault)

if mac_address_search_resault:
    print(mac_address_search_resault.group(0))
else:
    print("[-] Could not found MAC address.")