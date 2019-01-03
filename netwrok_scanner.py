import scapy.all as scapy
import argparse



def get_argument():
	parser=argparse.ArgumentParser()
	parser.add_argument("-ip","--ipaddress",dest="target",help="target ip/range")
	options=parser.parse_args()

	return options

def scan(ip):

	arp_request=scapy.ARP(pdst=ip)
	broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	packet=broadcast/arp_request # '/' is the sign for appending 
	answered,unanswered=scapy.srp(packet,timeout=1,verbose=False)
	# or above code can be written as 
	#answered=scapy.srp(packet,timeout=1)[0]
	print("IP \t\t\t\t  MAC address ")
	print("---------------------")
	for element in answered:

		print(element[1].psrc + "\t\t\t"+ element[1].hwsrc)
			
		print("---------------------")


options=get_argument()

scan(options.target) 