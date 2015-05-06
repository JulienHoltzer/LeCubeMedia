f = open('/etc/wpa_supplicant/wpa-roam.conf', "r")
w = open('result', "w")

for line in iter(f):
	result = open('result', "w")
	target = "ssid"
	words = line.split("=")
	prevline = ""
	for line in words:
		if 'ssid' in prevline:
			ssid = line[1:-1].rstrip('"')
			print ssid
			w.write(ssid + "\n")
		prevline = line
	
			
w.close()
f.close()