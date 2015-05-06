import os
#scan available networks
os.system('sudo iwlist wlan1 scan | grep ESSID > networks')		
f = open('networks', "r")
w = open('listssid', "a")

for line in iter(f):
	
	prevline = ""
	words = line.split(":")
	for i in words:
		if 'ESSID' in prevline:
			ssid = i[1:-1].rstrip('"')
			if ssid != "":
				print ssid
				w.write(ssid + "\n")
		prevline = i
	
			
w.close()
f.close()

seenlines = set()
outfile = open('ssidlistfin', "w")
w = open('listssid', "r")
for line in w:
	if line not in seenlines:
		outfile.write(line)
		seenlines.add(line)


outfile.close()