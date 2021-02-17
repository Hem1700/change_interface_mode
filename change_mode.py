
import subprocess
import optparse

def change_mode(interface, mode):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["iwconfig", interface, "mode", mode])
    subprocess.call(["ifconfig", interface, "up"])


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its mode")
    parser.add_option("-m", "--mode", dest="mode", help= "Mode to change its mode")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[+] Please specify an interface, use --help for further information")
    if not options.mode:
        parser.error("[+] Please specify a mode, use --help for further information")
    return options


def get_mode():
    print("")

options = get_arguments()
change_mode(options.interface, options.mode)


