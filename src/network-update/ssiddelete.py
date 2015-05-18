import re

t = open('ssiddelete', 'r')
target = t.read()
regex = "network=\{\s*ssid=\"" + target + "\"[^}]*.*?" + "}"

#define points to cut -> regex
cut = re.compile(regex, re.DOTALL)

f = open('wpa-roam.conf', 'r')
data = f.read()
f.close()

#cut
data_cut = cut.sub('', data)


#print data_cut

f = open('wpa-roam.conf', 'w')	
f.write(data_cut)
f.close()