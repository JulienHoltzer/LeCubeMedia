import os
os.system('sudo iwlist wlan1 scan | grep ESSID > scanresults')
f = open ('scanresults', "r")
w = open('listssidfromscan', "w")

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
outfile = open('listssidfromscanfin', "w")
r = open('listssidfromscan', "r")
for line in r:
	if line not in seenlines:
		outfile.write(line)
		seenlines.add(line)

outfile.close()

