import subprocess
import optparse
import re


def param_parse()
	#function to take the inputs and arguments
	parser=optparse.OptionParser()

	parser.add_option("-i","--interface",dest="inter",help="Interface to change the mac address")
	parser.add_option("-m","--new_mac",dest="macname",help="The new mac address")

	(options,arguments)=parser.parse_args()

	if not in option.inter:
		parser.error("please input the interface")

	if not in opiton.macname:
		parser.error("please input the mac ID")

	return options

def change_mac(interace,macname):
	#core function for chaning mac address
	subprocess.call(["ifconfig",inter,"down"])
	subprocess.call(["ifconfig",inter,"hw","ether",macname])
	subprocess.call(["ifconfig",inter,"up"])

def current_mac(interface):
	ifconfig_result=subprocess.check_output(["ifconfig",interface])

	captured_mac=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)

	if captured_mac:
		return captured_mac.group(0)

	else:

		print("could not get mac address")


options=param_parse()

now_mac=current_mac(options.inter)

print("Current mac ID " + str(now_mac))

change_mac(options.inter,options.macname)


now_mac=current_mac(options.inter)

if now_mac ==  options.macname:

	print("Mac address has changed to ",now_mac)

else:
	print("mac address not changed")
