



s = "ssid=\"TP-LINK_6EE4A8\""




target = "ssid"
words = s.split("=")
for i,w in enumerate(words):
	if w == target:
		# print the next word
		words = words[i+1]

		# print the next word
		print words[1:-1].rstrip('"')
		