#open file to read
f = open('test', "r")
#open file to write
w = open('listssidfromfile', "w")

for line in iter(f):

	target = "ssid"
	words = line.split("=")
	prevline = ""

	#if previous line is ssid, take current line
	for line in words:
		if 'ssid' in prevline:
			ssid = line[1:-1].rstrip('"')
			print ssid
			w.write(ssid + "\n")
		prevline = line


w.close()
f.close()