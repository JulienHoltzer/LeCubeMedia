t = open('ssidadd', 'r')
target = t.read()
t.close()

targetfin = target.split(':::', 1)
<<<<<<< HEAD

if targetfin[1] is '':
	regex = "\n\n\nnetwork={\n\tssid=\"" + targetfin[0] + "\"\n}" 

else:

	#print targetfin

	regex = "\n\n\nnetwork={\n\tssid=\"" + targetfin[0] + "\"\n\tpsk=\"" + targetfin[1] + "\"\n}" 



=======
#print targetfin

regex = "\n\n\nnetwork={\n\tssid=\"" + targetfin[0] + "\"\n\tpsk=\"" + targetfin[1] + "\"\n}" 
>>>>>>> dddaf02d6399abb420d8fd5408cc483ff301f5b8

w = open('/etc/wpa_supplicant/wpa-roam.conf', 'a')
w.write(regex)
w.close()