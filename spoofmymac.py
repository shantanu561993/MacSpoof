import spoofmac
from netifaces import interfaces

print "You have following interfaces on your system"
a=interfaces()
for i in len(a):
	print str(i+1)+") "+a[i]
	
	

print "Enter interface number you want to spoof MAC of "
mac_num=int(raw_input())
if mac_num>len(a):
	print "You Entered invalid number"
	print "Exiting"
else:
	mac_inr=a[mac_num-1]
	b=spoofmac.find_interface(mac_inr)
	print "Type : %s Name : %s CURRENT_MAC : %s " %(b[0],b[1],b[2])
	
	
	
