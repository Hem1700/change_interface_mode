
import subprocess
#import optparse
import argparse
import re

def change_mode(interface, mode):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["iwconfig", interface, "mode", mode])
    subprocess.call(["ifconfig", interface, "up"])


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change its mode")
    parser.add_argument("-m", "--mode", dest="mode", help= "Mode to change its mode")
    options = parser.parse_args()
    if not options.interface:
        parser.error("[+] Please specify an interface, use --help for further information")
    if not options.mode:
        parser.error("[+] Please specify a mode, use --help for further information")
    return options


def get_mode(interface):
    iwconfig_result = subprocess.check_output(["iwconfig", interface])
    mode_search_result = re.search(r"Mode:\D\D\D\D\D\D\D", iwconfig_result.decode("utf-8"))
    if mode_search_result:
        return mode_search_result.group(0)


options = get_arguments()
current_mode = get_mode(options.interface)
change_mode(options.interface, options.mode)
print(current_mode)
current_mode=get_mode(options.interface)
print(current_mode)

